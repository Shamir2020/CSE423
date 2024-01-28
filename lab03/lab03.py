import random

def MidpointCircleDrawing(xCenter, yCenter, radius):


    x = 0
    y = radius 
    d = 1 - radius

    points = []

    while x < y:
        if d < 0:
            x = x + 1
        else:
            x = x + 1
            y = y - 1

        if d < 0:
            d = d + 2*x + 1 
        else:
            d = d + 2 *(x - y) + 1

        points.append((x,y))
        
    zone1 = GenerateZones(points,1)
    zone2 = GenerateZones(points,2)
    zone3 = GenerateZones(points,3)
    zone4 = GenerateZones(points,4)
    zone5 = GenerateZones(points,5)
    zone6 = GenerateZones(points,6)
    zone7 = GenerateZones(points,7)

    points.extend(zone1)
    points.extend(zone2)
    points.extend(zone3)
    points.extend(zone4)
    points.extend(zone5)
    points.extend(zone6)
    points.extend(zone7)


    points2 = []
    for x,y in points:
        points2.append((x+xCenter,y+yCenter))

    return points2


def GenerateZones(points,zone):
    newPoints = []
    for x , y in points:
        a,b = ConvertToZones(x,y,zone)
        newPoints.append((a,b))

    return newPoints

def ConvertToZones(x,y,zone):
    if zone == 0:
        return x,y
    elif zone == 1:
        return y,x
    elif zone == 2:
        return -y,x
    elif zone == 3:
        return -x,y
    elif zone == 4:
        return -x,-y
    elif zone == 5:
        return -y,-x
    elif zone == 6:
        # return y,-x
        return y, -x
    else:
        return x,-y
    


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import midpoint_circle
import time
import threading
import numpy as np

circles = []
colors = []
speed = np.array([])
offset = 1
pause = False


def DiscardCircle(cordinates):
    for x, y in cordinates:
        if x >= 400 or x <= -400:
            return True 
        elif y >= 400 or y <= -400:
            return True

def IncreaseSpeed():
    global speed, offset, pause
    while True:
        if pause:
            pass
        else:
            speed += offset
            time.sleep(0.5)
            # print(f'speed = {speed}')

threading.Thread(target=IncreaseSpeed).start()

def drawAllCircles():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global circles, speed, offset, colors

    i = 0
    while len(circles) != 0:
        if i >= len(circles):
            break
        cordinates = MidpointCircleDrawing(circles[i][0],circles[i][1],20+speed[i])
        color = colors[i]
        discard = DiscardCircle(cordinates)
        if discard:
            circles.remove(circles[i])
            speed = np.delete(speed,i)
            colors.pop(i)
            # print(circles)
        else:
            drawCircle(3,cordinates, color)
        
        i += 1

def drawCircle(width, cordinates, color):
    glPointSize(width)
    
    a, b, c = color 
    glColor3f(a,b,c)
    glBegin(GL_POINTS)
    for x,y in cordinates:
        glVertex2f(x, y)  
        
    glEnd()


def mouseListener(button, state, x, y):
    global circles, speed, pause, colors 
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            # Check for which button was clicked
            # s
            if pause:
                pass
            else:
                circles.append((x-400, 400-y))
                speed = np.insert(speed, len(speed), 1)
                c = [random.random(),random.random(),random.random()]
                colors.append(c)
            



def ListenSpecialKeys(key, x, y):
    global offset


    if key == GLUT_KEY_LEFT:
        # print('Left arrow pressed')
        # Bend rain drops to left
        offset += 1

    if key == GLUT_KEY_RIGHT:
        # print('Right arrow pressed')
        # Bend rain drops to right
        if offset > 1:
            offset -= 1

    glutPostRedisplay()


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-400, 400, -400, 400, 0.0, 1)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    drawAllCircles()


    glutSwapBuffers()

def IdleDisplay():
    global pause
   
    if pause:
        pass 
    else:
        drawAllCircles()
        glutSwapBuffers()

def keyboardListener(key, x, y):
    global pause
    if key==b' ':
        if pause:
            pause = False
        else:
            pause = True


    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800, 800)

glutCreateWindow(b"LAB03")

glutDisplayFunc(showScreen)

glutIdleFunc(IdleDisplay)
glutSpecialFunc(ListenSpecialKeys)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import midpoint_circle
import time
import threading
import numpy as np

circles = []
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
    global circles, speed, offset

    i = 0
    while len(circles) != 0:
        if i >= len(circles):
            break
        cordinates = midpoint_circle.MidpointCircleDrawing(circles[i][0],circles[i][1],20+speed[i])
        discard = DiscardCircle(cordinates)
        if discard:
            circles.remove(circles[i])
            speed = np.delete(speed,i)
            # print(circles)
        else:
            drawCircle(3,cordinates)
        
        i += 1

def drawCircle(width, cordinates):
    glPointSize(width)
    
    glBegin(GL_POINTS)
    for x,y in cordinates:
        glVertex2f(x, y)  
        
    glEnd()


def mouseListener(button, state, x, y):
    global circles, speed, pause
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            # Check for which button was clicked
            # s
            if pause:
                pass
            else:
                circles.append((x-400, 400-y))
                speed = np.insert(speed, len(speed), 1)
            



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


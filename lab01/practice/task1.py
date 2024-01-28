from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

# Draw a Rectangle
raindrops = [(random.uniform(200, 1500), random.uniform(340, 1200)) for _ in range(100)]
rain_offset = 0
color_offset = 0

dynamicColors = [(0,0,0),(1,1,1)]

w,h= 1500,700
def drawHouse():
    glLineWidth(10)

    glBegin(GL_LINES)
    glVertex2f(400, 50)
    glVertex2f(1300, 50)


    glVertex2d(1300, 350)
    glVertex2d(1300, 50)


    glVertex2f(1300, 350)
    glVertex2f(400, 350)

    glVertex2f(400, 350)
    glVertex2f(400,50)

    glEnd()
    # Draw Door 

    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex2f(700, 50)
    glVertex2f(700, 200)

    glVertex2f(700,200)
    glVertex2f(850,200)
    
    glVertex2f(850,200)
    glVertex2f(850, 50)

    glEnd()

    #Draw Door knob
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(820,130) 
    glEnd()

    # Draw Window
    glLineWidth(4)
    glBegin(GL_LINES)

    glVertex2f(1000, 150)
    glVertex2f(1200, 150)

    glVertex2f(1200, 150)
    glVertex2f(1200, 270)

    glVertex2f(1200, 270)
    glVertex2f(1000, 270)

    glVertex2f(1000, 270)
    glVertex2f(1000, 150)

    glEnd()

    glLineWidth(3)
    glBegin(GL_LINES)

    glVertex2f(1000, 210)
    glVertex2f(1200, 210)

    glVertex2f(1100, 150)
    glVertex2f(1100, 270)

    glEnd()

    # Draw RoofTop
    glLineWidth(10)
    glBegin(GL_LINES)

    glVertex2f(370, 350)
    glVertex2f(850, 500)

    glVertex2f(850, 500)
    glVertex2f(1330, 350)

    glVertex2f(370,350)
    glVertex2f(1330, 350)


    glEnd()


def drawEmptyArea():
    glBegin(GL_TRIANGLES)
    glVertex2f(850, 500)
    glVertex2f(370, 350)
    glVertex2f(1330, 350)
    glEnd()

    # set dynamic color
    glColor3f(1-color_offset,1-color_offset,1-color_offset)
    glBegin(GL_TRIANGLES)
    glVertex2f(405,350)
    glVertex2f(1300, 350)
    glVertex2f(405, 300)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(1295,350)
    glVertex2f(1295, 300)
    glVertex2f(400, 300)
    glEnd()

    # set dynamic color
    


def drawRain():
    global rain_offset
    glColor3f(1-color_offset,1-color_offset ,1-color_offset )
    glLineWidth(5)
    glBegin(GL_LINES)
    for x, y in raindrops:
        glVertex2f(x, y)
        glVertex2f(x + rain_offset, y - 20)  # Simulating raindrop falling
    glEnd()

def continueRain():
    for i in range(len(raindrops)):
        time.sleep(0.000000000000000000000000000001)
        y = raindrops[i][1] - 1
        if y <= 340:
            y = 1200
        raindrops[i] = (raindrops[i][0], y )

def iterate():
    glViewport(0, 0, 1000, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1500, 0.0, 700, 0.0, 1.0)
    # glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global color_offset
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glClearColor(color_offset,color_offset,color_offset,color_offset)
    glColor3f(1-color_offset,1-color_offset ,1-color_offset )
    drawHouse()
    drawEmptyArea()
    drawRain()
    
    glutSwapBuffers()


def idle():
    continueRain()
    glutPostRedisplay()


def ListenSpecialKeys(key, x, y):
    global rain_offset
    global color_offset
    if key == GLUT_KEY_UP:
        print('Up arrow pressed')
        # Dark Theme
        if color_offset < 1:
            color_offset += 0.1
    
    if key == GLUT_KEY_DOWN:
        print('Down arrow pressed')
        # White Theme
        if color_offset > 0:
            color_offset -= 0.1

    if key == GLUT_KEY_LEFT:
        print('Left arrow pressed')
        # Bend rain drops to left
        rain_offset += 1

    if key == GLUT_KEY_RIGHT:
        print('Right arrow pressed')
        # Bend rain drops to right
        rain_offset -= 1

    glutPostRedisplay()




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1500, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(idle)
glutSpecialFunc(ListenSpecialKeys)

glutMainLoop()
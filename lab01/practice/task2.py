from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
print('This is task2')

W_Width, W_Height = 1500, 700
ballx = bally = 0
speed = 0.01
speed2 = 0
ball_size = 2
create_new = False
points = []
diagonal = [0,1,10,11]
colors = []
flag = True 

def generatePoint():
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)

    return x,y

def draw_points(x, y):
    global points
    print('drawing point')
    color = (random.random(), random.random(), random.random())
    d = random.randint(0,3)
    points.append([x,y, color,d])




def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b


def keyboardListener(key, x, y):
    global speed , speed2
    if key==b' ' and speed != 0:
        print('Space bar button clicked')
        speed2 = speed
        speed = 0
        
    elif key == b' ' and speed == 0:
        speed = speed2


    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed
    
    if key==GLUT_KEY_UP:
        speed *= 2
        print("Speed Increased")
    if key== GLUT_KEY_DOWN:		
        speed /= 2
        print("Speed Decreased")
    glutPostRedisplay()

a = 0
def ReAppearPoints():
    global a
    for i in range(len(points)):
        point = points[i]
        x, y , color, d = point 
        color = colors[i]
        points[i] = [x,y,color,d]
    a = 0


def mouseListener(button, state, x, y):	
    global a 
    global ballx, bally, points, colors
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            # Create blink effect
            if a == 0:
                for i in range(len(points)):
                    point = points[i]
                    x, y , color, d = point 
                    colors.append(color)
                    color = (0,0,0)
                    points[i] = [x,y,color,d]
                a = 1
                display()
                time.sleep(0.7)
                ReAppearPoints()
                display()

            # else:
            #     for i in range(len(points)):
            #         point = points[i]
            #         x, y , color, d = point 
            #         color = colors[i]
            #         points[i] = [x,y,color,d]
            #     a = 0



    if button==GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        x, y = generatePoint()
        draw_points(x, y)
        print('Right mouse button pressed!')
    glutPostRedisplay()

            
    


def animate():
    global points

    
    global ballx, bally,speed
    ballx=(ballx+speed)%180
    bally=(bally+speed)%180
    for i in range(len(points)):
        x, y , color, d = points[i] 
        if d == 0:
            x = (x + speed) % 1500
            y = (y + speed) % 700 
        elif d == 1:
            x = (x + speed) % 1500
            y = (y - speed) % 700
        elif d == 2:
            x = (x - speed) % 1500
            y = (y + speed) % 700
        else:
            x = (x - speed) % 1500
            y = (y - speed) % 700
        points[i] = [x, y , color, d]

    glutPostRedisplay()


def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()

    gluPerspective(104,	1,	1,	1000.0)


def display():
    global points
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    iterate()

    glMatrixMode(GL_MODELVIEW)

    for point in points:
        glPointSize(10)
        glBegin(GL_POINTS)
        x , y, color, d = point 
        glColor3f(color[0], color[1], color[2])
        glVertex2f(x, y)
        glEnd()

    glutSwapBuffers()

def iterate():
    glViewport(0, 0, 1000, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1500, 0.0, 700, 0.0, 1.0)
    # glOrtho(-1, 1, -1, 1, -1, 1) 
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

    
glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"This is task2 of lab01")
init()

glutDisplayFunc(display)	
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()
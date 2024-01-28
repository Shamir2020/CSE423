import midpoint_line
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import midpoint_circle


# NAME - SHAMIR ROY
# ID - 20241015
# Sec - 08
# Course - CSE423

PlayerOffset = 5
dropOffset = 0

playerLeft = -16
playerOffset = 0
left = 0
score = 0

gameOver = False
count = 0
pause = False

d = [0 , 0]
L = [0, 0]
R = [0, 0]

a , b , c = 0 , 0 , 0 

speed = 0

o = -180
l = 0
backgroundPoints =  [(random.uniform(-300, 300), random.uniform(-300, 300)) for _ in range(200)]
fire1 = [(l,o)]
fire2 = [(l,o)]
fire3 = [(l,o)]
fireOffset = 2
def generateRandomC():
    return random.choices([0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])[0]


def increaseSpeed():
    global speed 
    speed += 1

def generateRandomHorizontal():
    global left
    left = random.randint(-94,94)
    

def generateRandomColor():
    global a, b, c
    a = random.random()
    b = random.random()
    c = random.random()

def drawLine(cordinates, width):
    glPointSize(width)
    

    glBegin(GL_POINTS)
    for x,y in cordinates:
        glVertex2f(x, y)  # Coordinates of the point
        
    glEnd()


def drawControlsBtns():
    global pause
    # Draw restart button 
    glColor3f(0, 0.8667, 1)
    topLeft = midpoint_line.MidPointLineDrawing(-95,280,-85,290)
    drawLine(topLeft, 3)
    bottomLeft = midpoint_line.MidPointLineDrawing(-95, 280, -85, 270)
    drawLine(bottomLeft,3)
    middleLine = midpoint_line.MidPointLineDrawing(-95,280,-80,280)
    drawLine(middleLine, 3)

    # Draw Pause button 
    glColor3f(1, 0.65098,0)
    if pause:
        topLeft = midpoint_line.MidPointLineDrawing(-5,282.5,3,294)
        drawLine(topLeft,3)
        bottomLeft = midpoint_line.MidPointLineDrawing(-5,282.5,3,270)
        drawLine(bottomLeft,3)
        right = midpoint_line.MidPointLineDrawing(3,270,3,294)
        drawLine(right,3)
    else:
        pauseLeft = midpoint_line.MidPointLineDrawing(-3,295,-3,270)
        drawLine(pauseLeft, 3)
        pauseRight = midpoint_line.MidPointLineDrawing(3,295,3,270)
        drawLine(pauseRight, 3)

    #Draw close button 
    glColor3f(1,0,0)
    closeLeft = midpoint_line.MidPointLineDrawing(85, 295, 95, 270)
    drawLine(closeLeft, 3)
    closeRight = midpoint_line.MidPointLineDrawing(85, 270, 95,295)
    drawLine(closeRight, 3)


def drawBackground():
    global backgroundPoints
    glColor3f(0.7,0.7,0.7)
    glPointSize(2)
    glBegin(GL_POINTS)
    for x,y in backgroundPoints:
        glVertex2f(x, y)  
        
    glEnd()


def MoveFire1Points():
    global l,o, fire1

    for i in range(len(fire1)):
        fire1[i] = (fire1[i][0],fire1[i][1]+10)
       
    fire2 = []
    i = 0
    while True:
        if i == len(fire1):
            break
        if fire1[i][1] < 300:
            fire2.append(fire1[i])
        i += 1

    fire1 = fire2.copy()

def Player1Fire():
    global o, l, fire1, fireOffset


    if len(fire1) < 300:
        fire1.append((l,o))
    else:
        fire1 = [(l,o)]

    glPointSize(5)

    glBegin(GL_POINTS)
    for x,y in fire1:
        glVertex2f(x,y)
        
    glEnd()

    MoveFire1Points()

def MoveFire2Points():
    global l,o, fire2

    for i in range(len(fire2)):
        fire2[i] = (fire2[i][0],fire2[i][1]+10)
       
    fire = []
    i = 0
    while True:
        if i == len(fire2):
            break
        if fire2[i][1] < 300:
            fire.append(fire2[i])
        i += 1

    fire2 = fire.copy()

def MoveFire3Points():
    global l,o, fire3

    for i in range(len(fire3)):
        fire3[i] = (fire3[i][0],fire3[i][1]+15)
       
    fire = []
    i = 0
    while True:
        if i == len(fire3):
            break
        if fire3[i][1] < 300:
            fire.append(fire3[i])
        i += 1

    fire3 = fire.copy()

def Player2Fire():
    global o, l, fire2, fireOffset

      
    if len(fire2) < 300:
        fire2.append((l,o))
    else:
        fire2 = [(l,o)]

    glPointSize(8)

    glBegin(GL_POINTS)
    for x,y in fire2:
        glVertex2f(x,y)
        
    glEnd()

    MoveFire2Points()

def Player3Fire():
    global o, l, fire3, fireOffset

      
    if len(fire3) < 300:
        fire3.append((l,o))
    else:
        fire3 = [(l,o)]

    glPointSize(10)

    glBegin(GL_POINTS)
    for x,y in fire3:
        glVertex2f(x,y)
        
    glEnd()

    MoveFire3Points()

       

def Player1():
    global o, l
    #Drawing player 1
    # Drawing mouth
    glColor3f(1,1,1)
    

    mtopRight = midpoint_line.MidPointLineDrawing(0+l,0+o,20+l,-20+o)
    drawLine(mtopRight,3)
    mtopLeft = midpoint_line.MidPointLineDrawing(0+l,0+o,-20+l,-20+o)
    drawLine(mtopLeft,3)

    mbottomRight = midpoint_line.MidPointLineDrawing(20+l,-20+o,0+l,-40+o)
    drawLine(mbottomRight,3)

    mbottomLeft = midpoint_line.MidPointLineDrawing(-20+l,-20+o,0+l,-40+o)
    drawLine(mbottomLeft,3)

    #Drawing sides 
    leftSide = midpoint_line.MidPointLineDrawing(-20+l, -20+o, -20+l,-60+o)
    drawLine(leftSide,3)

    rightSide = midpoint_line.MidPointLineDrawing(20+l,-20+o,20+l,-60+o)
    drawLine(rightSide,3)

    middleSide = midpoint_line.MidPointLineDrawing(0+l,-40+o,0+l, -80+o)
    drawLine(middleSide,3)

    #Drawing Tail 
    tailLeft = midpoint_line.MidPointLineDrawing(-20+l,-60+o,0+l,-80+o)
    drawLine(tailLeft,3)

    tailRight = midpoint_line.MidPointLineDrawing(20+l,-60+o,0+l,-80+o)
    drawLine(tailRight,3)

    #Drawing Wings 
    topLeftWing = midpoint_line.MidPointLineDrawing(-20+l,-20+o,-50+l,-50+o)
    drawLine(topLeftWing,3)
    
    topRightWing = midpoint_line.MidPointLineDrawing(20+l,-20+o,50+l,-50+o)
    drawLine(topRightWing,3)

    bottomLeftWing = midpoint_line.MidPointLineDrawing(-20+l,-60+o,-60+l,-100+o)
    drawLine(bottomLeftWing,3)

    bottomRightWing = midpoint_line.MidPointLineDrawing(20+l,-60+o,60+l,-100+o)

    drawLine(bottomRightWing,3)

    Player1Fire()

def Player2():
    global o,l
    glColor3f(1,1,0)
    
    
    mtopRight = midpoint_line.MidPointLineDrawing(0+l,0+o,20+l,-20+o)
    drawLine(mtopRight,3)
    mtopLeft = midpoint_line.MidPointLineDrawing(0+l,0+o,-20+l,-20+o)
    drawLine(mtopLeft,3)

    mbottomRight = midpoint_line.MidPointLineDrawing(20+l,-20+o,0+l,-40+o)
    drawLine(mbottomRight,3)

    mbottomLeft = midpoint_line.MidPointLineDrawing(-20+l,-20+o,0+l,-40+o)
    drawLine(mbottomLeft,3)

    #Drawing sides 
    leftSide = midpoint_line.MidPointLineDrawing(-20+l, -20+o, -20+l,-60+o)
    drawLine(leftSide,3)

    rightSide = midpoint_line.MidPointLineDrawing(20+l,-20+o,20+l,-60+o)
    drawLine(rightSide,3)

    middleSide = midpoint_line.MidPointLineDrawing(0+l,-40+o,0+l, -80+o)
    drawLine(middleSide,3)

    #Drawing Tail 
    tailLeft = midpoint_line.MidPointLineDrawing(-20+l,-60+o,0+l,-80+o)
    drawLine(tailLeft,3)

    tailRight = midpoint_line.MidPointLineDrawing(20+l,-60+o,0+l,-80+o)
    drawLine(tailRight,3)

    #Drawing Wings 
    topLeftWing = midpoint_line.MidPointLineDrawing(-20+l,-20+o,-50+l,-50+o)
    drawLine(topLeftWing,3)

    bottomTopLeftWing = midpoint_line.MidPointLineDrawing(-20+l,-20+o, -40+l, -60+o)
    drawLine(bottomTopLeftWing,3)
    
    leftWingJoin = midpoint_line.MidPointLineDrawing(-50+l,-50+o,-40+l,-60+o)
    drawLine(leftWingJoin,3)

    topRightWing = midpoint_line.MidPointLineDrawing(20+l,-20+o,50+l,-50+o)
    drawLine(topRightWing,3)

    bottomTopRightWing = midpoint_line.MidPointLineDrawing(20+l,-20+o,40+l,-60+o)
    drawLine(bottomTopRightWing,3)

    rightWingJoin = midpoint_line.MidPointLineDrawing(50+l,-50+o,40+l,-60+o)

    drawLine(rightWingJoin,3)

    bottomLeftWing = midpoint_line.MidPointLineDrawing(-20+l,-60+o,-60+l,-100+o)
    drawLine(bottomLeftWing,3)

    bottomRightWing = midpoint_line.MidPointLineDrawing(20+l,-60+o,60+l,-100+o)

    drawLine(bottomRightWing,3)

    Player2Fire()

def Player3():
    global o,l

    glColor3f(0,1,1)
    
    mtopRight = midpoint_line.MidPointLineDrawing(0+l,0+o,20+l,-20+o)
    drawLine(mtopRight,3)
    mtopLeft = midpoint_line.MidPointLineDrawing(0+l,0+o,-20+l,-20+o)
    drawLine(mtopLeft,3)

    mbottomRight = midpoint_line.MidPointLineDrawing(20+l,-20+o,0+l,-40+o)
    drawLine(mbottomRight,3)

    mbottomLeft = midpoint_line.MidPointLineDrawing(-20+l,-20+o,0+l,-40+o)
    drawLine(mbottomLeft,3)

    #Drawing sides 
    leftSide = midpoint_line.MidPointLineDrawing(-20+l, -20+o, -20+l,-60+o)
    drawLine(leftSide,3)

    rightSide = midpoint_line.MidPointLineDrawing(20+l,-20+o,20+l,-60+o)
    drawLine(rightSide,3)

    middleSide = midpoint_line.MidPointLineDrawing(0+l,-40+o,0+l, -80+o)
    drawLine(middleSide,3)

    #Drawing Tail 
    tailLeft = midpoint_line.MidPointLineDrawing(-20+l,-60+o,0+l,-80+o)
    drawLine(tailLeft,3)

    tailRight = midpoint_line.MidPointLineDrawing(20+l,-60+o,0+l,-80+o)
    drawLine(tailRight,3)

    #Drawing Wings 
    topLeftWing = midpoint_line.MidPointLineDrawing(-20+l,-20+o,-50+l,-50+o)
    drawLine(topLeftWing,3)

    bottomTopLeftWing = midpoint_line.MidPointLineDrawing(-20+l,-20+o, -40+l, -60+o)
    drawLine(bottomTopLeftWing,3)
    
    leftWingJoin = midpoint_line.MidPointLineDrawing(-50+l,-50+o,-40+l,-60+o)
    drawLine(leftWingJoin,3)

    topRightWing = midpoint_line.MidPointLineDrawing(20+l,-20+o,50+l,-50+o)
    drawLine(topRightWing,3)

    bottomTopRightWing = midpoint_line.MidPointLineDrawing(20+l,-20+o,40+l,-60+o)
    drawLine(bottomTopRightWing,3)

    rightWingJoin = midpoint_line.MidPointLineDrawing(50+l,-50+o,40+l,-60+o)

    drawLine(rightWingJoin,3)

    bottomLeftWing = midpoint_line.MidPointLineDrawing(-20+l,-60+o,-60+l,-100+o)
    drawLine(bottomLeftWing,3)

    bottomBottomLeftWing = midpoint_line.MidPointLineDrawing(-20+l,-60+o,-50+l,-110+o)
    drawLine(bottomBottomLeftWing,3)


    bottomLeftJoin = midpoint_line.MidPointLineDrawing(-60+l,-100+o,-50+l,-110+o)
    drawLine(bottomLeftJoin,3)

    bottomRightWing = midpoint_line.MidPointLineDrawing(20+l,-60+o,60+l,-100+o)

    drawLine(bottomRightWing,3)

    bottomBottomRightWing = midpoint_line.MidPointLineDrawing(20+l,-60+o,50+l,-110+o)
    drawLine(bottomBottomRightWing,3)

    bottomRightJoin = midpoint_line.MidPointLineDrawing(60+l,-100+o,50+l,-110+o)
    drawLine(bottomRightJoin,3)

    Player3Fire()

def drawPlayer():
    global playerOffset, L, R, gameOver, score
    #draw the player 

    drawBackground()
    if score <= 3000:
        Player1()
    elif score <= 6000:
        Player2()
    else:
        Player3()


def hasCollided():
    global d, L, R, score, dropOffset, speed
    if d[1] <= L[1]:
        if d[0] >= L[0] and d[0] <= R[0]:
            score += 1
            print(f'Score: {score}')
            dropOffset = 0
            speed += 0.01


def drawIdleEnemy():
    global dropOffset, left, gameOver, score, count, pause,a,b,c, d, L , R

    pass 
   

def IdleDisplay():
    drawPlayer()
    # drawIdleEnemy()
    glutSwapBuffers()
    glClear(GL_COLOR_BUFFER_BIT)
    # drawPlayer()
    drawIdleEnemy()
    drawControlsBtns()
    hasCollided()
    

def drawEnemy():
    global left, dropOffset

    pass



def iterate():
    glViewport(0, 0, 500, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300, 300, -300, 300, 0.0, 1)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    drawControlsBtns()
    drawBackground()
    # glColor3f(1,0,0)
    drawEnemy()
    drawPlayer()
    
    glutSwapBuffers()

def mouseListener(button, state, x, y):
    global pause, dropOffset, score, gameOver, speed, count
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            # Check for which button was clicked
            # print('Mouse left btn clicked!')
            # print(f'Mouse left btn co ordinate - ( {x},{y} )')
           pass 


def ListenSpecialKeys(key, x, y):
    global playerOffset, pause, gameOver, o, l


    if key == GLUT_KEY_LEFT:
        # print('Left arrow pressed')
        # Bend rain drops to left
        if l > -260:
            l -= 15
    if key == GLUT_KEY_RIGHT:
        # print('Right arrow pressed')
        # Bend rain drops to right
        if l < 260:
            l += 15

    if key == GLUT_KEY_UP:
        if o < 100:
            o += 15
    if key == GLUT_KEY_DOWN:
        if o > -200:
            o -= 15

    glutPostRedisplay()




glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 800)

glutCreateWindow(b"Ball Catcher Game")

glutDisplayFunc(showScreen)
if gameOver == False:
    glutIdleFunc(IdleDisplay)
else:
    print('Game Over!!')
    print(f'Score is {score}')

glutSpecialFunc(ListenSpecialKeys)
glutMouseFunc(mouseListener)

glutMainLoop()

glutMainLoop()
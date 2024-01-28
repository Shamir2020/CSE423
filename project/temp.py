import midpoint_line
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

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

    

def drawPlayer():
    global playerOffset, L, R, gameOver
    #draw the player 
    if gameOver:
        glColor3f(1,0,0)
    else:
        glColor3f(1,1,1)

    coordinatesUp = midpoint_line.MidPointLineDrawing(-20+playerOffset,-260,20+playerOffset,-260)
    drawLine(coordinatesUp, 4)
    coordinatesDown = midpoint_line.MidPointLineDrawing(-16+playerOffset,-280,16+playerOffset,-280)
    drawLine(coordinatesDown, 4)
    cordinatesLeft = midpoint_line.MidPointLineDrawing(-16+playerOffset,-280,-20+playerOffset,-260)
    drawLine(cordinatesLeft, 4)
    cordinatesRight = midpoint_line.MidPointLineDrawing(16+playerOffset,-280,20+playerOffset,-260)
    drawLine(cordinatesRight, 4)

    L = [-20 + playerOffset, -260]
    R = [20 + playerOffset, -260]


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


    if 290 - dropOffset == 290 or 290 - dropOffset == -288:
        # print('Block 1 true')
        generateRandomColor()
        generateRandomHorizontal()
        
    elif 290-dropOffset <= -290:
        # print(f'Block 2 true. dropOffset = {dropOffset}')
        dropOffset = 0
        
        generateRandomHorizontal()
        generateRandomColor()
        
        gameOver = True


    if gameOver:
        if count == 0:
            print(f'Game Over! Score: {score}')
            
            count += 1
    else:
        glColor3f(a,b,c)
        bottomRight = midpoint_line.MidPointLineDrawing(left,260-dropOffset,left+5,275-dropOffset)
        drawLine(bottomRight, 3)

        topRight = midpoint_line.MidPointLineDrawing(left+5,275-dropOffset,left,290-dropOffset)
        drawLine(topRight, 3)

        topLeft = midpoint_line.MidPointLineDrawing(left,290-dropOffset,left-5,275-dropOffset)
        drawLine(topLeft, 3)
    
        bottomLeft = midpoint_line.MidPointLineDrawing(left-5,275-dropOffset,left,260-dropOffset)
        drawLine(bottomLeft, 3)
        
        d = [left, 260-dropOffset]

        if pause:
            dropOffset = dropOffset
        else:
            dropOffset += 0.1 + speed

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

    #Draw the enemy
    if 290 - dropOffset == 290:
        generateRandomHorizontal()
    elif 290-dropOffset <= -290:
        dropOffset = 0
    
    glColor3f(generateRandomC(),generateRandomC(),generateRandomC())

    bottomRight = midpoint_line.MidPointLineDrawing(left,260-dropOffset,left+5,275-dropOffset)
    drawLine(bottomRight, 3)

    topRight = midpoint_line.MidPointLineDrawing(left+5,275-dropOffset,left,290-dropOffset)
    drawLine(topRight, 3)

    topLeft = midpoint_line.MidPointLineDrawing(left,290-dropOffset,left-5,275-dropOffset)
    drawLine(topLeft, 3)
    
    bottomLeft = midpoint_line.MidPointLineDrawing(left-5,275-dropOffset,left,260-dropOffset)
    drawLine(bottomLeft, 3)

    

# def drawAxix():
#     glBegin(GL_LINES)
#     glVertex2f(-700,0)
#     glVertex2f(700,0)
    
#     glVertex2f(0,-350)
#     glVertex2f(0,350)

#     glEnd()

#     glBegin(GL_POINTS)
    
#     glVertex2f(0, 0) 

#     glVertex2f(99,10)
#     glVertex2f(-99, 10)

#     glVertex2f(10,300)
#     glVertex2f(-10, -300)   
#     glEnd()

def iterate():
    glViewport(0, 0, 500, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-100, 100, -300, 300, 0.0, 1)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    drawControlsBtns()
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
            if x >= 241 and x <= 257:
                if y >= 5 and y <= 39:
                    # print('Pause btn clicked!')
                    if pause == False:
                        pause = True
                    else:
                        pause = False 
            
            elif x >= 461 and x <= 487:
                if y >= 7 and y <= 39:
                    print(f'Goodbye! Score = {score}')
                    glutLeaveMainLoop()

            elif x >= 13 and x <= 50:
                if y >= 9 and y <= 39:
                    # print('Restart btn clicked!')
                    print('Starting Over!')
                    score = 0
                    pause = False
                    dropOffset = 0
                    gameOver = False
                    speed = 0
                    count = 0


def ListenSpecialKeys(key, x, y):
    global playerOffset, pause, gameOver


    if key == GLUT_KEY_LEFT:
        # print('Left arrow pressed')
        # Bend rain drops to left
        if pause or gameOver:
            pass 
        else:
            if playerOffset > -80:
                playerOffset -= 10
            else:
                playerOffset = playerOffset

    if key == GLUT_KEY_RIGHT:
        # print('Right arrow pressed')
        # Bend rain drops to right
        if pause or gameOver:
            pass 
        else:
            if playerOffset + 20 < 100:
                playerOffset += 10
            else:
                playerOffset = playerOffset

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




def MidPointLineDrawing(x1,y1, x2,y2):
    if x1 > x2:
        x1 , x2 = x2, x1 
        y1, y2 = y2, y1 
    
    zone = FindZone(x1, y1, x2,y2)
    
    
    x1_, y1_ = convertZoneToZero(x1, y1, zone)
    x2_ , y2_ = convertZoneToZero(x2, y2, zone)
    
    # print(x1_,y1_)
    # print(x2_,y2_)
    dx = x2_ - x1_ 
    dy = y2_ - y1_

    dstart = 2*dy - dx 
    
    dE = 2 * dy 

    dNE = 2 * (dy - dx)

    CoOrdinates = []

    x = x1_
    y = y1_
    d = dstart

    while x < x2_:

        if d < 0:
            d = d + dE
        else:
            d = d + dNE
            y = y + 1
        x = x + 1

        CoOrdinates.append((x,y))


    mappedCordinates = []
    for x_, y_ in CoOrdinates:
        x , y = convertZoneBack(x_, y_, zone)
        mappedCordinates.append((x,y))
    
    # print(mappedCordinates)
    return mappedCordinates


def FindZone(x1,y1,x2,y2):
    dy = y2 - y1
    dx = x2 - x1 
    import math 
    if abs(dx) > abs(dy):
        if dx >= 0:
            if dy >= 0:
                return 0
            else:
                7
        else:
            if dy >= 0:
                return 3 
            else:
                return 4
    else:
        if dy >= 0:
            if dx >= 0:
                return 1
            else:
                return 2 
        else:
            if dx >= 0:
                return 6
            else:
                return 5

def findZone(x1,y1,x2,y2):
    dy = y2 - y1
    dx = x2 - x1 

    import math 
    try:
        angle = math.atan(dy/dx)
        angle = math.degrees(angle)
    except:
        angle = 90

    

    if angle >= 0:
        if dx > 0 and dy > 0:
            angle = angle
        elif dx < 0 and dy < 0:
            angle = angle + 180 
    else:
        if dx < 0 and dy > 0:
            angle = angle + 180
        elif dx > 0 and dy < 0:
            angle = angle + 360

    
    zone = 0

    if angle >= 0 and angle <= 45:
        zone = 0 
    if angle > 45 and angle < 90:
        zone = 1
    if angle >= 90 and angle <= 135:
        zone = 2 
    if angle > 135 and angle < 180:
        zone = 3 
    if angle >= 180 and angle <= 225:
        zone = 4
    if angle > 225 and angle < 270:
        zone = 5
    if angle >= 270 and angle <= 315:
        zone = 6 
    if angle > 315 and angle < 360:
        zone = 7
    
    return zone

def convertZoneToZero(x,y,zone):
    if zone == 0:
        return x,y
    elif zone == 1:
        return y,x
    elif zone == 2:
        return y,-x
    elif zone == 3:
        return -x,y
    elif zone == 4:
        return -x,-y
    elif zone == 5:
        return -y,-x
    elif zone == 6:
        return -y,x
        # return -y, x
    else:
        return x,-y

def convertZoneBack(x,y,zone):
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
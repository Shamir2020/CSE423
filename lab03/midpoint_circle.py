

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
    


# print(MidpointCircleDrawing(0,0,50))
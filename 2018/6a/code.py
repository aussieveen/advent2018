import sys
import os
import re
import datetime
from string import ascii_letters

map = None

class chronalCoordinates():

    def __init__(self, inputFile):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        self.input = file.read().splitlines()
        file.close()        
        self.coordinateList = {}
        self.coordValueKey = 0

    def run(self):
        largestX = largestY = 0
        for line in self.input:
            coordinates = line.split(", ")
            x = int(coordinates[0]);
            y = int(coordinates[1]);
            self.coordinateList[ascii_letters[self.coordValueKey]] = cCoord(x,y,ascii_letters[self.coordValueKey])
            if (x > largestX):
                largestX = x
            if (y > largestY):
                largestY = y
            self.coordValueKey += 1
        global map        
        map = cMap(largestX + 1,largestY + 1)
        for k,coordObject in self.coordinateList.items():
            map.addMarker(coordObject.x, coordObject.y, coordObject)
        map.explore(self.coordinateList)
        largestCoordSize = 0
        for k,coordObject in self.coordinateList.items():    
            if(coordObject.infinite):
                continue
            if(coordObject.size > largestCoordSize):
                largestCoordSize = coordObject.size
        print (largestCoordSize)        
        return largestCoordSize

class cMap():
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.layout = [['.']*self.height for _ in range(self.width)]

    def getDistance(self,x1,y1,x2,y2):
        return abs(x1-x2)+abs(y1-y2)

    def printCMap(self):
        for y in range(self.height):
            string = ""
            for x in range(self.width):
                if (type(self.layout[x][y])) is str:
                    string += self.layout[x][y]     
                else:
                    string += self.layout[x][y].value   
            print(string)
        print("                                           ")      

    def addMarker(self,x,y,value):
        try: 
            self.layout[x][y] = value
            return True
        except:
            return False

    def explore(self,coordinateList):
        for y in range(self.height):
            for x in range(self.width):
                distance = 10000000;
                point = self.layout[x][y]
                if (point == "."):
                    for k,coordObject in coordinateList.items():
                        coordDistance = self.getDistance(x,y,coordObject.x,coordObject.y)
                        if (coordDistance == distance):
                            value = "+"
                        if (coordDistance < distance):
                            value = coordObject
                            distance = coordDistance
                    self.layout[x][y] = value
                    if (value != "+"):
                        value.increaseSize()
                        if (y == 0 or y == self.height-1 or x==0 or x==self.width-1):
                            value.setInfinite()

    def expandCoordinate(self,x,y,value):
        if (x < 0 or y < 0 ):
            value.infinite = True
            return False
        try:
            newPoint = self.layout[x][y]
        except:
            value.infinite = True
            return False    
        if (newPoint == "."):
            self.layout[x][y] = value
            return True
        if (newPoint == "+"):
            return False    

        if (newPoint.value == value.value):
            return False
        else:
            newPointDistance = self.getDistance(x,y,newPoint.x,newPoint.y)
            valueDistance = self.getDistance(x,y,value.x,value.y)
            if (newPointDistance == valueDistance):
                self.layout[x][y] = "+"
                return False
            if (newPointDistance < valueDistance):
                return False
            if (newPointDistance > valueDistance):
                self.layout[x][y] = value
                return True     
  
class cCoord():
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value = value
        self.infinite = False
        self.size = 1

    def getCoords(self):
        return (self.x,self.y)    

    def getValue(self):
        return self.value

    def setInfinite(self):
        self.infinite = True

    def getInfinite(self):
        return self.infinite

    def increaseSize(self):
        self.size += 1


if __name__ == '__main__':
    # Map command line arguments to function arguments.
    cc = chronalCoordinates(*sys.argv[1:])
    cc.run()

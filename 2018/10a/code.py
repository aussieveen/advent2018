import sys
import os
import re
from string import ascii_uppercase
from collections import deque,defaultdict

class Message():

    def __init__(self, inputFile):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        self.input = file.read().splitlines()
        file.close()

        self.stars = deque()
        for line in self.input:
            m = re.findall("(-*\d+)",line) 
            self.stars.append(Star(int(m[0]),int(m[1]),int(m[2]),int(m[3])))

    def run(self):
        message = False
        i = 0
        prevArea = None
        message = False
        while not message:
            i += 1
            # print (i)
            smallestX = None
            smallestY = None
            largestX = None
            largestY = None

            for star in self.stars:
                star.updatePosition()
                if (smallestX == None or smallestX > star.x):
                    smallestX = star.x
                if (smallestY == None or smallestY > star.y):
                    smallestY = star.y    
                if (largestX == None or largestX < star.x):
                    largestX = star.x
                if (largestY == None or largestY < star.y):
                    largestY = star.y    

            # for star in self.stars:
            #     if (star.connected):
            #         continue
            #     N = star.y - 1
            #     S = star.y + 1
            #     E = star.x + 1
            #     W = star.x - 1
            #     for possibleAdjacentStar in self.stars:
            #         if (((N == possibleAdjacentStar.y or S == possibleAdjacentStar.y) and possibleAdjacentStar.x == star.x) or 
            #             ((E == possibleAdjacentStar.x or W == possibleAdjacentStar.x) and possibleAdjacentStar.y == star.y) or
            #             (E == possibleAdjacentStar.x and N == possibleAdjacentStar.y) or
            #             (E == possibleAdjacentStar.x and S == possibleAdjacentStar.y) or
            #             (W == possibleAdjacentStar.x and N == possibleAdjacentStar.y) or
            #             (W == possibleAdjacentStar.x and S == possibleAdjacentStar.y)):
            #             star.setConnection(True)
            #             possibleAdjacentStar.setConnection(True)

            # for star in self.stars:
            #     if not star.connected:
            #         message = False
            #         break 
            # print(SEx)
            # print(NWx)
            # print(SEy)
            # print(NWy)
            area = (largestX - smallestX) * (largestY - smallestY);
            if (prevArea == None):
                prevArea = area
            if (area > prevArea):
                message = True
                i -= 1
                for star in self.stars:
                    star.reversePosition()

            prevArea = area    

            # if (i % 100 == 0):
            #     print (SEx - NWx)
            #     print (SEy - NWy)
                # self.printStars(NWx,NWy,SEx,SEy)
        self.printStars(smallestX,smallestY,largestX,largestY)
        print(i)       

    def printStars(self,NWx,NWy,SEx,SEy):                
        for y in range(NWy, SEy+1):
            string = ""
            for x in range(NWx, SEx+1):
                isStar = False
                for star in self.stars:
                    if (star.x == x and star.y == y):
                        isStar = True
                        break
                if isStar:        
                    string += "*"            
                else:
                    string += "."            
            print(string)


        # circle = deque([0])

        # for marble in range(1, self.numOfMarbles + 1):
        #     if marble % 23 == 0:
        #         circle.rotate(7)
        #         scores[marble % self.numOfPlayers] += marble + circle.pop()
        #         circle.rotate(-1)
        #     else:
        #         circle.rotate(-1)
        #         circle.append(marble)


class Star():
    def __init__(self,x,y,xVel,yVel):
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
        self.connected = False

    def updatePosition(self):
        self.x += self.xVel
        self.y += self.yVel

    def reversePosition(self):
        self.x -= self.xVel
        self.y -= self.yVel        

    def setConnection(self,value):
        self.connected = value

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    mg = Message(*sys.argv[1:])
    mg.run()

import sys
import os
import re
from string import ascii_uppercase
from collections import deque,defaultdict
import numpy

class PowerGrid():

    def __init__(self, serialNumber):
        self.fuelCells = numpy.zeros((301,301),numpy.int8)
        self.cache = {}
        for x in range(1,301):
            for y in range(1,301):
                rackId = x + 10
                powerLevel = rackId * y
                powerLevel += int(serialNumber)
                powerLevel *= rackId
                powerLevelAsStr = str(powerLevel)
                if(len(powerLevelAsStr) >= 3):
                    hundredDigit = int(powerLevelAsStr[-3])
                else:
                    hundredDigit = 0
                self.fuelCells[y][x] = hundredDigit - 5
                self.setToCache(x,y,1,hundredDigit-5)
        
    def getFuelCellPowerLevel(self,x,y): 
        return self.getFromCache(x,y,1)
                
    def getGridPowerLevel(self,x,y,size):
        sum = self.getFromCache(x,y,size-1)
        for i in range(x,x+size):
            sum+= self.getFromCache(i,y,1)
        for j in range(y,y+size):
            sum+= self.getFromCache(x,j,1)
        sum+=self.getFromCache(x+size-1,y+size-1,1)    
        self.setToCache(x,y,size,sum);
        return sum
    
    def getLargestGridPowerLevel(self):
        highestPowerLevel = 0
        hplx = 0
        hply = 0
        hpls = 0
        for size in range(2,18):
            print(size)
            for x in range(1,301-size):
                for y in range(1,301-size):            
                    gridPowerLevel = self.getGridPowerLevel(x,y,size)
                    if (gridPowerLevel > highestPowerLevel):
                        highestPowerLevel = gridPowerLevel
                        hplx = str(x)
                        hply = str(y)
                        hpls = str(size)
        print (str(hplx) + "," + str(hply) + "," + str(size))
        return str(hplx) + "," + str(hply) + "," + str(size)

    def getFromCache(self,x,y,size):
        return self.cache[self.getCacheString(x,y,size)]
            
    def setToCache(self,x,y,size,value):
        self.cache[self.getCacheString(x,y,size)] = value

    def getCacheString(self,x,y,size):
        return str(x)+","+str(y)+","+str(size)   

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    pg = PowerGrid(*sys.argv[1:])
    pg.getLargestGridPowerLevel()

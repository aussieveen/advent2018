import sys
import os
import re
from string import ascii_uppercase
from collections import deque,defaultdict
import numpy

class PowerGrid():

    def __init__(self, serialNumber):
        self.fuelCells = numpy.zeros((301,301),numpy.int8)
        for x in range(1,301):
            for y in range(1,301):
                rackId = x + 10
                powerLevel = rackId * y
                powerLevel = powerLevel + int(serialNumber)
                powerLevel = powerLevel * rackId
                powerLevelAsStr = str(powerLevel)
                if(len(powerLevelAsStr) >= 3):
                    hundredDigit = int(powerLevelAsStr[-3])
                else:
                    hundredDigit = 0
                self.fuelCells[y][x] = hundredDigit - 5
        
    def getFuelCellPowerLevel(self,x,y): 
        return self.fuelCells[int(y)][int(x)]
                
    def getGridPowerLevel(self,x,y):
        sum = 0
        for i in range(x,x+3):
           for j in range(y,y+3):
               sum+=self.getFuelCellPowerLevel(i,j)
        return sum
    
    def getLargestGridPowerLevel(self):
        highestPowerLevel = 0
        hplx = 0
        hply = 0
        for x in range(1,298):
            for y in range(1,298):            
                gridPowerLevel = self.getGridPowerLevel(x,y)
                if (gridPowerLevel > highestPowerLevel):
                    highestPowerLevel = gridPowerLevel
                    hplx = str(x)
                    hply = str(y)
        print(hplx + "," + hply)
        return hplx + "," + hply
        

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    pg = PowerGrid(*sys.argv[1:])
    pg.getLargestGridPowerLevel()

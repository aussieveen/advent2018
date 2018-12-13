import sys
import os
import re
import datetime


class polymer():

    def __init__(self):
        self.polymerChain = ''

    def loadInput(self, inputFile):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        fileContents = file.read().splitlines()
        file.close()

        self.polymerChain = fileContents[0]
        return self
         

    def findRemoveable(self):
        removeableIndexes = []
        skipNext = False
        for index in range(len(self.polymerChain)):
            if (index == len(self.polymerChain) - 1):
                break
            if (skipNext):
                skipNext = False
                continue
            letterOne = self.polymerChain[index]
            letterTwo = self.polymerChain[index + 1]
            if (letterOne.lower() != letterTwo.lower()):
                continue
            if ((letterOne.isupper() and letterTwo.islower())
                    or (letterOne.islower() and letterTwo.isupper())):
                removeableIndexes.append(index)
                skipNext = True

        return removeableIndexes

    def removeIndex(self,index):
        self.polymerChain = self.polymerChain[:index] + "" + self.polymerChain[index + 2:]

    def runPolymer(self):
        while True:
            removeable = self.findRemoveable()
            if(len(removeable) == 0):
                break
            for index in reversed(removeable):
                self.removeIndex(index)
        print(len(self.polymerChain))
        return len(self.polymerChain)

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    p = polymer()
    p.loadInput(*sys.argv[1:]).runPolymer()

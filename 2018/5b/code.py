import sys
import os
import re
import datetime
from string import ascii_lowercase


class polymer():

    def __init__(self):
        self.polymerChain = ''

    def loadInput(self, inputFile):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        fileContents = file.read().splitlines()
        file.close()

        self.polymerChain = fileContents[0]
        self.originalChain = self.polymerChain
        self.shortestChain = len(self.polymerChain)
        return self

    def removeCharacterFromPolymerChain(self,char):
        self.polymerChain = re.sub("["+char+char.upper()+"]", "",self.originalChain)     

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
        for c in ascii_lowercase:
            print(c)
            self.removeCharacterFromPolymerChain(c)
            while True:
                removeable = self.findRemoveable()
                if(len(removeable) == 0):
                    break
                for index in reversed(removeable):
                    self.removeIndex(index)
            if (len(self.polymerChain) < self.shortestChain):
                self.shortestChain = len(self.polymerChain)
        print(self.shortestChain)        
        return self.shortestChain

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    p = polymer()
    p.loadInput(*sys.argv[1:]).runPolymer()

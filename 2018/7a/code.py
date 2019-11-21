import sys
import os
import re
from string import ascii_uppercase

class InstructionRunner():

    def __init__(self, inputFile):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        self.input = file.read().splitlines()
        self.allNodes = {} 
        file.close()        

    def buildTree(self): 
        for line in self.input:
            nodes = self.regexLine(line)
            parent = nodes[0]
            child = nodes[1]
            if parent not in self.allNodes:
                self.allNodes[parent] = []
            if child not in self.allNodes:
                self.allNodes[child] = []

            self.allNodes[child].append(parent)
                        

    def regexLine(self, line):
        return re.findall(' ([A-Z]{1}) ', line)

    def run(self):
        instructionOrder = []
        while True:
            canDoInstructions = []
            for child,parents in self.allNodes.items():
                if not parents:
                    canDoInstructions.append(child)
            canDoInstructions = sorted(canDoInstructions)
            instructionOrder.append(canDoInstructions[0])
            for child,parents in self.allNodes.items():
                if (canDoInstructions[0] in parents):
                    parents.remove(canDoInstructions[0])
            del self.allNodes[canDoInstructions[0]]
            if not self.allNodes:
                print("".join(instructionOrder))
                return "".join(instructionOrder)        


if __name__ == '__main__':
    # Map command line arguments to function arguments.
    ir = InstructionRunner(*sys.argv[1:])
    ir.buildTree()
    ir.run()

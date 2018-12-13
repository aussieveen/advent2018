import sys
import os
import re
from string import ascii_uppercase

class InstructionRunner():

    def __init__(self, inputFile,workers):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        self.input = file.read().splitlines()
        file.close()        
        
        self.allNodes = {} 
        self.workers = []
        for i in range(int(workers)):
            self.workers.append(None)

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
        runningTime = 0
        instructionOrder = []
        canDoInstructions = []
        workInProgress = []
        while True:
            # find instructions that can be done
            print("WORK REMAINING = " + str(self.allNodes))
            for child,parents in self.allNodes.items():
                if (not parents and child not in canDoInstructions):
                    canDoInstructions.append(child)
            canDoInstructions = sorted(canDoInstructions)
            print("CDI = " + str(canDoInstructions))

            #assign instructions to workers
            for instruction in canDoInstructions:
                for index,worker in enumerate(self.workers):
                    if not worker and instruction not in workInProgress:
                        self.workers[index] = {'instruction':instruction, "time": self.instructionTime(instruction) }
                        workInProgress.append(instruction)
                        break
            print("WORKERS = " + str(self.workers))
            print("workInProgress = " + str(workInProgress))            

            # get task(s) that will finish next
            nextFinishedWorker = []
            nextInstructionFinishedIn = 1000000
            timeAdded = False
            for index,worker in enumerate(self.workers):
                if not worker:
                    continue
                if(int(worker['time']) < nextInstructionFinishedIn):
                    nextFinishedWorker = []
                    nextFinishedWorker.append(index)
                    nextInstructionFinishedIn = worker['time']
                elif(int(worker['time']) == nextInstructionFinishedIn):    
                    nextFinishedWorker.append(index)
            # complete next tasks

            print("NFW = " + str(nextFinishedWorker))
            print("NIFN = " + str(nextInstructionFinishedIn))
            for index,worker in enumerate(self.workers):
                if not worker:
                    continue
                if(index in nextFinishedWorker):
                    #add to running time
                    if not timeAdded:
                        runningTime += nextInstructionFinishedIn
                        timeAdded = True
                    self.workers[index] = None

                    #remove completed task from instruction list
                    for child,parents in self.allNodes.items():
                        if (worker['instruction'] in parents):
                            parents.remove(worker['instruction'])
                    del self.allNodes[worker['instruction']]
                    #remove completed task from can do instruction list and work in progress list
                    canDoInstructions.remove(worker['instruction'])   
                    workInProgress.remove(worker['instruction'])  
                else:
                    worker['time'] -= nextInstructionFinishedIn
            print("                                                         ")
            if not self.allNodes:
                print(runningTime)
                return runningTime

    def instructionTime(self,instruction):
        return 60 + ascii_uppercase.find(instruction) + 1

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    ir = InstructionRunner(*sys.argv[1:])
    ir.buildTree()
    ir.run()

import sys
import os
import re
from string import ascii_uppercase

class LicenseFile():

    def __init__(self, inputFile):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        self.input = file.read()
        file.close()        
        self.list = self.input.split()

    def run(self):
        node = Node(self.list)
        print(node.sumMetaData())


class Node():
    def __init__(self, list):
        self.numberOfChildren = int(list.pop(0))
        self.numberOfMetaValues = int(list.pop(0))
        self.children = [Node(list) for _ in range(self.numberOfChildren)]
        self.metadata = [int(list.pop(0)) for _ in range(self.numberOfMetaValues)]

    def sumMetaData(self):
        return sum(self.metadata) + sum(child.sumMetaData() for child in self.children )

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    lf = LicenseFile(*sys.argv[1:])
    lf.run()

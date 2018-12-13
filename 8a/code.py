import sys
import os
import re
from string import ascii_uppercase
from anytree import NodeMixin,RenderTree

class LicenseFile():

    def __init__(self, inputFile):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        self.input = file.read()
        file.close()        
        self.sum = 0
        self.list = self.input.split()

    # def extractChildNodes(self):


    # def run(self):


class Node:

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    ir = LicenseFile(*sys.argv[1:])
    ir.run()

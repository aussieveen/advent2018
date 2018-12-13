import sys
import os
import operator

def frequency(inputFile):
	file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
	fileContents = file.read().splitlines()
	file.close();

	ops = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}

	frequency = 0;
	for line in fileContents:
		frequency = ops[line[0]](frequency,int(line[1:])) 
	print(frequency)
	return frequency

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    frequency(*sys.argv[1:])
import sys
import os
import operator

def frequency(inputFile):
	file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
	fileContents = file.read().splitlines()
	file.close();

	ops = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}

	frequency = 0;
	usedFrequencies = [frequency];
	frequencyTwice = False
	while frequencyTwice == False:
		for line in fileContents:
			frequency = ops[line[0]](frequency,int(line[1:]))
			if frequency in usedFrequencies:
				print(frequency)
				return frequency
			else:
				usedFrequencies.append(frequency)
				print(len(usedFrequencies))

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    frequency(*sys.argv[1:])
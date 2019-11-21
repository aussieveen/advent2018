import sys
import os


def checksum(inputFile):
    file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
    fileContents = file.read().splitlines()
    file.close()

    two = 0
    three = 0

    for line in fileContents:
        used = {1:[],2:[],3:[]}
        for char in line:
            newCount = 1
            for key in used.keys():
            	if char in used[key]:
                	newCount = key + 1

            used[newCount].append(char)
            print(used)
            if newCount != 1:
                del used[newCount - 1][used[newCount-1].index(char)]

        if len(used[2]) > 0:
            two = two + 1

        if len(used[3]) > 0:
            three = three + 1

    print(two * three)
    return two * three

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    checksum(*sys.argv[1:])

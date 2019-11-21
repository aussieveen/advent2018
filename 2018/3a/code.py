import sys
import os
import re

def claims(inputFile):
    file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
    fileContents = file.read().splitlines()
    file.close()

    fabricSize = 1001
    fabric = [[0]*fabricSize for _ in range(fabricSize)]
    overLappingClaims = 0;

    for line in fileContents:
        claimDetails = regex(line)
        xStart = int(claimDetails[0]);
        yStart = int(claimDetails[1]);
        w = int(claimDetails[2]);
        h = int(claimDetails[3]);
        for x in range(xStart+1, xStart+1+w):
            for y in range(yStart+1, yStart+1+h):
                fabric[x][y] = fabric[x][y]+1
                if (fabric[x][y] == 2):
                    overLappingClaims= overLappingClaims + 1;

    
    print(overLappingClaims)
    return overLappingClaims

def regex(string):
    matchObj = re.match('.*@ (\d+),(\d+): (\d+)x(\d+)', string, re.M|re.I)
    if matchObj:
        #return [matchObj.group(1),matchObj.group(2),matchObj.group(3),matchObj.group(4)]
        return matchObj.groups()

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    claims(*sys.argv[1:])


# used = {1:[],2:[],3:[]}
#         for char in line:
#             newCount = 1
#             for key in used.keys():
#                 if char in used[key]:
#                     newCount = key + 1

#             used[newCount].append(char)
#             print(used)
#             if newCount != 1:
#                 del used[newCount - 1][used[newCount-1].index(char)]

#         if len(used[2]) > 0:
#             two = two + 1

#         if len(used[3]) > 0:
#             three = three + 1
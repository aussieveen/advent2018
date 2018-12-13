import sys
import os
import re



def claims(inputFile):
    file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
    fileContents = file.read().splitlines()
    file.close()

    fabricSize = 1000
    fabric = [['.']*fabricSize for _ in range(fabricSize)]
    overlapped = False

    cleanList = []
    deadList = []

    for line in fileContents:
        claimDetails = regex(line)
        claim = int(claimDetails[0])
        xStart = int(claimDetails[1]);
        yStart = int(claimDetails[2]);
        w = int(claimDetails[3]);
        h = int(claimDetails[4]);
        cleanList.append(claim)
        print(claim)
        for x in range(yStart, yStart+h):
            for y in range(xStart, xStart+w):
                if fabric[x][y] == '.':
                    fabric[x][y] = claim
                else:
                    if (claim in cleanList):
                        cleanList.remove(claim)
                    if (fabric[x][y] != 'x'):
                        deadList.append(fabric[x][y])   
                        if(fabric[x][y] in cleanList):
                            cleanList.remove(fabric[x][y])
                        fabric[x][y] = 'x'
                    deadList.append(claim)    
 
    print(cleanList[0])
    return cleanList[0]
    
    

def regex(string):
    matchObj = re.match('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', string, re.M|re.I)
    if matchObj:
        #return [matchObj.group(1),matchObj.group(2),matchObj.group(3),matchObj.group(4)]
        return matchObj.groups()

def printFabric(fabric):
    for x in range(len(fabric)):
        string = ""
        for y in range(len(fabric)):
           string+=str(fabric[x][y])
        print(string)

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
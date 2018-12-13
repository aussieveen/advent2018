import sys
import os


def checksum(inputFile):
    file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
    fileContents = file.read().splitlines()
    file.close()

    for index, line in enumerate(fileContents):
        for remainingLines in fileContents[index+1:]:
            matches = []
            for charIndex,char in enumerate(line):
                if (char != remainingLines[charIndex]):
                    matches.append(charIndex)
                    print(matches)
                    if (len(matches) == 2):
                        break
            print(line)
            print(remainingLines)
            print(matches)
            if(len(matches) == 1):
                checksum = line[:(matches[0])] + line[(matches[0]+1):]
                print(checksum)
                return checksum

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    checksum(*sys.argv[1:])

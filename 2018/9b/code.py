import sys
import os
import re
from string import ascii_uppercase
from collections import deque,defaultdict

class MarbleGame():

    def __init__(self, inputFile):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        self.input = file.read()
        file.close()

        m = re.findall("(\d+)",self.input) 
        self.numOfPlayers = int(m[0])
        self.numOfMarbles = int(m[1])
        # for i in range(1,self.numOfPlayers + 1):
        #     self.players[i] = Player()

    def playGame(self):
        # set up initial state of the game
        gameState = deque([0])
        index = 0
        scores = defaultdict(int)
        for marble in range(1,self.numOfMarbles+1):
            if (marble % 23 == 0):
                gameState.rotate(-7)
                scores[marble % self.numOfPlayers] += gameState.pop()+marble
                continue

            gameState.rotate(2)
            gameState.append(marble)    

        # circle = deque([0])

        # for marble in range(1, self.numOfMarbles + 1):
        #     if marble % 23 == 0:
        #         circle.rotate(7)
        #         scores[marble % self.numOfPlayers] += marble + circle.pop()
        #         circle.rotate(-1)
        #     else:
        #         circle.rotate(-1)
        #         circle.append(marble)

        print(max(scores.values()))
        return(max(scores.values()))

# class Player():
#     def __init__(self):
#         self.score = 0

#     def addToScore(self,addValue):
#         self.score += addValue

#     def getScore(self):
#         return self.score

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    mg = MarbleGame(*sys.argv[1:])
    mg.playGame()

import sys
import os
import re
from string import ascii_uppercase

class MarbleGame():

    def __init__(self, inputFile):
        file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
        self.input = file.read()
        file.close()

        m = re.findall("(\d+)",self.input) 
        self.numOfPlayers = int(m[0])
        self.numOfMarbles = int(m[1])
        self.players = {}
        for i in range(1,self.numOfPlayers + 1):
            self.players[i] = Player()

    def playGame(self):
        # set up initial state of the game
        gameState = [0,1]
        index = 1
        player = 1
        for marble in range(2,self.numOfMarbles+1):
            if (player == self.numOfPlayers):
                player = 1
            else:
                player+=1
            if (marble % 23 == 0):
                index -= 7
                self.players[player].addToScore(gameState[index]+marble)
                del(gameState[index])
                continue

            if (index == len(gameState)-1 ):
                index = 1
            else:
                index += 2    
            gameState.insert(index,marble)

        highestScore = 0    
        for id,player in self.players.items():
            if (player.getScore() > highestScore):
                highestScore = player.getScore()
        print(highestScore)
        return(highestScore)

class Player():
    def __init__(self):
        self.score = 0

    def addToScore(self,addValue):
        self.score += addValue

    def getScore(self):
        return self.score

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    mg = MarbleGame(*sys.argv[1:])
    mg.playGame()

import unittest
from code import * 

class Advent(unittest.TestCase):

	def testGames(self):
		# game = MarbleGame('6')
		# self.assertEqual(game.playGame(),32)

		game = MarbleGame('3')
		self.assertEqual(game.playGame(),2764)

		# game = MarbleGame('1')
		# self.assertEqual(game.playGame(),8317)
		
		# game = MarbleGame('5')
		# self.assertEqual(game.playGame(),37305)
		
		# game = MarbleGame('4')
		# self.assertEqual(game.playGame(),54718)
						
		# game = MarbleGame('2')
		# self.assertEqual(game.playGame(),146373)
		
		
		

if __name__ == '__main__':
    unittest.main()
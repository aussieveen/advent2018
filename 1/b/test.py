import unittest
from code import * 

class Advent1a(unittest.TestCase):

	def testFirstCase(self):
		self.assertEqual(frequency('1'), 12)

	def testSecondCase(self):
		self.assertEqual(frequency('2'), 10)

	def testThirdCase(self):
		self.assertEqual(frequency('3'), 5)

	def testFourthCase(self):
		self.assertEqual(frequency('4'), 14)

if __name__ == '__main__':
    unittest.main()
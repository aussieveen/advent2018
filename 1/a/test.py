import unittest
from code import * 

class Advent1a(unittest.TestCase):

	def testFirstCase(self):
		self.assertEqual(frequency('1'), 3)

	def testSecondCase(self):
		self.assertEqual(frequency('2'), 3)

	def testThirdCase(self):
		self.assertEqual(frequency('3'), 0)

	def testFourthCase(self):
		self.assertEqual(frequency('4'), -6)

	def testFourthCase(self):
		self.assertEqual(frequency('5'), 321)

if __name__ == '__main__':
    unittest.main()
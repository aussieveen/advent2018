import unittest
from code import * 

class Advent2a(unittest.TestCase):

	def testDistanceCalculations(self):
		testMap = cMap(10,12)
		self.assertEqual(testMap.getDistance(1,1,2,2), 2);
		self.assertEqual(testMap.getDistance(2,2,1,1), 2);
		self.assertEqual(testMap.getDistance(2,2,2,2), 0);
		self.assertEqual(testMap.getDistance(0,0,3,3), 6);
		self.assertEqual(testMap.getDistance(1,3,3,1), 4);
		self.assertEqual(testMap.getDistance(1,1,8,7), 13);
		


	def testFirstCase(self):
		testCc = chronalCoordinates('1')
		self.assertEqual(testCc.run(),17)

if __name__ == '__main__':
    unittest.main()
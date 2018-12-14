import unittest
from code import * 

class Advent(unittest.TestCase):
		
	def testNodeClass(self):
		node = Node([0, 3, 10, 11, 12])
		self.assertEqual(node.sumMetaData(),33)

		node = Node([0, 1, 99])
		self.assertEqual(node.sumMetaData(),99)

		node = Node([1, 1, 0, 1, 99, 2])
		self.assertEqual(node.sumMetaData(),101)

		node = Node([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
		self.assertEqual(node.sumMetaData(),138)
		
		node = Node([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
		self.assertEqual(node.getRootValue(),66)


if __name__ == '__main__':
    unittest.main()
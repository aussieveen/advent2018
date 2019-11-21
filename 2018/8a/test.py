import unittest
from code import * 

class Advent(unittest.TestCase):

	# def testFullRun(self):
	# 	testLf = LicenseFile('1')
		# testLf.sum = 0
		# testLf.extractChildNodes([0, 1,99,2,1,1,2],1)
		# self.assertEqual(testLf.sum,99)
		# testLf.sum = 0
		# testLf.extractChildNodes([1, 1, 0, 1, 99, 2, 1, 1, 2],1,0)
		# self.assertEqual(testLf.sum,101)
		# testLf.sum = 0
		# testLf.extractChildNodes([0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2],2,0)
		# self.assertEqual(testLf.sum,134,2)
		# testLf.sum = 0
		# testLf.extractChildNodes([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2],1,0)
		# self.assertEqual(testLf.sum,138)


		
		
		# testIr.buildTree()
		# self.assertEqual(testIr.run(),'CABDFE')

	def testNodeClass(self):
		node = Node([0, 3, 10, 11, 12])
		self.assertEqual(node.sumMetaData(),33)

		node = Node([0, 1, 99])
		self.assertEqual(node.sumMetaData(),99)

		node = Node([1, 1, 0, 1, 99, 2])
		self.assertEqual(node.sumMetaData(),101)

		node = Node([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
		self.assertEqual(node.sumMetaData(),138)
		


if __name__ == '__main__':
    unittest.main()
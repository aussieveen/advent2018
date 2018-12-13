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
		nodeclass = NodeClass([0, 3, 10, 11, 12])
		print(nodeclass.children)
		# self.assertEqual(nodeclass.getChildNodeCount(),0)
		# self.assertEqual(nodeclass.getMetadataEntryCount(),3)
		# self.assertEqual(nodeclass.sumMetaData(),33)		

		nodeclass = NodeClass([0, 1, 99])
		print(nodeclass.children)
		# self.assertEqual(nodeclass.getChildNodeCount(),0)
		# self.assertEqual(nodeclass.getMetadataEntryCount(),1)
		# self.assertEqual(nodeclass.sumMetaData(),99)
		nodeclass = NodeClass([1, 1, 0, 1, 99, 2])
		print(nodeclass.children)

		nodeclass = NodeClass([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
		print(nodeclass.children)
		


if __name__ == '__main__':
    unittest.main()
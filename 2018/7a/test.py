import unittest
from code import * 

class Advent(unittest.TestCase):

	def testRegex(self):
		IR = InstructionRunner('1')
		self.assertEqual(IR.regexLine('Step C must be finished before step F can begin.'),['C','F'])
		self.assertEqual(IR.regexLine('Step A must be finished before step B can begin.'),['A','B'])

		IR.buildTree()

	def testFullRun(self):
		testIr = InstructionRunner('1')
		testIr.buildTree()
		self.assertEqual(testIr.run(),'CABDFE')

if __name__ == '__main__':
    unittest.main()
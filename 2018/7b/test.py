import unittest
from code import * 

class Advent(unittest.TestCase):

	def testRegex(self):
		IR = InstructionRunner('1',2)
		self.assertEqual(IR.regexLine('Step C must be finished before step F can begin.'),['C','F'])
		self.assertEqual(IR.regexLine('Step A must be finished before step B can begin.'),['A','B'])

	def testFullRun(self):
		testIr = InstructionRunner('1',2)
		testIr.buildTree()
		self.assertEqual(testIr.run(),15)

if __name__ == '__main__':
    unittest.main()
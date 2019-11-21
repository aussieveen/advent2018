import unittest
from code import * 

class Advent2a(unittest.TestCase):

	# def testRegex(self):
	# 	self.assertEqual(regex('#23 @ 1,3: 4x4'), ('1','3','4','4'));
	# 	self.assertEqual(regex('#2 @ 10,30: 40x40'), ('10','30','40','40'));
	# 	self.assertEqual(regex('#3 @ 100,300: 400x400'), ('100','300','400','400'));

	def testFirstCase(self):
		self.assertEqual(claims('1'), 4)

if __name__ == '__main__':
    unittest.main()
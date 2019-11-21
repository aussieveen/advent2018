import unittest
from code import * 

class Advent(unittest.TestCase):

	def testPoints(self):
		pg = PowerGrid(8)
		self.assertEqual(pg.getFuelCellPowerLevel(3,5),4)
		pg = PowerGrid(57)
		self.assertEqual(pg.getFuelCellPowerLevel(122,79),-5)
		pg = PowerGrid(39)
		self.assertEqual(pg.getFuelCellPowerLevel(217,196),0)
		pg = PowerGrid(71)
		self.assertEqual(pg.getFuelCellPowerLevel(101,153),4)

	# def testGrid(self):
	# 	pg = PowerGrid(18)
	# 	self.assertEqual(pg.getGridPowerLevel(90,269,16),113)	
	# 	pg = PowerGrid(42)
	# 	self.assertEqual(pg.getGridPowerLevel(232,251,12),119)	

	def testHighestPower(self):
		# pg = PowerGrid(18)
		# self.assertEqual(pg.getLargestGridPowerLevel(),"33,45,3")	
		pg = PowerGrid(18)
		self.assertEqual(pg.getLargestGridPowerLevel(),"90,269,16")	
		pg = PowerGrid(42)
		self.assertEqual(pg.getLargestGridPowerLevel(),"232,251,12")		

if __name__ == '__main__':
    unittest.main()
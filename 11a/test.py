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

	def testGrid(self):
		pg = PowerGrid(18)
		self.assertEqual(pg.getGridPowerLevel(33,45),29)	
		pg = PowerGrid(42)
		self.assertEqual(pg.getGridPowerLevel(21,61),30)	

	def testHighestPower(self):
		pg = PowerGrid(18)
		self.assertEqual(pg.getLargestGridPowerLevel(),"33,45")	
		pg = PowerGrid(42)
		self.assertEqual(pg.getLargestGridPowerLevel(),"21,61")		

if __name__ == '__main__':
    unittest.main()
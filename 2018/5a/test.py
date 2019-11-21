import unittest
from code import * 

class Advent2a(unittest.TestCase):

	# def testRegex(self):
		# self.assertEqual(eventObject('[1518-04-14 00:00] Guard #3121 begins shift').dateTime, '1518-04-14 00:00');
		# self.assertEqual(getHour('[1518-04-14 00:00] Guard #3121 begins shift'), '00');
		# self.assertEqual(getMin('[1518-04-14 00:00] Guard #3121 begins shift'), '00');
		# self.assertEqual(getAction('[1518-04-14 00:00] Guard #3121 begins shift'), 'begins');
		# self.assertEqual(getGuard('[1518-04-14 00:00] Guard #3121 begins shift'), '3121');
		# self.assertEqual(getGuard('[1518-04-14 00:00] Guard #99 begins shift'), '99');
		# self.assertEqual(getAction('[1518-11-04 00:36] falls asleep'), 'asleep');
		# self.assertEqual(getAction('[1518-11-04 00:46] wakes up'), 'wakes');
		# self.assertEqual(getGuard('[1518-11-04 00:36] falls asleep'), False);
		# self.assertEqual(getGuard('[1518-11-04 00:46] wakes up'), False);


	def testFirstCase(self):
		testPolymer = polymer()
		testPolymer.loadInput('1')
		self.assertEqual(testPolymer.runPolymer(),'dabCBAcaDA')

if __name__ == '__main__':
    unittest.main()
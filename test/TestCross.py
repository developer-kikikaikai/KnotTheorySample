# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../') 
from Cross import Cross

class TestCross(unittest.TestCase):

	def test_Cross(self):
		#test points
		cross=Cross([0,0])
		self.assertEqual(cross.get_point(), [0,0])

		#test slide
		slide=[1,2]
		cross.slide_point(slide)
		self.assertEqual(cross.get_point(), slide)

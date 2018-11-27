# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../') 
from Arc import Arc
from KnotDefinition import KnotDef

class TestNodes(unittest.TestCase):

	def inittest(self):
		#test points
		points_param=[[0,0], [0,5], [5,5], [5,0]]
		points_init=[[0,0], [0,5], [5,5], [5,0]]
		points=[points_init]
		points.append([ [points[0][0], points[0][1]], [points[0][1], points[0][2]], [points[0][2], points[0][3]] ])
		#test initialize
		arc = Arc(points_param)
		self.assertEqual(arc.get_points(), points[1])

		#test slide
		slide=[1,2]
		slide_points=[]
		for point in points_init:
			point[0]+=slide[0]
			point[1]+=slide[1]

		arc.slide_points(slide)
		self.assertEqual(arc.get_points(), points[1])

	def slide_x_and_y_operand_eq_test(self):
		points_init=[[0,0], [0,5], [5,5], [5,0]]
		points=[points_init]
		points.append([ [points[0][0], points[0][1]], [points[0][1], points[0][2]], [points[0][2], points[0][3]] ])
		arc = Arc(points_init)

		slide_x=5
		arc.slide_x(KnotDef.OPERAND_EQUAL, points[0][2][0], slide_x)
		points_init[2][0] += slide_x
		points_init[3][0] += slide_x
		self.assertEqual(arc.get_points(), points[1])

		slide_y=3
		arc.slide_y(KnotDef.OPERAND_EQUAL, points[0][0][1], slide_y)
		points_init[0][1] += slide_y
		points_init[3][1] += slide_y
		self.assertEqual(arc.get_points(), points[1])

	def slide_x_and_y_operand_lt_test(self):
		points_init=[[0,0], [0,5], [5,5], [5,0]]
		points=[points_init]
		points.append([ [points[0][0], points[0][1]], [points[0][1], points[0][2]], [points[0][2], points[0][3]] ])
		arc = Arc(points_init)

		slide_x=5
		point_x=3
		arc.slide_x(KnotDef.OPERAND_LESS_THAN, point_x, slide_x)
		points_init[0][0] += slide_x
		points_init[1][0] += slide_x
		self.assertEqual(arc.get_points(), points[1])

		slide_y=3
		point_y=10
		arc.slide_y(KnotDef.OPERAND_LESS_THAN, point_y, slide_y)
		points_init[3][1] += slide_y
		points_init[2][1] += slide_y
		points_init[1][1] += slide_y
		points_init[0][1] += slide_y
		self.assertEqual(arc.get_points(), points[1])
		point_y=-1
		arc.slide_y(KnotDef.OPERAND_LESS_THAN, point_y, slide_y)
		self.assertEqual(arc.get_points(), points[1])

	def slide_x_and_y_operand_gt_test(self):
		points_init=[[0,0], [0,5], [5,5], [5,0]]
		points=[points_init]
		points.append([ [points[0][0], points[0][1]], [points[0][1], points[0][2]], [points[0][2], points[0][3]] ])
		arc = Arc(points_init)

		slide_x=5
		point_x=3
		arc.slide_x(KnotDef.OPERAND_GREATER_THAN, point_x, slide_x)
		points_init[2][0] += slide_x
		points_init[3][0] += slide_x
		self.assertEqual(arc.get_points(), points[1])

		slide_y=3
		point_y=3
		arc.slide_y(KnotDef.OPERAND_GREATER_THAN, point_y, slide_y)
		points_init[1][1] += slide_y
		points_init[2][1] += slide_y
		self.assertEqual(arc.get_points(), points[1])


	def is_cross_test(self):
		points_init=[[0,0], [0,5], [5,5], [5,0]]
		points=[points_init]
		points.append([ [points[0][0], points[0][1]], [points[0][1], points[0][2]], [points[0][2], points[0][3]] ])
		arc = Arc(points_init)

		#cross point
		self.assertTrue(arc.is_cross([-1,0], [2,0]))
		#has point
		self.assertTrue(arc.is_cross([1,5], [0,5]))
		self.assertTrue(arc.is_cross([5,5], [5,6]))
		#on the line
		self.assertTrue(arc.is_cross([5,-1], [5,1]))
		self.assertTrue(arc.is_cross([-1,5], [1,5]))
		self.assertTrue(arc.is_cross([1,5], [3,5]))
		#cross 1 point
		self.assertTrue(arc.is_cross([-1,1], [1,1]))
		self.assertTrue(arc.is_cross([2,4], [4,6]))
		self.assertTrue(arc.is_cross([4,6], [2,4]))
		#no point
		self.assertFalse(arc.is_cross([1,0], [4,0]))
		self.assertFalse(arc.is_cross([-2,1], [-1,1]))
		self.assertFalse(arc.is_cross([2,6], [4,7]))

	def slide_loop_test(self):
		points_init=[[0,0], [0,5], [5,5], [5,0], [0,0]]
		points=[points_init]
		points.append([ [points[0][0], points[0][1]], [points[0][1], points[0][2]], [points[0][2], points[0][3]], [points[0][3], points[0][4]] ])
		arc = Arc(points_init)
		slide_x=5
		point_x=0
		arc.slide_x(KnotDef.OPERAND_GREATER_THAN|KnotDef.OPERAND_EQUAL, point_x, slide_x)
		for data in points_init[0]:
			data[0] += slide_x
		self.assertEqual(arc.get_points(), points[1])

	def test_Arc(self):
		#test points
		self.inittest()

		#test slide x and y (operand ==)\
		self.slide_x_and_y_operand_eq_test()

		#test slide x and y (operand <)
		self.slide_x_and_y_operand_lt_test()

		#test slide x and y (operand >=)
		self.slide_x_and_y_operand_gt_test()

		#test cross
		self.is_cross_test()

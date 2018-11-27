# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../') 
from Nodes import Nodes
from KnotDefinition import KnotDef

class TestNodes(unittest.TestCase):
	def init(self):
		return [[1,11],[1,22],[3,22],[3,44],[5,55]]

	def test_Nodes(self):
		#test points
		points=self.init()
		#test initialize
		nodes = Nodes(points)
		result_nodes=nodes.get_points()
		self.assertEqual(result_nodes, points)

		#test slide
		slide=[1,2]
		slide_points=[]
		for point in points:
			point_add = point.copy()
			point_add[0]+=slide[0]
			point_add[1]+=slide[1]
			slide_points.append(point_add)

		nodes.slide_points(slide)
		self.assertEqual(nodes.get_points(), slide_points)

		#test slide x and y (operand ==)
		points=self.init()
		nodes = Nodes(points)
		slide_points=self.init()

		slide_x=5
		slide_points[0][0] += slide_x
		slide_points[1][0] += slide_x
		nodes.slide_x(KnotDef.OPERAND_EQUAL, points[1][0], slide_x)
		self.assertEqual(nodes.get_points(), slide_points)

		slide_y=3
		slide_points[2][1] += slide_y
		slide_points[1][1] += slide_y
		nodes.slide_y(KnotDef.OPERAND_EQUAL, points[2][1], slide_y)
		self.assertEqual(nodes.get_points(), slide_points)

		#test slide x and y (operand <)
		points=self.init()
		nodes = Nodes(points)
		slide_points=self.init()

		slide_x=5
		slide_points[0][0] += slide_x
		slide_points[1][0] += slide_x
		nodes.slide_x(KnotDef.OPERAND_LESS_THAN, points[3][0], slide_x)
		self.assertEqual(nodes.get_points(), slide_points)

		slide_y=3
		slide_points[2][1] += slide_y
		slide_points[1][1] += slide_y
		slide_points[0][1] += slide_y
		nodes.slide_y(KnotDef.OPERAND_LESS_THAN, points[3][1], slide_y)
		self.assertEqual(nodes.get_points(), slide_points)

		#test slide x and y (operand >=)
		points=self.init()
		nodes = Nodes(points)
		slide_points=self.init()

		slide_x=5
		slide_points[2][0] += slide_x
		slide_points[3][0] += slide_x
		slide_points[4][0] += slide_x
		nodes.slide_x(KnotDef.OPERAND_GREATER_THAN, points[1][0], slide_x)
		self.assertEqual(nodes.get_points(), slide_points)

		slide_y=3
		slide_points[3][1] += slide_y
		slide_points[4][1] += slide_y
		nodes.slide_y(KnotDef.OPERAND_GREATER_THAN, points[2][1], slide_y)
		self.assertEqual(nodes.get_points(), slide_points)

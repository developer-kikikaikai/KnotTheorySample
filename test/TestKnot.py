# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../') 
from Knot import Knot
from KnotDefinition import KnotDef

class TestKnot(unittest.TestCase):

	def initialize_test(self):
		knot_testdata = {
			Knot.DATATYPE_CROSS:[[1,Knot.CROSSTYPE_NONE]],
			Knot.DATATYPE_ARCS:[]
		}
		#new
		knot = Knot()
		self.assertEqual(knot.get_knot_data(), knot_testdata)

	def add_cross(self):
		knot_testdata = {
			Knot.DATATYPE_CROSS:[[1,Knot.CROSSTYPE_NONE]],
			Knot.DATATYPE_ARCS:[]
		}
		#new
		knot = Knot()

		#add to west
		self.assertTrue(knot.join_cross(1, Knot.CROSS_WEST))
		knot_testdata[Knot.DATATYPE_CROSS].append([2,Knot.CROSSTYPE_NONE])
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_WEST],[2,Knot.CROSS_EAST]],
			Knot.DATATYPE_ARCS:[[[0,0],[8,0]]]
			})
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#check already connect
		self.assertFalse(knot.join_cross(1, Knot.CROSS_WEST))

		#add to east
		self.assertTrue(knot.join_cross(1, Knot.CROSS_EAST))
		knot_testdata[Knot.DATATYPE_CROSS].append([3,Knot.CROSSTYPE_NONE])
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_EAST],[3,Knot.CROSS_WEST]],
			Knot.DATATYPE_ARCS:[[[0,0],[-8,0]]]
			})
		self.assertEqual(knot.get_knot_data(), knot_testdata)
		#check already connect
		self.assertFalse(knot.join_cross(1, Knot.CROSS_EAST))

		#add to north
		self.assertTrue(knot.join_cross(2, Knot.CROSS_NORTH))
		knot_testdata[Knot.DATATYPE_CROSS].append([4,Knot.CROSSTYPE_NONE])
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[2,Knot.CROSS_NORTH],[4,Knot.CROSS_SOUTH]],
			Knot.DATATYPE_ARCS:[[[8,0],[8,8]]]
			})
		self.assertEqual(knot.get_knot_data(), knot_testdata)
		#check already connect
		self.assertFalse(knot.join_cross(2, Knot.CROSS_NORTH))

		#add to south
		self.assertTrue(knot.join_cross(3, Knot.CROSS_SOUTH))
		knot_testdata[Knot.DATATYPE_CROSS].append([5,Knot.CROSSTYPE_NONE])
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[3,Knot.CROSS_SOUTH],[5,Knot.CROSS_NORTH]],
			Knot.DATATYPE_ARCS:[[[-8,0],[-8,-8]]]
			})
		self.assertEqual(knot.get_knot_data(), knot_testdata)
		#check already connect
		self.assertFalse(knot.join_cross(3, Knot.CROSS_SOUTH))

		return [knot, knot_testdata]

	def add_cross_test(self):
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]

		#slide at north
		self.assertTrue(knot.join_cross(1, Knot.CROSS_NORTH))
		knot_testdata[Knot.DATATYPE_CROSS].append([6,Knot.CROSSTYPE_NONE])
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_NORTH],[6,Knot.CROSS_SOUTH]],
			Knot.DATATYPE_ARCS:[[[0,0],[0,8]]]
			})
		#slide 4
		knot_testdata[Knot.DATATYPE_ARCS][2][Knot.DATATYPE_ARCS][0][1][1] += 4
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#slide at east
		self.assertTrue(knot.join_cross(4, Knot.CROSS_EAST))
		knot_testdata[Knot.DATATYPE_CROSS].append([7,Knot.CROSSTYPE_NONE])
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[4,Knot.CROSS_EAST],[7,Knot.CROSS_WEST]],
			Knot.DATATYPE_ARCS:[[[8,12],[0,12]]]
			})
		#slide 4
		knot_testdata[Knot.DATATYPE_ARCS][0][Knot.DATATYPE_ARCS][0][0][0] -= 4
		knot_testdata[Knot.DATATYPE_ARCS][1][Knot.DATATYPE_ARCS][0][0][0] -= 4
		knot_testdata[Knot.DATATYPE_ARCS][1][Knot.DATATYPE_ARCS][0][1][0] -= 4
		knot_testdata[Knot.DATATYPE_ARCS][3][Knot.DATATYPE_ARCS][0][0][0] -= 4
		knot_testdata[Knot.DATATYPE_ARCS][3][Knot.DATATYPE_ARCS][0][1][0] -= 4
		knot_testdata[Knot.DATATYPE_ARCS][4][Knot.DATATYPE_ARCS][0][0][0] -= 4
		knot_testdata[Knot.DATATYPE_ARCS][4][Knot.DATATYPE_ARCS][0][1][0] -= 4
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#slide at west
		self.assertTrue(knot.join_cross(5, Knot.CROSS_WEST))
		knot_testdata[Knot.DATATYPE_CROSS].append([8,Knot.CROSSTYPE_NONE])
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[5,Knot.CROSS_WEST],[8,Knot.CROSS_EAST]],
			Knot.DATATYPE_ARCS:[[[-12,-8],[-4,-8]]]
			})
		#slide 4
		knot_testdata[Knot.DATATYPE_ARCS][0][Knot.DATATYPE_ARCS][0][0][0] += 4
		knot_testdata[Knot.DATATYPE_ARCS][0][Knot.DATATYPE_ARCS][0][1][0] += 4
		knot_testdata[Knot.DATATYPE_ARCS][1][Knot.DATATYPE_ARCS][0][0][0] += 4
		knot_testdata[Knot.DATATYPE_ARCS][2][Knot.DATATYPE_ARCS][0][0][0] += 4
		knot_testdata[Knot.DATATYPE_ARCS][2][Knot.DATATYPE_ARCS][0][1][0] += 4
		knot_testdata[Knot.DATATYPE_ARCS][4][Knot.DATATYPE_ARCS][0][0][0] += 4
		knot_testdata[Knot.DATATYPE_ARCS][4][Knot.DATATYPE_ARCS][0][1][0] += 4
		knot_testdata[Knot.DATATYPE_ARCS][5][Knot.DATATYPE_ARCS][0][0][0] += 4
		knot_testdata[Knot.DATATYPE_ARCS][5][Knot.DATATYPE_ARCS][0][1][0] += 4
		print(knot.get_knot_data())
		print(knot_testdata)
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#slide at south
		self.assertTrue(knot.join_cross(1, Knot.CROSS_SOUTH))
		knot_testdata[Knot.DATATYPE_CROSS].append([9,Knot.CROSSTYPE_NONE])
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_SOUTH],[9,Knot.CROSS_NORTH]],
			Knot.DATATYPE_ARCS:[[[0,0],[0,-8]]]
			})
		#slide 2
		knot_testdata[Knot.DATATYPE_ARCS][3][Knot.DATATYPE_ARCS][0][1][1] -= 4
		knot_testdata[Knot.DATATYPE_ARCS][6][Knot.DATATYPE_ARCS][0][0][1] -= 4
		knot_testdata[Knot.DATATYPE_ARCS][6][Knot.DATATYPE_ARCS][0][1][1] -= 4
		print(knot.get_knot_data())
		print(knot_testdata)
		self.assertEqual(knot.get_knot_data(), knot_testdata)

	def add_arc_test(self):
		#create knot
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]

		#failed, already set
		self.assertFalse(knot.connect_cross(1,Knot.CROSS_NORTH, 2,Knot.CROSS_NORTH))
		self.assertFalse(knot.connect_cross(1,Knot.CROSS_NORTH, 2,Knot.CROSS_EAST))
		self.assertFalse(knot.connect_cross(1,Knot.CROSS_NORTH, 3,Knot.CROSS_WEST))
		self.assertFalse(knot.connect_cross(1,Knot.CROSS_NORTH, 3,Knot.CROSS_SOUTH))
		self.assertFalse(knot.connect_cross(2,Knot.CROSS_NORTH,1,Knot.CROSS_NORTH))
		self.assertFalse(knot.connect_cross(2,Knot.CROSS_EAST,1,Knot.CROSS_NORTH))
		self.assertFalse(knot.connect_cross(3,Knot.CROSS_WEST,1,Knot.CROSS_NORTH))
		self.assertFalse(knot.connect_cross(3,Knot.CROSS_SOUTH,1,Knot.CROSS_NORTH))

		#north->north, 1->4
		self.assertTrue(knot.connect_cross(1,Knot.CROSS_NORTH, 4,Knot.CROSS_NORTH))
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_NORTH],[4,Knot.CROSS_NORTH]],
			Knot.DATATYPE_ARCS:[[[0,0],[0,12]],[[0,12],[8,12]],[[8,12],[8,8]]]
			})
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#north->east, 1->3
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]
		self.assertTrue(knot.connect_cross(1,Knot.CROSS_NORTH, 3,Knot.CROSS_EAST))
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_NORTH],[3,Knot.CROSS_EAST]],
			Knot.DATATYPE_ARCS:[[[0,0],[0,4]],[[0,4],[-12,4]],[[-12,0],[-8,0]]]
			})
		#slide arc
		knot_testdata[Knot.DATATYPE_ARCS][2][Knot.DATATYPE_ARCS][0][1]+=2
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#north->south, 1->5
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]
		self.assertTrue(knot.connect_cross(1,Knot.CROSS_NORTH, 3,Knot.CROSS_SOUTH))
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_NORTH],[5,Knot.CROSS_SOUTH]],
			Knot.DATATYPE_ARCS:[[[0,0],[0,12]],[[0,12],[12,12]],[[12,-12],[-8,-12]],[[-8,-12],[-8,-8]]]
			})
		#slide arc
		knot_testdata[Knot.DATATYPE_ARCS][2][Knot.DATATYPE_ARCS][0][1]+=2
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#north->west, 1->4
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]
		self.assertTrue(knot.connect_cross(1,Knot.CROSS_NORTH, 4,Knot.CROSS_WEST))
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_NORTH],[4,Knot.CROSS_WEST]],
			Knot.DATATYPE_ARCS:[[[0,0],[0,12]],[[0,12],[12,12]],[[12,8],[8,8]]]
			})
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#east->south, 3->5
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]
		self.assertTrue(knot.connect_cross(3,Knot.CROSS_EAST, 5,Knot.CROSS_SOUTH))
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[3,Knot.CROSS_EAST],[5,Knot.CROSS_SOUTH]],
			Knot.DATATYPE_ARCS:[[[-8,0],[-12,0]],[[-12,-12],[-8,-12]],[[-8,-12],[-8,-8]]]
			})
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#east->west, 3->5
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]
		self.assertTrue(knot.connect_cross(3,Knot.CROSS_EAST, 5,Knot.CROSS_WEST))
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[3,Knot.CROSS_EAST],[5,Knot.CROSS_WEST]],
			Knot.DATATYPE_ARCS:[[[-8,0],[-12,0]],[[-12,-12],[-4,-12]],[[-4,-8],[-8,-8]]]
			})
		#slide arc
		knot_testdata[Knot.DATATYPE_ARCS][0][Knot.DATATYPE_ARCS][0][0]+=2
		knot_testdata[Knot.DATATYPE_ARCS][0][Knot.DATATYPE_ARCS][1][0]+=2
		knot_testdata[Knot.DATATYPE_ARCS][1][Knot.DATATYPE_ARCS][1][0]+=2
		knot_testdata[Knot.DATATYPE_ARCS][2][Knot.DATATYPE_ARCS][0][0]+=2
		knot_testdata[Knot.DATATYPE_ARCS][2][Knot.DATATYPE_ARCS][1][0]+=2
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#south->south, 0->1
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]
		self.assertTrue(knot.connect_cross(1,Knot.CROSS_SOUTH, 2,Knot.CROSS_SOUTH))
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_SOUTH],[2,Knot.CROSS_SOUTH]],
			Knot.DATATYPE_ARCS:[[[0,0],[0,-4]],[[0,-4],[8,-4]],[[8,-4],[8,0]]]
			})
		knot_testdata[Knot.DATATYPE_ARCS][3][Knot.DATATYPE_ARCS][1][1]-=2
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#south->west, 1->4
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]
		self.assertTrue(knot.connect_cross(1,Knot.CROSS_SOUTH, 4,Knot.CROSS_WEST))
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[1,Knot.CROSS_SOUTH],[4,Knot.CROSS_WEST]],
			Knot.DATATYPE_ARCS:[[[0,0],[0,-4]],[[0,-4],[12,-4]],[[12,-4],[12,8]],[[12,8],[8,8]]]
			})
		knot_testdata[Knot.DATATYPE_ARCS][1][Knot.DATATYPE_ARCS][1][0]-=2
		knot_testdata[Knot.DATATYPE_ARCS][3][Knot.DATATYPE_ARCS][0][0]-=2
		knot_testdata[Knot.DATATYPE_ARCS][3][Knot.DATATYPE_ARCS][1][0]-=2
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#west->west, 2->4
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]
		self.assertTrue(knot.connect_cross(2,Knot.CROSS_WEST, 4,Knot.CROSS_WEST))
		knot_testdata[Knot.DATATYPE_ARCS].append({
			Knot.DATATYPE_CROSS:[[2,Knot.CROSS_WEST],[4,Knot.CROSS_WEST]],
			Knot.DATATYPE_ARCS:[[[8,0],[12,0]],[[12,0],[12,8]],[[12,8],[8,8]]]
			})
		self.assertEqual(knot.get_knot_data(), knot_testdata)

		#check separating west
		knot_info = self.add_cross()
		knot = knot_info[0]
		knot_testdata = knot_info[1]
		self.assertTrue(knot.connect_cross(1,Knot.CROSS_NORTH, 1,Knot.CROSS_SOUTH))
		#north->
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_NORTH, 3,Knot.CROSS_NORTH))
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_NORTH, 3,Knot.CROSS_EAST))
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_NORTH, 5,Knot.CROSS_SOUTH))
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_NORTH, 5,Knot.CROSS_WEST))
		#east->
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_EAST, 3,Knot.CROSS_NORTH))
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_EAST, 3,Knot.CROSS_EAST))
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_EAST, 5,Knot.CROSS_SOUTH))
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_EAST, 5,Knot.CROSS_WEST))
		#west->
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_WEST, 3,Knot.CROSS_NORTH))
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_WEST, 3,Knot.CROSS_EAST))
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_WEST, 5,Knot.CROSS_SOUTH))
		self.assertFalse(knot.connect_cross(4,Knot.CROSS_WEST, 5,Knot.CROSS_WEST))
		#south->
		self.assertFalse(knot.connect_cross(2,Knot.CROSS_SOUTH, 3,Knot.CROSS_NORTH))
		self.assertFalse(knot.connect_cross(2,Knot.CROSS_SOUTH, 3,Knot.CROSS_EAST))
		self.assertFalse(knot.connect_cross(2,Knot.CROSS_SOUTH, 5,Knot.CROSS_SOUTH))
		self.assertFalse(knot.connect_cross(2,Knot.CROSS_SOUTH, 5,Knot.CROSS_WEST))

	def test_Knot(self):
		#initialize test
		self.initialize_test()

		#add cross
		self.add_cross_test()

		#add arc
		self.add_arc_test()

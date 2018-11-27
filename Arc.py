from Nodes import Nodes
class Arc:
	#list_of_points: list of [x,y]
	# arcs are only holizonal line or Vertical line
	def __init__(self, list_of_points):
		self._nodes=[]
		for i in range(0,len(list_of_points)-1):
			self._nodes.append(Nodes([list_of_points[i], list_of_points[i+1]]))

	#slide position
	def slide_points(self, slide_point):
		for node in self._nodes:
			node.slide_points(slide_point)

	#slide x
	def slide_x(self, operand, place_x, slide_point):
		for node in self._nodes:
			node.slide_x(operand, place_x, slide_point)

	#slide y
	def slide_y(self, operand, place_y, slide_point):
		for node in self._nodes:
			node.slide_y(operand, place_y, slide_point)

	#parallel dislacement, move point[0] to [(0, 0), (0, y)]
	def _parallel_dislacement(self, base_line, check_line):
		#slide base
		parallel_info=[[0, 0]]
		#roll 90 degree or not
		if base_line[1][0] == base_line[0][0]:
			#check which position is 
			if base_line[1][1] < base_line[0][1]:
				sign = -1
			else:
				sign = 1
			parallel_info.append([ base_line[1][0] - base_line[0][0], sign*( base_line[1][1] - base_line[0][1])])
			parallel_info.append([check_line[0][0] - base_line[0][0], sign*(check_line[0][1] - base_line[0][1])])
			parallel_info.append([check_line[1][0] - base_line[0][0], sign*(check_line[1][1] - base_line[0][1])])
		#roll 90 degree
		else:
			if base_line[1][0] < base_line[0][0]:
				sign = -1
			else:
				sign = 1
			parallel_info.append([ base_line[1][1] - base_line[0][1], sign*( base_line[1][0] - base_line[0][0])])
			parallel_info.append([check_line[0][1] - base_line[0][1], sign*(check_line[0][0] - base_line[0][0])])
			parallel_info.append([check_line[1][1] - base_line[0][1], sign*(check_line[1][0] - base_line[0][0])])

		return parallel_info

	#check cross
	def _is_cross(self, parallel_info):
		#base line is (0,0), (0,y)
		base_y = parallel_info[1][1]
		point1 = parallel_info[2]
		point2 = parallel_info[3]

		#accross x=0?
		if (point1[0] < 0 and point2[0] < 0) or (point1[0] > 0 and point2[0] > 0):
			return False

		#on y area? check [0, base_y] and [point1[1], point2[1]]
		if ((point1[1] < 0) and (point2[1] < 0)) or ((base_y < point1[1]) and (base_y < point2[1])):
			return False

		return True

	#is cross x, 
	# arcs are only holizonal line or Vertical line
	def is_cross(self, point1, point2):
		for node in self._nodes:
			#2 points
			points = node.get_points()
			parallel_dislancement = self._parallel_dislacement(points, [point1, point2])

			if self._is_cross(parallel_dislancement):
				return True
		return False

	#get points
	def get_points(self):
		points=[]
		for node in self._nodes:
			points.append(node.get_points())
		return points

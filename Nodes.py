from KnotDefinition import KnotDef

#list of point, set arc, 
#slide points
class Nodes:

	#list_of_points: list of [x,y]
	def __init__(self, list_of_points):
		self._points = []
		for point in list_of_points:
			self._points.append([point[0], point[1]])

	#slide position
	def slide_points(self, slide_point):
		for point in self._points:
			point[0]+=slide_point[0]
			point[1]+=slide_point[1]

	#private, operand check
	def _operand(self, operand, input1, input2):
		#check == 
		if (operand & KnotDef.OPERAND_EQUAL != 0) and (input1 == input2):
			return True
		#check <
		if (operand & KnotDef.OPERAND_LESS_THAN != 0) and (input1 < input2):
			return True
		#check >
		if (operand & KnotDef.OPERAND_GREATER_THAN != 0) and (input1 > input2):
			return True

		return False

	#slide x
	def slide_x(self, operand, place_x, slide_x):
		for point in self._points:
			if self._operand(operand, point[0], place_x):
				point[0] += slide_x

	#slide y
	def slide_y(self, operand, place_y, slide_y):
		for point in self._points:
			if self._operand(operand, point[1], place_y):
				point[1] += slide_y

	#get positions
	def get_points(self):
		return self._points

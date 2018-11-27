from Nodes import Nodes
class Cross:
	#point: [x,y]
	# arcs are only holizonal line or Vertical line
	def __init__(self, point):
		self._node=Nodes([[point[0],point[1]]])

	#slide position
	def slide_point(self, slide_point):
		self._node.slide_points(slide_point)

	#get points
	def get_point(self):
		return self._node.get_points()[0]

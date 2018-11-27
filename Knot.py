from Cross import Cross
from Arc import Arc
from KnotDefinition import KnotDef

class Knot:

	#information data type
	DATATYPE_CROSS="cross"
	DATATYPE_ARCS="arcs"

	#Cross Type
	CROSSTYPE_NONE=0
	CROSSTYPE_PLUS_NORMAL=1
	CROSSTYPE_PLUS_RANGLE=2
	CROSSTYPE_PLUS_OPPOSED=3
	CROSSTYPE_PLUS_LANGLE=4
	CROSSTYPE_MINUS_NORMAL=5
	CROSSTYPE_MINUS_RANGLE=6
	CROSSTYPE_MINUS_OPPOSED=7
	CROSSTYPE_MINUS_LANGLE=8

	#slide place
	SLIDE_VALUE=2

	#Direction
	CROSS_NORTH="north"
	CROSS_SOUTH="south"
	CROSS_EAST="east"
	CROSS_WEST="west"

	#cross: hash of points
	#arcs: hash of arcs, [cross_name1, name2, arcs]
	def __init__(self):
		self.crosses=[[1,self.CROSSTYPE_NONE]]
		self.crosses_place=[Cross([0,0])]
		self.arcs=[]
		#list of arcs
		self.neighborhoods=[Arc([[-1,-1],[-1,1],[1,1],[1,-1],[-1,-1]])]
		self.CROSS_PLACE={
			self.CROSS_NORTH:[0, self.SLIDE_VALUE],
			self.CROSS_SOUTH:[0, -1*(self.SLIDE_VALUE)],
			self.CROSS_EAST :[-1*(self.SLIDE_VALUE), 0],
			self.CROSS_WEST :[self.SLIDE_VALUE, 0],
		}
		self.CROSS_DIRECTION_PAIR={
			self.CROSS_NORTH:self.CROSS_SOUTH,
			self.CROSS_SOUTH:self.CROSS_NORTH,
			self.CROSS_EAST :self.CROSS_WEST,
			self.CROSS_WEST :self.CROSS_EAST,
		}
		self.CROSS_OPERATE_PAIR={
			self.CROSS_NORTH:KnotDef.OPERAND_EQUAL | KnotDef.OPERAND_GREATER_THAN,
			self.CROSS_SOUTH:KnotDef.OPERAND_EQUAL | KnotDef.OPERAND_LESS_THAN,
			self.CROSS_EAST :KnotDef.OPERAND_EQUAL | KnotDef.OPERAND_LESS_THAN,
			self.CROSS_WEST :KnotDef.OPERAND_EQUAL | KnotDef.OPERAND_GREATER_THAN,
		}

		#両方向チェックしてあげないといけないやつ方向が北南ではなく、直線的に繋いで、ぶつかった場所を上下左右にずらしていく系にしないといけない。
		## +-----+
		#  |     |
		##++    ++
		# a     b
		#例えばa↑とb↑を接続する場合を考慮

	def _get_connected_place(self, cross_num, direction):
		cross_place=self.crosses_place[cross_num-1].get_point()
		return Cross([ cross_place[0] + 4*self.CROSS_PLACE[direction][0], cross_place[1] + 4*self.CROSS_PLACE[direction][1] ])

	def _new_cross(self):
		new_id = len(self.crosses)+1
		return [new_id,self.CROSSTYPE_NONE]

#	def _is_cross_arc(self, cross_name1 direction):
#		return

#	def _is_arc_and_cross(self, cross_name1 direction):
#		return

	def _slide_arcs(self, cross_data, direction):
		cross_place=None
		print("_slide_arcs " + str(cross_data) + ", len " + str(len(self.crosses_place)))
		#search cross point num
		for n in range(0,len(self.crosses_place)):
			print("cross_data " + str(cross_data))
			print("self.crosses_place[n].get_point() " + str(self.crosses_place[n].get_point()))
			if cross_data == self.crosses_place[n].get_point():
				print("place " + str(n + 1))
				#keep cross point num if place is same as cross_data
				cross_place = n + 1
				break

		slide_point=self.CROSS_PLACE[direction]
		operate=self.CROSS_OPERATE_PAIR[direction]
		for arc_info in self.arcs:
			#arcs has cross place? yes=> skip
			if cross_place != None and ((arc_info[self.DATATYPE_CROSS][0][0] == cross_place) or (arc_info[self.DATATYPE_CROSS][1][0] == cross_place)):
				continue

			print("slide " + str(slide_point) + "at " + str(arc_info[self.DATATYPE_ARCS].get_points()) + ", slide point: "+str(cross_data))
			#slide arcs
			if (direction == self.CROSS_NORTH) or (direction == self.CROSS_SOUTH):
				arc_info[self.DATATYPE_ARCS].slide_y(operate, cross_data[1], slide_point[1]*2)
			else:
				arc_info[self.DATATYPE_ARCS].slide_x(operate, cross_data[0], slide_point[0]*2)

	def _slide_crosses(self, cross_data, direction):
		cross_position = cross_data.get_point()
		for cross in self.crosses_place:
			if cross == cross_data:
				continue
			tmp_cross_position = cross.get_point()
			print("check " + str(tmp_cross_position) + "and " + str(cross_position))
			if ((direction == self.CROSS_NORTH) and (tmp_cross_position[1] < cross_position[1]) ) or ( (direction == self.CROSS_SOUTH) and (cross_position[1] < tmp_cross_position[1]) ):
				continue
			elif ((direction == self.CROSS_WEST) and (tmp_cross_position[0] < cross_position[0]) ) or ( (direction == self.CROSS_EAST) and (cross_position[0] < tmp_cross_position[0]) ):
				continue
			print("slide " + str(tmp_cross_position))
			cross.slide_point([self.CROSS_PLACE[direction][0]*2, self.CROSS_PLACE[direction][1]*2])

	#
	def _slide_neighborhoods(self, cross_data, direction):
		slide_point=self.CROSS_PLACE[direction]
		operate=self.CROSS_OPERATE_PAIR[direction]
		for neighborhood in self.neighborhoods:
			#slide arcs
			if (direction == self.CROSS_NORTH) or (direction == self.CROSS_SOUTH):
				neighborhood.slide_y(operate, cross_data[1], slide_point[1]*2)
			else:
				neighborhood.slide_x(operate, cross_data[0], slide_point[0]*2)

	def _has_arc(self, cross_name1, direction):
		for arc_info in self.arcs:
			for cross in arc_info[self.DATATYPE_CROSS]:
				if cross[0] == cross_name1 and cross[1] == direction:
					return True
		return False

	#slide position
	def join_cross(self, cross_name1, direction):
		if self._has_arc(cross_name1, direction):
			return False

		new_place = self._get_connected_place(cross_name1, direction)
		cross = self._new_cross()

		#add cross
		self.crosses.append(cross)
		self.crosses_place.append(new_place)
		new_arcs={
			self.DATATYPE_CROSS:[ [cross_name1, direction],[cross[0], self.CROSS_DIRECTION_PAIR[direction]] ],
		}
		new_arcs[self.DATATYPE_ARCS]=Arc([self.crosses_place[cross_name1-1].get_point(), new_place.get_point()])
		self.arcs.append(new_arcs)

		#slide crosses and arcs
		self._slide_crosses(new_place, direction)
		self._slide_arcs(new_place.get_point(), direction)

		#slide neighborhood
		self._slide_neighborhoods([new_place.get_point()[0] + (-1)*self.CROSS_PLACE[direction][0]/self.SLIDE_VALUE, new_place.get_point()[1] + (-1)*self.CROSS_PLACE[direction][1]/self.SLIDE_VALUE], direction)
		#add new neighborhood
		if self.CROSS_PLACE[direction][0] == 0:
			index=1
		else:
			index=0

		neiborhood_slide=[int(self.CROSS_PLACE[direction][0]/self.SLIDE_VALUE), int(self.CROSS_PLACE[direction][1]/self.SLIDE_VALUE)]
		neighborhood_point=[self.crosses_place[cross_name1-1].get_point()[0], self.crosses_place[cross_name1-1].get_point()[1]]
		neighborhood_point[0] += neiborhood_slide[0]
		neighborhood_point[1] += neiborhood_slide[1]
		new_neighborhood=[]
		new_neighborhood.append([new_place.get_point()[0] + (-1)*(neiborhood_slide[0]) , new_place.get_point()[1] + (-1)*(neiborhood_slide[1])])
		new_neighborhood.append([new_place.get_point()[0] + (neiborhood_slide[0]), new_place.get_point()[1] + (neiborhood_slide[1])])
		print("__check__" + str(new_neighborhood))
		print("__check__" + str(self.crosses_place[cross_name1-1].get_point()) + direction)
		print("__check__" + str(neighborhood_point))
		for i in range(0,len(self.neighborhoods)):
			print("__XXXX__"+str(self.neighborhoods[i].get_points()))
			if self.neighborhoods[i].is_cross(self.crosses_place[cross_name1-1].get_point(), new_place.get_point()):
				#update neighborhood
				points = self.neighborhoods[i].get_points()
				new_points=[]
				for point in points:
					#slide neighborhood
					if ( (abs(point[0][0]-neighborhood_point[0])+abs(point[0][1]-neighborhood_point[1])) == 1) and ( (abs(point[1][0]-neighborhood_point[0])+abs(point[1][1]-neighborhood_point[1])) == 1):
						print("Change neighborhood " + str(point[0]))
						print(new_neighborhood)
						#change neighborhood
						new_points.append(point[0])
						new_points.append([new_neighborhood[0][0] + point[0][0]-neighborhood_point[0], new_neighborhood[0][1] + point[0][1]-neighborhood_point[1]])
						new_points.append([new_neighborhood[1][0] + point[0][0]-neighborhood_point[0], new_neighborhood[1][1] + point[0][1]-neighborhood_point[1]])
						new_points.append([new_neighborhood[1][0] + -1*( point[0][0]-neighborhood_point[0]), new_neighborhood[1][1] + -1*( point[0][1]-neighborhood_point[1])])
						new_points.append([new_neighborhood[0][0] + -1*( point[0][0]-neighborhood_point[0]), new_neighborhood[0][1] + -1*( point[0][1]-neighborhood_point[1])])
					else:
						new_points.append(point[0])
				new_points.append(points[len(points)-1][1])
				self.neighborhoods[i] = Arc(new_points)
				print("____"+str(self.neighborhoods[i].get_points()))
				break

		return True

	def _next_direction(self, cross_name1, direction1, cross_name2, direction2):
		return

	#arcs
	def _get_base_arcs(self, cross_name1, direction1, cross_name2, direction2):
		#set arc
		return

	#startが4, 2個ずらす
	#connect 2 crosses [cross_num, cross_place], [cross_num, cross_place]
	def connect_cross(self, cross_name1, direction1, cross_name2, direction2):
		if self._has_arc(cross_name1, direction1) or self._has_arc(cross_name2, direction2):
			return False

		#base line
		#base_arcs = 
		return True

	#set crossing type
	def set_cross_type(self, cross_name1, type):
		return

	#get knot data
	#format as:
	#{
	#	"cross":
	#		[
	#			#cross num, type(0-8)
	#			[1, 0],
	#		],
	#	"arcs":
	#		[
	#			{"cross":[[1,"west" ],[2,"east" ]],"arcs":[[0,0],[x,0]},
	#			{"cross":[[2,"east" ],[2,"north"]],"arcs":[[x,y],[x,y]]},
	#			{"cross":[[2,"south"],[1,"south"]],"arcs":[[x,y],[x,y]]},
	#			{"cross":[[1,"north"],[1,"east" ]],"arcs":[[x,y],[x,y]]},
	#		]
	#}
	def get_knot_data(self):
		result={
			self.DATATYPE_CROSS:self.crosses,
			self.DATATYPE_ARCS:[],
		}
		for arc_info in self.arcs:
			new_arcs={self.DATATYPE_CROSS:arc_info[self.DATATYPE_CROSS], self.DATATYPE_ARCS:arc_info[self.DATATYPE_ARCS].get_points()}
			result[self.DATATYPE_ARCS].append(new_arcs)
		return result

	def write_knotfigure(self):
		result={
			self.DATATYPE_CROSS:self.crosses,
			self.DATATYPE_ARCS:{},
		}
		for arc_info in self.arcs:
			result[self.DATATYPE_ARCS][self.DATATYPE_CROSS] = arc_info[self.DATATYPE_CROSS]
			result[self.DATATYPE_ARCS][self.DATATYPE_ARCS] = arc_info[self.DATATYPE_ARCS].get_points()
		return result

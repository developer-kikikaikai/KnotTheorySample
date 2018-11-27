import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('point_1.png')

#グラフ

#有向グラフ
#Graph = nx.DiGraph()
#無向グラフ
Graph = nx.Graph()

cross_tag="cross"
direction={"north":"n", "south":"s", "east":"e", "west":"w"}

#頂点を決める
Graph.to_undirected()
for i in range(1,6):
	Graph.add_node(f'{cross_tag}{i}')
	for key, dir in direction.items():
		Graph.add_node(f'{dir}{i}')
		Graph.add_edge(f'{dir}{i}',f'{cross_tag}{i}')

# fixed place
fixed_positions = {f'{cross_tag}1':(0,0),f'{cross_tag}2':(5,0),f'{cross_tag}3':(10,0),f'{cross_tag}4':(15,0),f'{cross_tag}5':(20,0)}
point_place={"north":(0,-1),"south":(0,1),"east":(-1,0),"west":(1,0)}
update_positions={}
for i in range(1,6):
	print(f'{cross_tag}{i}')
	point=fixed_positions[f'{cross_tag}{i}']
	for dir, place in point_place.items():
		update_positions.update({f"{direction[dir]}{i}":(place[0]+point[0],place[1]+point[1])})
		print(update_positions)
fixed_positions.update(update_positions)

#set edge
Graph.add_edge('w1','e2')
Graph.add_edge('w2','e3')
#Graph.add_edge('w3','s1')
#add top start
Graph.add_nodes_from(['_t1','_t3'], node_size=0)
update_positions = {"_t1":(0,2),"_t3":(10+1,2)}
fixed_positions.update(update_positions)
Graph.add_edge('w3','_t3')
Graph.add_edge('_t3','_t1')
Graph.add_edge('_t1','s1')
#add top end
Graph.add_edge('n1','n2')
Graph.add_edge('s2','s3')
#Graph.add_edge('n3','e1')
#add bottom start
Graph.add_nodes_from(['b1','b3'], data=True)
update_positions = {"b1":(0-1,-2),"b3":(10,-2)}
fixed_positions.update(update_positions)
Graph.add_edge('n3','b3', data=True)
Graph.add_edge('b3','b1', data=True)
Graph.add_edge('b1','e1', data=True)
#add tail end
print("Graph")
print(Graph.nodes())
print(Graph.edges())
#print(Graph.simple_cycles())

#draw
plt.figure(figsize=(20,20))
pos = nx.spring_layout(Graph,pos=fixed_positions, fixed = fixed_positions.keys())
nx.draw_networkx(Graph,pos)

plt.axis("off")
#plt.savefig("default.png")
plt.show()
#plt.savefig("default2.png")
###全部接続した際のPlaceも覚えておくかな。なかったら作る

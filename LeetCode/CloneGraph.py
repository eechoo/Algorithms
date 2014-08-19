#!/usr/bin/python
'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
	/ \
         \_/
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []
	
	def cloneGraph2(self,node,map):
		if(not map.has_key(node.label)):
			map[node.label]=UndirectedGraphNode(node.label)
			for i in range(len(node.neighbors)):
				self.cloneGraph2(node.neighbors[i],map)
				map[node.label].neighbors.append(map[node.neighbors[i].label])			
		return map

	# @param node, a undirected graph node
	# @return a undirected graph node
	def cloneGraph(self, node):
		if(node == None):
			return None
		map=self.cloneGraph2(node,{})
		return map[node.label]

def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	node0=UndirectedGraphNode(0)
	node1=UndirectedGraphNode(1)
	node0.neighbors=[node1]
	node1.neighbors=[node1]
	result=node0.cloneGraph(node0)
	print result.label
	print result.neighbors[0].label


if __name__ == '__main__':
    main()
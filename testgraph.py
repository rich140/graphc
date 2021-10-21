import networkx as nx
import unittest
from graph import *

class TestGraph(unittest.TestCase):
    def test_bfs(self):
        G = nx.Graph()
        G.add_nodes_from([0,1,2,3])
        G.add_edges_from([(0,1),(0,2),(1,3),(2,3)])
        Vertices = [Vertex(v,0) for v in G.nodes]
        Edges = [Edge(u,v,0) for (u,v) in G.edges]
        EdgeIDTable = [0,2,3,0]
        EdgeIDTable = [idx for v in G.nodes for ]

        VProperty = [0] * G.number_of_nodes()
        VTempProperty = [0] + [99999] * (G.number_of_nodes()-1)
        VConst = [0] * G.number_of_nodes()

        ActiveVertex = [Vertices[0]]
        ActiveVertexCount = 1
        
        actual_VProperty= Run(Vertices, Edges, EdgeIDTable, VProperty, VTempProperty, VConst,
                ActiveVertex, ActiveVertexCount, 100)
        expected_VProperty = [0] * G.number_of_nodes()
        for it, nodes in dict(nx.bfs_successors(G, 0)).items():
            for i in range(len(nodes)):
                expected_VProperty[nodes[i]] = it + 1 
        self.assertListEqual(actual_VProperty, expected_VProperty)

if __name__ == "__main__":
    unittest.main()

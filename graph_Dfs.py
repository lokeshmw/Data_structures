import numpy as np


class DFS_Graph:

    def __init__(self, vertices):
        self._adjMatrix = np.zeros((vertices, vertices))
        self._vertices = vertices
        self._visited = [0] * vertices

    def insert_edge(self, u, v, x=1):
        self._adjMatrix[u][v] = x

    def remove_edge(self, u, v):
        self._adjMatrix[u][v] = 0

    def edge_exist(self, u, v):
        return self._adjMatrix[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMatrix[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def display_adjMat(self):
        print(self._adjMatrix)

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMatrix[i][j] != 0:
                    print(i, '--', j)

    def DFS(self, d):
        if self._visited[d] == 0:
            print(d, end=' ')
            self._visited[d] = 1
            for i in range(self._vertices):
                if self._adjMatrix[d][i] == 1 and self._visited[i] == 0:
                    self.DFS(i)


D = DFS_Graph(5)
D.insert_edge(0, 1)
D.insert_edge(0, 3)
D.insert_edge(0, 2)
D.insert_edge(1, 4)
D.insert_edge(1, 2)
D.insert_edge(1, 1)
D.insert_edge(1, 3)
D.insert_edge(2, 4)
D.insert_edge(2, 3)
D.insert_edge(2, 4)
D.insert_edge(3, 2)
D.insert_edge(4, 4)
D.insert_edge(4, 2)
print(D.remove_edge(4, 1))
print('Edges:')
D.edges()
print(D.display_adjMat())
print(D.edge_count())
print(D.vertex_count())
print('DFS:')
D.DFS(0)

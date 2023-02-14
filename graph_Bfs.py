from graph_queue import QueuesLinked
import numpy as np


class Graph:

    def __init__(self, vertices):
        self._adj_Matrix = np.zeros((vertices, vertices))
        self._vertices = vertices

    def insert_edge(self, u, v, x=1):
        self._adj_Matrix[u][v] = x

    def remove_edge(self, u, v):
        self._adj_Matrix[u][v] = 0

    def edge_exist(self, u, v):
        return self._adj_Matrix[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adj_Matrix[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adj_Matrix[i][j] != 0:
                    print(i, '--', j)

    def display_adjMat(self):
        print(self._adj_Matrix)

    def BFS(self, A):
        i = A
        q = QueuesLinked()
        visited = [0] * self._vertices
        print(i, end=' ')
        visited[i] = 1
        q.enqueue(i)
        while not q.isempty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adj_Matrix[i][j] == 1 and visited[j] == 0:
                    print(j, end=' ')
                    visited[j] = 1
                    q.enqueue(j)


b = Graph(6)
b.insert_edge(0, 1)
b.insert_edge(0, 5)
b.insert_edge(0, 4)
b.insert_edge(1, 0)
b.insert_edge(1, 2)
b.insert_edge(1, 5)
b.insert_edge(1, 4)
b.insert_edge(2, 3)
b.insert_edge(2, 4)
b.insert_edge(2, 1)
b.insert_edge(3, 4)
b.insert_edge(4, 2)
b.insert_edge(4, 5)
print('Edges:')
b.edges()
print(b.vertex_count())
print(b.edge_count())
print(b.display_adjMat())
print('BFS:')
b.BFS(0)

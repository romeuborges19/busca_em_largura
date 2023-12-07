import numpy as np
from numpy.linalg import matrix_power

def get_adjency_matrix(graph):
    adjency_matrix = []

    row = []
    for char in graph:
        if char in ['1', '0']:
            row.append(char)

        if char == '\n':
            adjency_matrix.append(row)
            row = []

    adjency_matrix.append(row)

    return adjency_matrix
 
def is_connected(adjacency_matrix, num_vertex):
    aux = []
    for i in range(num_vertex):
        row = []
        for j in range(num_vertex):
            row.append(int(adjacency_matrix[i][j]))
        row[i] = 1
        aux.append(row)

    A = np.array(aux) 
    A = matrix_power(A, num_vertex)

    connected = 'NÃO'
    for row in A:
        if 0 not in row:
            connected = 'SIM'

    return connected

def is_bipartite(graph):
    for edge in graph.edge_set:
        if edge.edge_type == "ai" or edge.edge_type == "ap":
            print(f'Não é bipartido! aresta ({edge.v1.index}, {edge.v2.index}) é AI ou AT')
            return False
    print('É bipartido')
    return True

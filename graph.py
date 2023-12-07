class Graph:
    def __init__(self, matrix):
        # Cria uma lista de adjacência para armazenar o grafo
        self.adjency_list = self.get_adjency_list(matrix)
        self.edge_set = self.get_edge_set()
        self.vertex_set = list(range(0, 10))

    def get_adjency_list(self, matrix):
        adjency_list = []

        for line in matrix:
            vertex_index = matrix.index(line)
            current_vertex = Vertex(vertex_index) # Salva o vértice atual, rotulando-o pelo índice

            index = 0
            for vertex in line:
                if vertex == '1':
                    # Se ha adjacência, o vértice adjacente é adicionado à lista de adjacência do vértice atual
                    current_vertex.adjency.append(index)

                index += 1

            adjency_list.append(current_vertex)

        return adjency_list

    def print_adjency_list(self):
        for vertex in self.adjency_list:
            print(f"V{vertex.index} = {[adjacent for adjacent in vertex.adjency]}")

    def get_edge_set(self):
        edge_set = []

        for vertex in self.adjency_list:
            for adjacent in vertex.adjency:
                 
                exists = False
                for item in edge_set:
                    if vertex.index in item and adjacent in item:
                        exists = True

                edge = (vertex.index, adjacent)

                if not exists:
                    edge_set.append(edge)

        return edge_set

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

         
class Vertex:
    def __init__(self, index):
        self.index = index
        self.adjency = []

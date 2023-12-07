

class Graph:
    def __init__(self, matrix):
        # Cria uma lista de adjacência para armazenar o grafo
        self.vertex_set = self.get_adjency_list(matrix)
        self.vertex_set_indexes = list(range(0, len(matrix[0])))
        self.edge_set = self.get_edge_set()

    def get_adjency_list(self, matrix):
        adjacency_list = []

        j = 0
        for line in matrix:
            vertex_index = j
            current_vertex = Vertex(vertex_index) # Salva o vértice atual, rotulando-o pelo índice

            index = 0
            for vertex in line:
                if vertex == '1':
                    # Se ha adjacência, o vértice adjacente é adicionado à lista de adjacência do vértice atual
                    current_vertex.adjacency.append(index)

                index += 1

            adjacency_list.append(current_vertex)
            j += 1

        self.vertex_set = adjacency_list

        for vertex in adjacency_list:
            for i in range(len(vertex.adjacency)):
                neighbor = self.get_vertex(vertex.adjacency[i])
                vertex.adjacency[i] = neighbor

        return adjacency_list

    def get_vertex(self, key):
        for vertex in self.vertex_set:
            if vertex.index == key:
                return vertex
        
        return None

    def print_adjency_list(self):
        for vertex in self.vertex_set:
            print(f"V{vertex.index} = {[adjacent.index for adjacent in vertex.adjacency]}")

    def get_edge_set(self):
        edge_set = []

        for vertex in self.vertex_set:
            for adjacent in vertex.adjacency:
                 
                exists = False

                for item in edge_set:
                    item = (item.v1, item.v2)
                    if vertex in item and adjacent in item:
                        exists = True

                if not exists:
                    edge = Edge(vertex, adjacent)
                    edge_set.append(edge)


        self.edge_set_literal = []
        for edge in edge_set:
            aux = (edge.v1.index, edge.v2.index)
            self.edge_set_literal.append(aux)

        return edge_set

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.visited = False

    def visit(self):
        self.visited = True

    def set_type(self):
        # aa = aresta de árvore
        # ai = aresta irmão
        # at = aresta tio
        # ap = aresta primo

        if self.v1.parent == self.v2 or self.v2.parent == self.v1:
            self.edge_type = "aa"
        else:
            if self.v1.level() == self.v2.level():
                if self.v1.parent != self.v2.parent:
                    self.edge_type = "ap"
                else: self.edge_type = "ai" 
            elif self.v1.level() == (self.v2.level()-1) or (self.v1.level()-1) == self.v2.level():
                self.edge_type = "at"
         
class Vertex:
    def __init__(self, index):
        self.index = index
        self.adjacency = []
        self.marked = False
        self.parent = None

    def mark(self):
        self.marked = True

    def level(self):
        level = 1
        current = self

        while current.parent != None:
            current = current.parent
            level += 1

        return level

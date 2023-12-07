from utils import is_connected


class BFS:
    def __init__(self, graph):
        self.bsf_vertex_set = graph.vertex_set
        self.bsf_edge_set = graph.edge_set 
        self.queue = []
        self.marked = []

    def get_edge(self, v1, v2):
        for edge in self.bsf_edge_set:
            if edge.v1 == v1 and edge.v2 == v2:
                return edge
            elif edge.v2 == v1 and edge.v1 == v2:
                return edge

    # def breadth_first_search(self, root):
    #     components = []
    #     component = []
    #     current = self.bsf_vertex_set[root]
    #     self.queue.append(current)

    #     while self.queue:
    #         current = self.queue[0]
    #         self.marked.append(current)
    #         component.append(current)
    #         current.mark()
    #         print(f'fila: {[i.index for i in self.queue]}]')

    #         for adjacent in current.adjacency:
    #             if not adjacent.marked:
    #                 edge = self.get_edge(current, adjacent)
    #                 edge.visit()

    #                 adjacent.mark()
    #                 adjacent.parent = current

    #                 self.queue.append(adjacent)
    #                 print(f'fila: {[i.index for i in self.queue]}]')                
    #             else: 
    #                 if adjacent in self.queue:
    #                     edge = self.get_edge(current, adjacent)
    #                     edge.visit()

            
    #         self.queue.pop(0)

    #     components.append(component)
    #     print(f'fila: {[i.index for i in self.queue]}')
    #     print(f'fila: {[i.index for i in self.marked]}')

    def bfs(self, root):
        component = []
        current = self.bsf_vertex_set[root]
        self.queue.append(current)

        while self.queue:
            current = self.queue[0]
            self.marked.append(current)
            component.append(current)
            current.mark()

            for adjacent in current.adjacency:
                if not adjacent.marked:
                    edge = self.get_edge(current, adjacent)
                    edge.visit()

                    adjacent.mark()
                    adjacent.parent = current

                    self.queue.append(adjacent)
                else: 
                    if adjacent in self.queue:
                        edge = self.get_edge(current, adjacent)
                        edge.visit()
            self.queue.pop(0)

        return component

    def perform_bfs(self, root):
        components = []

        component = self.bfs(root)
        components.append(component)

        for vertex in self.bsf_vertex_set:
            if vertex not in self.marked:
                component = self.bfs(vertex.index)
                components.append(component)
        
        self.components = components

    def print_components(self):
        print('Componentes conexas: ')
        i = 1
        for component in self.components:
            print(f'C{i}: [', end=" ")
            for vertex in component:
                print(f'{vertex.index}', end=" ")
            print(']\n')
            i += 1

    def get_edge_types(self):
        for edge in self.bsf_edge_set:
            edge.set_type()


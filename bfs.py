class BFS:
    def __init__(self, graph):
        self.bsf_vertex_set = graph.vertex_set
        self.bsf_edge_set = graph.edge_set 
        self.queue = []

    def get_edge(self, v1, v2):
        for edge in self.bsf_edge_set:
            if edge.v1 == v1 and edge.v2 == v2:
                return edge
            elif edge.v2 == v1 and edge.v1 == v2:
                return edge

    def breadth_first_search(self, root):
        current = self.bsf_vertex_set[root]
        self.queue.append(current)

        while self.queue:
            current = self.queue[0]
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

    def get_edge_types(self):
        for edge in self.bsf_edge_set:
            edge.set_type()


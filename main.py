from bfs import *
from utils import *
import networkx as nx
from graph import *
import matplotlib.pyplot as plt

def main():
    graphs = open('grafo.txt')     

    graphs = graphs.read()

    graphs = graphs.split('\n\n')

    selected_graph = int(input("Insira o número da matriz você deseja manipular: "))
    selected_graph = selected_graph - 1

    print(f'Grafo selecionado: \n{graphs[selected_graph]}')

    adjency_matrix = get_adjency_matrix(graphs[selected_graph])

    for line in adjency_matrix:
        print(line)

    resulted_graph = Graph(adjency_matrix)
    print(resulted_graph.print_adjency_list())
    bfs = BFS(resulted_graph)
    bfs.breadth_first_search(0)
    bfs.get_edge_types()

    for edge in bfs.bsf_edge_set:
        print(f'Aresta ({edge.v1.index}, {edge.v2.index}), tipo {edge.edge_type}')

    # Plotando o grafo
    G = nx.Graph()

    G.add_nodes_from(resulted_graph.vertex_set_indexes)
    G.add_edges_from(resulted_graph.edge_set_literal)

    nx.draw(G, with_labels=True)
    plt.savefig("graph.png") 

if __name__=='__main__':
    main()

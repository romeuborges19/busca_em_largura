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
    print(resulted_graph.edge_set)
    print(resulted_graph.vertex_set)

    G = nx.Graph()

    G.add_nodes_from(resulted_graph.vertex_set)
    G.add_edges_from(resulted_graph.edge_set)

    nx.draw(G, with_labels=True)
    plt.savefig("graph.png") 
    



if __name__=='__main__':
    main()

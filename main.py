from bfs import *
from utils import *
import networkx as nx
from graph import *
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power

def main():
    # Lê o arquivo de grafos
    graphs = open('grafo.txt')     
    graphs = graphs.read()
    graphs = graphs.split('\n\n')

    # O usuário seleciona o grafo
    selected_graph = int(input("Insira o número da matriz você deseja manipular: "))
    selected_graph = selected_graph - 1

    print(f'Grafo selecionado: \n{graphs[selected_graph]}')

    # Gera matriz de adjacência
    adjacency_matrix = get_adjency_matrix(graphs[selected_graph])

    for line in adjacency_matrix:
        print(line)

    # Gera o grafo (lista de adjacências)
    resulted_graph = Graph(adjacency_matrix)

    # Pré-processa a busca em largura com raiz 0 por padrão
    bfs = BFS(resulted_graph)
    bfs.perform_bfs(0)

    # Plotando o grafo
    G = nx.Graph()

    G.add_nodes_from(resulted_graph.vertex_set_indexes)
    G.add_edges_from(resulted_graph.edge_set_literal)

    nx.draw(G, with_labels=True)
    plt.savefig("graph.png") 

    option = '1'
    while(option in ['1', '2', '3']):
        option = input('\nDigite a opção desejada:\n1 - Verificar se grafo é conexo\n2 - Aplicar busca em largura\n3 - Encontrar bipartição\n4 - Sair\n -- > ')

        if(option == '1'):
            num_vertex = len(adjacency_matrix[0])
            print(is_connected(adjacency_matrix, num_vertex))

            bfs.print_components()

        if(option == '2'):
            root = int(input(f'Qual será o vértice raiz da busca?\nVértices candidatos: {[i for i in range(len(adjacency_matrix[0]))]}\n -- > '))
            bfs = BFS(resulted_graph)

            bfs.perform_bfs(root)
            bfs.get_edge_types()

            for edge in bfs.bsf_edge_set:
                print(f'Aresta ({edge.v1.index}, {edge.v2.index}) - {edge.edge_type}')

        if(option == '3'):
            # TODO: Encontrar bipartições
            is_bipartite(resulted_graph)
                 
if __name__=='__main__':
    main()

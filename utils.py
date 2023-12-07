def get_adjency_matrix(selected_graph):
    adjency_matrix = []

    row = []
    for char in selected_graph:
        if char in ['1', '0']:
            row.append(char)

        if char == '\n':
            adjency_matrix.append(row)
            row = []

    adjency_matrix.append(row)

    return adjency_matrix
 

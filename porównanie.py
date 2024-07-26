import os
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from Algorytm_mrowkowy import solve as ant_colony_solve

def read_edge_list(file_path):
    edges = []
    with open(file_path, 'r') as file:
        line = file.readline()
        while line.strip() == '':
            line = file.readline()
        num_vertices = int(line)
        for line in file:
            vertices = list(map(int, line.split()))
            for i in range(1, len(vertices)):
                edges.append((vertices[0], vertices[i]))
    return edges, num_vertices

directory = 'GC_ANT'
graph_files = sorted([f for f in os.listdir(directory) if f.endswith('.txt')])
optimal_solutions = [11,9,13,11,10,31,5,8,9,30]  # The optimal solutions list

ant_colony_colors = []
for graph_file in graph_files:
    edges, num_vertices = read_edge_list(os.path.join(directory, graph_file))
    graph = nx.Graph()
    graph.add_edges_from(edges)
    num_colors_ant, _, _ = ant_colony_solve(graph)
    ant_colony_colors.append(num_colors_ant)

# Calculate the relative errors for the ant colony algorithm in percentage
ant_colony_errors = [(ant - opt) / opt * 100 for ant, opt in zip(ant_colony_colors, optimal_solutions)]

fig, ax = plt.subplots()
ax.bar(graph_files, ant_colony_errors, label='Ant Colony')
ax.set_ylabel('Relative Error %')
ax.set_title('Comparison of Ant Colony algorithm with Optimal Solution')
ax.set_xticks(range(len(graph_files)))
ax.set_xticklabels(graph_files, rotation=45)
ax.legend()
fig.tight_layout()
plt.show()
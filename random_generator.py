import os
import random
import networkx as nx

def generate_random_graphs(num_graphs=15, min_nodes=6, max_nodes=250, p=0.5, directory='GC_ANT'):
    # Print the current working directory
    print(f"Current working directory: {os.getcwd()}")

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist, creating it.")
        os.makedirs(directory)
    else:
        print(f"Directory {directory} already exists.")

    for i in range(num_graphs):
        # Generate a random number of nodes
        num_nodes = random.randint(min_nodes, max_nodes)

        # Generate a random graph
        G = nx.gnp_random_graph(num_nodes, p)

        # Define the file path
        file_path = os.path.join(directory, f'graph{i}.txt')

        # Write the graph to a file in the specified format
        with open(file_path, 'w') as f:
            # Write the number of vertices on the first line
            f.write(f'{G.number_of_nodes()}\n')

            # Write the vertices and their connections on the subsequent lines
            for node in G.nodes:
                connections = ' '.join(map(str, G.neighbors(node)))
                f.write(f'{node} {connections}\n')

        # Print a message indicating that the file has been created
        print(f'Graph {i} written to {file_path}')
generate_random_graphs()
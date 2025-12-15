from collections import deque
import sys
import networkx as nx
import matplotlib.pyplot as plt


def main():
    city_graph = create_graph(get_stops(), get_roads())
    
    show_graph_info(city_graph)
    print('DFS Traversal:')
    dfs(city_graph, "Park")
    print(f"\n {"-" * 100}")
    print('BFS Traversal:', flush=True)
    bfs(city_graph, deque(["Park"]))
    sys.stdout.flush()

    show_graph(city_graph)
  

def create_graph(stops, roads):
    G = nx.Graph()
    G.add_edges_from(roads)
    G.add_nodes_from(stops)
    return G


def show_graph(graph: nx.Graph):
    plt.figure(figsize=(10, 8))
    plt.title("Transportation Network of a Small City", color="blue")

    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=10,
        font_color="blue")
    plt.show()


def show_graph_info(graph: nx.Graph):
    # Number of nodes and edges
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()

    print(f"Number of nodes (stops): {num_nodes}")
    print(f"Number of edges (routes/roads): {num_edges}")

    # Degree of each node
    degrees = dict(graph.degree())
    print("\nNode degrees:")
    for node, deg in degrees.items():
        print(f"  {node}: {deg}")

    # Average node degree
    avg_degree = sum(degrees.values()) / num_nodes
    print(f"\nAverage node degree: {avg_degree:.2f}")


def dfs(graph: nx.Graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' -> ')
    for neighbor in graph.neighbors(vertex):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph: nx.Graph, queue: deque, visited=None):
    if visited is None:
        visited = set()

    if not queue:
            return
    
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=' -> ')
        visited.add(vertex)
   
    neigbors = set(graph.neighbors(vertex))
    queue.extend(neigbors - visited)
    
    bfs(graph, queue, visited)
   

def get_stops():
    return [
        "City Center",
        "Train Station",
        "University",
        "Shopping Mall",
        "Residential Area",
        "Park",
        "Hospital",
        "Old Town"
    ]


def get_roads():
    return[
        ("City Center", "Train Station"),
        ("City Center", "University"),
        ("Train Station", "University"),

        ("University", "Park"),
        ("Park", "Residential Area"),
        ("Residential Area", "University"),

        ("City Center", "Shopping Mall"),
        ("Shopping Mall", "Residential Area"),
        ("Shopping Mall", "Old Town"),
        ("Old Town", "City Center"),
        ("Hospital", "University"),
        ("Hospital", "Residential Area")
    ]

# def get_roads():
#     return[
#         ("City Center", "Train Station", 4),
#         ("City Center", "University", 3),
#         ("Train Station", "University", 5),

#         ("University", "Park", 2),
#         ("Park", "Residential Area", 3),
#         ("Residential Area", "University", 4),

#         ("City Center", "Shopping Mall", 5),
#         ("Shopping Mall", "Residential Area", 3),
#         ("Shopping Mall", "Old Town", 4),
#         ("Old Town", "City Center", 2),
#         ("Hospital", "University", 4),
#         ("Hospital", "Residential Area", 5)
#     ]



if __name__ == "__main__":
    main()


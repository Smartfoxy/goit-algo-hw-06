from matplotlib import pyplot as plt
from city_graph import  create_graph, get_roads, get_stops
import networkx as nx



def main():
    city_graph = create_graph(get_stops(), get_roads())
    weights = [4, 3, 5, 2, 7, 5, 3, 6, 1, 2, 2, 4]
    assign_weights_by_order(city_graph, weights)
    dijkstra(city_graph, "Park")
    
    show_graph_with_width(city_graph)


# def create_graph_with_weight(stops, roads):
#     G = nx.Graph()
#     G.add_nodes_from(stops)

#     for a, b, w in roads:
#         G.add_edge(a, b, weight=w)

#     return G


def show_graph_with_width(graph: nx.Graph):
    plt.figure(figsize=(20, 15))
    plt.title("Transportation Network of a Small City", color="blue")

    pos = nx.spring_layout(graph, seed=42, k=1.2)  

    # Draw nodes and edges
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=700,
        node_color="lightblue",
        font_size=12,
        font_color="blue",
        width=1
    )

    # Extract edge weights
    edge_labels = nx.get_edge_attributes(graph, "weight")

    # Draw weight labels
    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=edge_labels,
        font_color="red",
        font_size=10
    )

    plt.show()


def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)
    
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("{:<15} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph: nx.Graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, attrs  in graph[current_vertex].items():
            w = attrs["weight"]
            distance = distances[current_vertex] + w
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
        print_table(distances, visited)

    return distances


def assign_weights_by_order(graph: nx.Graph, weights: list):
    edges = list(graph.edges())
    
    if len(weights) != len(edges):
        raise ValueError(f"Number of weights ({len(weights)}) does not match number of edges ({len(edges)}).")

    for (u, v), w in zip(edges, weights):
        graph[u][v]["weight"] = w

    return graph


if __name__ == "__main__":
    main()
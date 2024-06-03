import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (зупинок транспорту)
stops = ["Stop A", "Stop B", "Stop C", "Stop D", "Stop E", "Stop F"]
G.add_nodes_from(stops)

# Додавання ребер (доріг)
edges = [
    ("Stop A", "Stop B"),
    ("Stop A", "Stop C"),
    ("Stop B", "Stop D"),
    ("Stop C", "Stop D"),
    ("Stop C", "Stop E"),
    ("Stop D", "Stop E"),
    ("Stop D", "Stop F"),
    ("Stop E", "Stop F"),
]
G.add_edges_from(edges)

# Візуалізація
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Transport Network Graph")
plt.show()

# Аналіз
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print(f"Degrees of nodes: {degrees}")

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Пошук шляху з Stop A до Stop F
start, goal = "Stop A", "Stop F"
print("DFS paths:")
dfs_result = list(dfs_paths(G, start, goal))
for path in dfs_result:
    print(path)

print("\nBFS paths:")
bfs_result = list(bfs_paths(G, start, goal))
for path in bfs_result:
    print(path)

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

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degrees}")

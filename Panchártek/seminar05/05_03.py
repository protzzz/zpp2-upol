LABEL = 0
EDGES = 1
VALUE = 2

def add_node(graph, label):
    graph.append([label, [], []])

def add_edge(graph, from_node, to_node, value):
    for node in graph:
        if node[0] == from_node:
            v = node
        elif node[0] == to_node:
            w = node

    v[1].append(w)
    v[2].append(value)
    w[1].append(v)
    w[2].append(value)

graph = []
add_node(graph, "a")
add_node(graph, "b")
add_node(graph, "c")
add_node(graph, "d")

add_edge(graph, "a", "b", 2)
add_edge(graph, "a", "c", 1)
add_edge(graph, "c", "b", 3)
add_edge(graph, "c", "b", 10)

print(graph)
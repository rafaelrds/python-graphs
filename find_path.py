from graphs import Graph

g = {"a": ["d"],
     "b": ["c"],
     "c": ["b", "c", "d", "e"],
     "d": ["a", "c"],
     "e": ["c"],
     "f": ["g"],
     "g": []
     }


graph = Graph(g)

# print("Vertices of graph:")
# print(graph.vertices())

# print("Edges of graph:")
# print(graph.edges())


# print('The path from vertex "a" to vertex "b":')
path = graph.find_path("a", "b")
assert path == ['a', 'd', 'c', 'b']
assert graph.path_exists("a", "b") == True
# print(path)

# print('The path from vertex "a" to vertex "f":')
path = graph.find_path("a", "f")
path == None
assert graph.path_exists("a", "f") == False
# print(path)

# print('The path from vertex "c" to vertex "c":')
path = graph.find_path("c", "c")
assert path == ["c"]
assert graph.path_exists("c", "c") == True
# print(path)

assert graph.path_exists("f", "g") == True
assert graph.path_exists("g", "f") == False
assert graph.path_exists("f", "a") == False

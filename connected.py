from graphs import Graph

g = {"a": ["d"],
     "b": ["c"],
     "c": ["b", "c", "d", "e"],
     "d": ["a", "c"],
     "e": ["c"],
     "f": ["g"],
     "g": []
     }

graph = Graph(graph_dict=g)

g2 = {"a": ["d"],
     "b": ["c"],
     "c": ["b", "c", "d", "e"],
     "d": ["a", "c"],
     "e": ["c"],
     }
graph2 = Graph(graph_dict=g2)

g3 = {"a": ["d", "g"],
     "b": ["c"],
     "c": ["b", "c", "d", "e", "f"],
     "d": ["a", "c"],
     "e": ["c"],
     "f": ["c"],
     "g": ["a", "k", "j"],
     "k": [],
     "j": ["k"]
     }

graph3 = Graph(graph_dict=g3)

assert not graph.is_connected()
assert graph2.is_connected()
assert graph3.is_connected()

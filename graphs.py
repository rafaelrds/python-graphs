""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.
"""


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that an edge is of type {set, tuple or list};
            between two vertices there can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def path_exists(self, start_vertex, end_vertex, visited=None):
        graph = self.__graph_dict

        if visited is None:
            visited = []
        
        visited.append(start_vertex)
        
        if start_vertex == end_vertex:
            return True

        if start_vertex not in graph:
            return False

        for vertex in graph[start_vertex]:
            if vertex not in visited:
                return self.path_exists(vertex, end_vertex, visited=visited)
        return False


    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        # If running for the first time, create an empty path list
        if path is None:
            path = []
        graph = self.__graph_dict
        # Concat path (list) with current vertex (start)
        path = path + [start_vertex]

        # If start_vertex = end_vertex the path was found
        if start_vertex == end_vertex:
            return path

        # If start vertex do not exist, the path cannot be found
        if start_vertex not in graph:
            return None

        # Check for neighbours of starting vertex
        for vertex in graph[start_vertex]:
            # Our path dont allow the same vertex twice
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)

                # If something Truty returns from find_path, return it
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """find all paths from start_vertex to
        end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def is_connected(self):
        s = self.vertices()[0]
        
        visitable_nodes = self._visitableNodes(s, visited=[])
        total_vertices = self.vertices()
        
        return len(visitable_nodes) == len(total_vertices)
    

    def _visitableNodes(self, start_vertex, visited):
        graph = self.__graph_dict
        
        if start_vertex in visited:
            return visited

        visited.append(start_vertex)
        print (visited)
        
        for neighbour in graph[start_vertex]:
            if neighbour not in visited:
                self._visitableNodes(neighbour, visited)
        return visited


if __name__ == "__main__":

    g = {
        "a": ["d"],
        "b": ["c"],
        "c": ["b", "c", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": []
    }

    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    vertex = "z"
    print("Add vertex: {}".format(vertex))
    graph.add_vertex(vertex)

    print("Vertices of graph:")
    print(graph.vertices())

    edge = {"a", "z"}
    print("Add an edge: {}".format(edge))
    graph.add_edge(edge)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x", "y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())

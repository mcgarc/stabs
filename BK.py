"""
Module for the BKgraph class, which will find maximal cliques in a graph
"""

class BKgraph:
    """
    Class for finding maximal cliques in a graph using the BK algo
    https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    Takes a graph in the form of a dictionary, whose keys are the vertices are
    lists of the neighbours
    """

    def __init__(self, graph):
        self._graph = graph
        self._output = []
        self.run()

    def _BK(self, R, P, X):
        """
        Recursive function for 
        """
        if len(P) == 0 and len(X) == 0:
            self._output.append(R)
            return None
        for _ in range(len(P)):
            vertex = P.pop()
            new_R = R.copy()
            new_R.add(vertex)
            new_P = P.intersection(set(self._graph[vertex]))
            new_X = X.intersection(set(self._graph[vertex]))
            self._BK(new_R, new_P, new_X)
            X.add(vertex)

    def run(self):
        """
        Recursively call the algorithm
        """
        R = set()
        P = set(self._graph.keys())
        X = set()
        self._BK(R, P, X)

    def printer(self):
        """
        Print the output line by line
        """
        print(self._output)
        for _ in self._output:
            print(_)

    def output_strs(self):
        return [ ' '.join(_) for _ in self._output ]


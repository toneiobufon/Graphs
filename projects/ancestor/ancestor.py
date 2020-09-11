from graph import Graph
from util import Queue




def earliest_ancestor(ancestors, starting_node):
    anagraph = Graph()

    for tup in ancestors:
        if tup[0] not in anagraph.vertices:
            anagraph.add_vertex(tup[0])
        if tup[1] not in anagraph.vertices:
            anagraph.add_vertex(tup[1])
    
    for vert in ancestors:
        anagraph.add_edge(vert[1], vert[0])

    if anagraph.vertices[starting_node] == set():
        return -1

    return anagraph.dfs(starting_node)
    


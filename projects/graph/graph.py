"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # if vertex_id in self.vertices:
        #     self.vertices[vertex_id]
        # return None

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        #create a queue to hold nodes to visit
        to_visit = Queue()

        #create a set to hold visited nodes
        visited = set()

        #inisiatlize: add the starting node to the queue
        to_visit.enqueue(starting_vertex)

        #as long as queue is not empty
        while to_visit.size() > 0:
            #get first/head of queue
            cur = to_visit.dequeue()

            # add to visited nodes 
            visited.add(cur)

            #print it 
            print(cur)

            #to get its neighbors, if they have been added to the to_visit list, add them
            neighbors = self.get_neighbors(cur)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    to_visit.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()

        visited.add(starting_vertex)
        stack.push(starting_vertex)

        while stack.size()>0:
            cur = stack.pop()
            visited.add(cur)
            print(cur)

            neighbors = self.get_neighbors(cur)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def dft_visited(vertex):
            visited.add(vertex)
            print(vertex)
            
            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    dft_visited(neighbor)
        dft_visited(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        visited = set()

        #here queue will hold the path
        paths = Queue()

        paths.enqueue([starting_vertex])

        while paths:
            curr_path = paths.dequeue()

            curr_vertex = curr_path[-1]

            if curr_vertex not in visited:
                neighbors = self.get_neighbors(curr_vertex)

                for neighbor in neighbors:
                    new_path = list(curr_path)
                    new_path.append(neighbor)
                    paths.enqueue(new_path)

                    if neighbor == destination_vertex:
                        return new_path

                visited.add(curr_vertex)
        #when there is no path between two vertices
        return None



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        paths = Stack()

        visited.add(starting_vertex)
        #holding paths
        paths.push([starting_vertex])

        if starting_vertex == destination_vertex:
            return paths

        while paths.size() > 0:
            curr_path = paths.pop()
            curr_node = curr_path[-1]

            visited.add(curr_node)

            neighbors = self.get_neighbors(curr_node)
            for neighbor in neighbors:
                new_path = list(curr_path)
                new_path.append(neighbor)
                if neighbor == destination_vertex:
                    return new_path
                visited.add(neighbor)
                paths.push(new_path)
        return None


    def dfs_recursive(self, starting_vertex, destination_vertex, path = {}, visited ={}):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = set()

        if starting_vertex not in path:
            path = path + starting_vertex

        neighbors = self.get_neighbors(starting_vertex)
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if neighbor not in path:
                    path[neighbor] = path[starting_vertex] + [neighbor]

                    if neighbor == destination_vertex:
                        return path[neighbor]
                    else:
                        create_path = self.dfs_recursive(neighbor, destination_vertex, path)
                        if create_path is not None:
                            return create_path
                

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

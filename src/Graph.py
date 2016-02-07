class Node:
    '''
    A class of Node in the Graph structure. Supports the directed Graph, so 
    keep track of the parents and children of the current node.
    '''

    ##
    # @param name  A string representing the name of the node
    def __init__(self, name):
        self.id = name
        self.parentsList = [] # this node's parent nodes
        self.childrenList = [] # this node's children nodes

    ## overrided string representation about this node
    def __str__(self):
        return str(self.id) + 
            ' parents: ' + str([x.id for x in self.parentsList]) +
            ' children: ' + str([x.id for x in self.childrenList])

    ## add parent node to this node
    # @param parent  Parent node
    def add_parent(self, parent):
        self.parentsList.append(parent)

    ## add child node to this node
    # @param child  Child node
    def add_child(self, child):
        self.childrenList.append(child)

    ## getter func for id
    def get_id(self):
        return self.id


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

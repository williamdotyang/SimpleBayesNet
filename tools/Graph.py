from Node import Node

class Graph:
    '''
    A class representing the Directed Graph structure. 
    '''

    ##
    def __init__(self):
        self.__nodes = {} # dict of Nodes, {string: Node}
        self.__numNodes = 0 # number of Nodes

    def __iter__(self):
        return iter(self.__nodes.values())

    ## add a node to this graph
    # @param name  A string of name of this node
    # @return A new Node object
    def addNode(self, name):
        self.__numNodes += 1
        newNode = Node(name)
        self.__nodes[name] = newNode
        return newNode

    ##
    # @param name  A string of name of a node
    # @return A Node obj if found, None otherwise
    def getNode(self, name):
        if name in self.__nodes:
            return self.__nodes[name]
        else:
            return None

    ##
    # @param frm  Name of node that strat from
    # @param to  Name of node that end to
    # @param weight  Weight of this edge
    # @return true if added, false if failed
    def add_edge(self, frm, to, weight=0):
        if frm not in self.__nodes:
            return False
        if to not in self.__nodes:
            return False

        self.__nodes[frm].addChild(self.__nodes[to], weight)
        self.__nodes[to].addParent(self.__nodes[frm], weight)
        return True

    ## return a list of names of all nodes
    def get_vertices(self):
        return self.__nodes.keys()

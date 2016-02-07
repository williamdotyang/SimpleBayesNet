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

    ## return a list of names of all nodes
    def getNodes(self):
        return self.__nodes.keys()

    ##
    # @param name  A string of name of a node
    # @return A Node obj if found, None otherwise
    def getNode(self, name):
        if name in self.__nodes:
            return self.__nodes[name]
        else:
            return None

    ## add a node to this graph
    # @param name  A string of name of this node
    # @return A new Node object, or None if name collides
    def addNode(self, name):
        if name in self.__nodes:
            return None
        self.__numNodes += 1
        newNode = Node(name)
        self.__nodes[name] = newNode
        return newNode

    ## removed a node in this graph
    # @param name  A string of name of this node
    # @return  The removed node, None if not found
    def removeNode(self, name):
        if name not in self.__nodes:
            return None
        node = self.__nodes[name]
        children = self.__nodes[name].getChildren()
        parents = self.__nodes[name].getParents()
        for c in children:
            c.removeParent(node)
        for p in parents:
            p.removeChild(node)
        del self.__nodes[name]
        self.__numNodes -= 1
        return node

    ##
    # @param frm  Name of node that strat from
    # @param to  Name of node that end to
    # @param weight  Weight of this edge
    # @return true if added, false if failed
    def addEdge(self, frm, to, weight=0):
        if frm not in self.__nodes:
            return False
        if to not in self.__nodes:
            return False
        self.__nodes[frm].addChild(self.__nodes[to], weight)
        self.__nodes[to].addParent(self.__nodes[frm], weight)
        return True

    ## remove an edge
    # @param frm  Name of node that strat from
    # @param to  Name of node that end to
    # @return true if removed, false if failed
    def removeEdge(self, frm, to):
        if frm not in self.__nodes:
            return False
        if to not in self.__nodes:
            return False
        frmNode = self.__nodes[frm]
        toNode = self.__nodes[to]
        frmNode.removeChild(toNode)
        toNode.removeParent(frmNode)
        return True


if __name__ == '__main__':
    # test code
    g = Graph()
    g.addNode('Y')
    g.addNode('X1')
    g.addNode('X2')
    g.addNode('X3')
    g.addEdge('Y', 'X1', 1)
    g.addEdge('Y', 'X2', 2)
    g.addEdge('Y', 'X3', 3)
    g.addEdge('X2', 'X1', 1)
    for n in g:
        print n

    print '---------removing--------\n'
    g.removeEdge('Y', 'X3')
    g.removeNode('X2')
    for n in g:
        print n

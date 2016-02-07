class Node:
    '''
    A class of Node in the Graph structure. Supports the directed Graph, so 
    keep track of the parents and children of the current node. Also supports 
    weighted Graph.
    '''

    ##
    # @param name  A string representing the name of the node
    def __init__(self, name):
        self.__id = name
        self.__parents = {} # this node's parent nodes
        self.__children = {} # this node's children nodes

    ## overrided string representation about this node
    def __str__(self):
        return str(self.__id) + 
            ' parents: ' + str([x.__id for x in self.__parents]) +
            ' children: ' + str([x.__id for x in self.__children])

    ## add parent node to this node
    # @param parent  Parent node
    # @param weight  Weight of edge between this node and parent
    def addParent(self, parent, weight=0):
        self.__parents[parent] = weight

    ## add child node to this node
    # @param child  Child node
    # @param weight Weight of edge between this node and child
    def addChild(self, child, weight=0):
        self.__children[child] = weight

    ## getter func for __id
    def getId(self):
        return self.__id

    ## getter func for __parents
    def getParents(self):
        return self.__parents

    ## getter fucn for __children
    def getChildren(self):
        return self.__children
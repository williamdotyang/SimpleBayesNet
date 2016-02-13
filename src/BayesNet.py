from tools.Data import Data
from tools.Graph import Graph
from tools.Node import Node
from tools.Calculation import *
import Queue as Q

class BayesNet:
    """
    Simple Bayes net model for discrete variables and binary response, supports structure 
    learning and predicting of Naive Bayes and Tree Augmented Net.
    """

    ##
    # train is a Data object representing a training dataset
    # test is a Data object representing a testing dataset
    def __init__(self):
        self.train = None
        self.test = None
        self.graph = Graph()

    ##
    # Load the training dataset.
    # @param trainFilename  A string of filename
    def loadTrain(self, trainFilename):
        self.train = Data(trainFilename)
        self.train.parse()

    ##
    # Load the testing dataset.
    # @param testFilename  A string of filename
    def loadTest(self, testFilename):
        self.test = Data(testFilename)
        self.test.parse()

    ## 
    # Build the graph structure of Naive Bayes
    def buildNaiveBayes(self):
        for name in self.train.names:
            self.graph.addNode(name)
        nodes = self.graph.getNodes()
        for node in nodes:
            if node != 'class':
                self.graph.addEdge('class', node.getId())

    ##
    # Build the graph structure of TAN, using Prim's algo.
    # Every element in priority queue is (score, to_node, frm_node), where
    # score = (-CMI, colIndex(frm), colIndex(to))
    # to_node is current node object
    # frm_node is the parent node which has edge frm_node -> to_node, with score
    def buildTAN(self):
        self.buildNaiveBayes() # first make a Naive Bayes structure
        pri_q = Q.PriorityQueue()
        rootNode  = self.graph.getNode(self.train.names[0]) # first attribute
        pri_q.put( ((0,0,0), rootNode, Node(None)) ) # frm is a dummy node
        visited = set() # a set of visited nodes' names
        while (not pri_q.empty()) and (len(visited) < self.train.names):
            item = pri_q.get() # top element stored in priority queue
            score = item[0]
            currNode = item[1] # current node object
            currName = currNode.getId()
            if currName in visited: continue
            frmNode = item[2] # frm node object
            frmName = frmNode.getId()
            self.graph.addEdge(frmName, currName, score)
            visited.add(currName)
            for attrName in self.train.names:
                if attrName not in visited:
                    CMI = calcCondMI(self.train, currName, attrName, 'class')
                    indexes = self.train.getColIndex([currName, attrName])
                    score = (-CMI, indexes[0], indexes[1])
                    nextNode = self.graph.getNode(attrName)
                    pri_q.put((score, nextNode, currNode))


    ##
    # Given the values of attributes of a testing instance, predict its class.
    # @param instanceVals  A list of instance variable values, including the 'class' at the end.
    # @return [predicted class value, actual class value, posterior prob of predicted value]
    def predictOneInstance(self, instanceVals):
        names = self.train.names # including the 'class'
        posteriors = []
        for y in self.train.variables['class']:
            # give the actual posterior porbability in the output
            true_y = instanceVals[-1]
            Py = calcProb(self.train, ['class'], [y])
            Px = calcProb(self.train, names[:-1], instanceVals[:-1])
            Px_pa = calcProbsCondParents(self.train, names[:-1], instanceVals[:-1] + [y], self.graph)
            #print Py, Px, Px_pa
            pred_p = Py * Px_pa / Px
            posteriors.append([y, true_y, pred_p])
        # normalize the posteriors
        total = sum(x[-1] for x in posteriors)
        posteriors = [x[:2] + [round(x[-1] / total, 12)] for x in posteriors]
        return sorted(posteriors, key = lambda x: -x[-1])[0]

    ##
    # Predict the class in all instances in testing dataset.
    # @return A list of predicted result for instances in testing set.
    def predictTestData(self):
        results = []
        for instance in self.test.data:
            results.append(self.predictOneInstance(instance))
        return results

    ## output the result as homework requirement
    def printResults(self):
        results = self.predictTestData()
        # display structures
        for attr in self.train.names[:-1]:
            node = self.graph.getNode(attr)
            parentNodes = node.getParents()
            parentIndexes = sorted([self.train.getColIndex([p.getId()])[0] \
                                for p in parentNodes])
            parentNames = [self.train.names[i] for i in parentIndexes]
            print attr + ' ' + ' '.join(parentNames)
        print ''
        # display predicts
        corrects = 0
        for r in results:
            if r[0] == r[1]:
                corrects += 1
            print ' '.join([str(x) for x in r])
        print ''
        # display correct predicts
        print str(corrects)

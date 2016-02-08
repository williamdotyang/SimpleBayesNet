from Data import Data
from Graph import Graph
from Calculation import *

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
                self.graph.addEdge('class', node)

    ##
    # Build the graph structure of TAN
    def buildTAN(self):
        pass

    ##
    # Given the values of attributes of a testing instance, predict its class.
    # @param instanceVars  A list of instance variable values, including the 'class' at the end.
    # @return (predicted class value, actual class value, posterior prob of predicted value)
    def predictOneInstance(self, instanceVars):
        names = self.train.names # including the 'class'
        posteriors = []
        for y in self.train.variables[response]:
            # give the actual posterior porbability in the output
            true_y = instanceVars[-1]
            Py = calcProb(self.train, ['class'], [y])
            Px = calcProb(self.train, names[:-1], instanceVars[:-1])
            Pxi_parents = calcProbsCondParents(self.train, instanceVars[:-1])
            Px-y = prod(Pxi_parents)
            pred_p = Py * Px-y / Px
            posteriors.append((y, true_y, pred_p))
        return sorted(posteriors, key = lambda x: -x[-1])[0]

    ##
    # Predict the class in all instances in testing dataset.
    # @return A list of predicted result for instances in testing set.
    def predictTestData(self):
        results = []
        for instance in self.test.data:
            results.append(self.predictOneInstance(instance))
        return results

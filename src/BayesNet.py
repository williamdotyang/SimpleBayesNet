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
        self.graph
        pass

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
    # Given the values of attributes of a testing instance, predict its class.
    # @param x  A list of instance variable values, including the 'class' at the end.
    # @return (predicted class value, actual class value, posterior prob of predicted value)
    def predictOneInstance(self, x):
        names = self.train.names # including the 'class'
        posteriors = []
        for y in self.train.variables['class']:
            # give the actual posterior porbability in the output
            true_y = x[-1]
            pred_p = calcProb(names, x[:-1] + [y]) / calcProb(X = names[:-1], v = x[:-1])
            posteriors.append((y, true_y, pred_p))
        return sorted(posteriors, key = lambda x: -x[-1])[0]


    ##
    # Predict the class in all instances in testing dataset.
    # @return A list of predicted class values for instances in testing set.
    def predictTestData(self):
        results = []
        for instance in self.test.data:
            results.append(self.predictOneInstance(instance))
        return results

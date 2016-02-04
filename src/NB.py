from Data import Data

class NB:
    """Naive Bayes for discrete variables and binary response."""

    ##
    # train is a Data object representing a training dataset
    # test is a Data object representing a testing dataset
    def __init__(self):
        self.train = None
        self.test = None
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
    # @param x  A list of attributes values. No class variable is in x.
    # @return One of the class values
    def predictOneInstance(self, x):


    ##
    # Predict the class in all instances in testing dataset.
    # @return A list of predicted class values for instances in testing set.
    def predictTestData(self):

from __future__ import division
from src.BayesNet import BayesNet
from tools.Data import Data
import random 
from math import floor

##
# from a given dataset, randomly pick n instances in data.
# @param matrix  A data matrix in Data object
# @param n  Number of resamplings
# @return A new data matrix
def sampleSubDataset(matrix, n):
    newMat = []
    for i in range(0, n):
        row = int(floor(random.random() * len(matrix)))
        newMat.append(matrix[row])
    return newMat

##
# Calculate the average accuracy of prediction over a test set with a 
# model trained by a resampling of training set
# @param trainFilename  File name of training set
# @param testFilename  File name of testing set
# @param n  Number of resamplings 
# @param flag  'n' for naive Bayes, 't' for TAN
# @return (n, average Accuracy)
def getAverageAccuracy(trainFilename, testFilename, n, flag):
    model = BayesNet()
    model.loadTrain(trainFilename)
    model.loadTest(testFilename)

    originalTrainMat = model.train.data
    accuracy = []
    for i in range(0, 4):
        newMat = sampleSubDataset(originalTrainMat, n)
        model.train.data = newMat
        if flag == 'n':
            model.buildNaiveBayes()
            print 'naive bayes built'
        else:
            model.buildTAN()
            print 'TAN built'
        results = model.predictTestData()
        total = len(results)
        count = 0
        for r in results:
            if r[0] == r[1]:
                count += 1
        print count / total
        accuracy.append(count / total)

    return (n, sum(accuracy) / len(accuracy))


if __name__ == '__main__':
    ## this script is to produce the learning curve for lymph dataset
    random.seed(20160214)
    print getAverageAccuracy('data/lymph_train.arff', 'data/lymph_test.arff', 25, 'n')
    print getAverageAccuracy('data/lymph_train.arff', 'data/lymph_test.arff', 50, 'n')
    print getAverageAccuracy('data/lymph_train.arff', 'data/lymph_test.arff', 100, 'n')
    print getAverageAccuracy('data/lymph_train.arff', 'data/lymph_test.arff', 25, 't')
    print getAverageAccuracy('data/lymph_train.arff', 'data/lymph_test.arff', 50, 't')
    print getAverageAccuracy('data/lymph_train.arff', 'data/lymph_test.arff', 100, 't')


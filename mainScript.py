from src import BayesNet
import sys

if __name__ == '__main__':
    # test code
    naive = BayesNet.BayesNet()
    naive.loadTrain('data/lymph_train.arff')
    naive.loadTest('data/lymph_test.arff')
    naive.buildNaiveBayes()
    #naive.printResults()

    tan = BayesNet.BayesNet()
    tan.loadTrain('data/lymph_train.arff')
    tan.loadTest('data/lymph_test.arff')
    tan.buildTAN()
    tan.printResults()
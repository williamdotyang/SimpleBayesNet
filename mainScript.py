from src import BayesNet
import sys

if __name__ == '__main__':
    if len(sys.argv) == 0: 
        sys.stderr('trainFile testFile learningMethod')
        sys.exit()

    trainFilename, testFilename, method = sys.argv[1:]

    if method == 'n':
        naive = BayesNet.BayesNet()
        naive.loadTrain(trainFilename)
        naive.loadTest(testFilename)
        naive.buildNaiveBayes()
        naive.printResults()

    if method == 't':
        tan = BayesNet.BayesNet()
        tan.loadTrain(trainFilename)
        tan.loadTest(testFilename)
        tan.buildTAN()
        tan.printResults()
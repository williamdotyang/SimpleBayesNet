from src import BayesNet
import sys

if __name__ == '__main__':
    if len(sys.argv) == 0: 
        sys.stderr('trainFile testFile learningMethod')
        sys.exit()

    trainFilename, testFilename, method = sys.argv[1:]

    model = BayesNet.BayesNet()
    model.loadTrain(trainFilename)
    model.loadTest(testFilename)

    if method == 'n':
        model.buildNaiveBayes()

    if method == 't':
        model.buildTAN()
    
    model.printResults()
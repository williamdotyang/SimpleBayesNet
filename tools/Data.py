class Data:
    """ A class representation of dataset, either training or testing.
        All the variables are discrete, and class variable is binary.
        Provides some basic counting functions of instances.
    """

    ##
    # @param filename  A string of input file name.
    def __init__(self, filename):
        self.filename = filename
        # A list of variable names representing the order [attr1, attr2, ...]
        self.names = []
        # A dictionary of variables {V1:[v11,v12,...], V2:[v21, v22,...], ...}
        self.variables = {} 
        # A matrix representing the instances [[..],[..],...]
        self.data = []

    ##
    # Reads a file and set some fields with data structures for easier access.
    def parse(self):
        for line in open(self.filename):
            line = line.rstrip('\n')
            if line[0] == '%':
                pass
            elif line[0] == '@':
                tokens = line.split(None, 2)
                if tokens[0] == "@attribute":
                    attribute = tokens[1].strip("'")
                    self.names.append(attribute)
                    self.variables[attribute] = tokens[2].strip("{ }").split(', ')
            else: # data lines
                self.data.append(line.split(','))        

    ##
    # Get the number of variables in this data set.
    def getNumNames(self):
        return len(self.names)

    ##
    # Get the number of instances in this data set.
    def getNumInstances(self):
        return len(self.data)

    ##
    # Get the column index(es) of given variables.
    # @param variables  A list of names of variables whose colum indicies are asked
    # @return A list of int
    def getColIndex(self, variables):
        indicies = []
        for var in variables:
            i = 0
            for name in self.names:
                if name == var:
                    indicies.append(i)
                    break
                else:
                    i += 1
        return indicies

    ##
    # Count the number of instances where given set of variables having a 
    # given set of values.
    # @param X  A list of names of selected variables.
    # @param v  A list of values for each of the variables.
    # @return An int, the count of instances in data where X=v.)

    def countInstances(self, X, v):
        cols = self.getColIndex(X)
        count = 0
        for line in self.data:
            x = [line[i] for i in cols]
            if x == v:
                count += 1
        return count


if __name__ == '__main__':
    # test code
    lym_train = Data('../data/lymph_train.arff')
    lym_train.parse()
    print lym_train.filename + ' has ' + str(lym_train.getNumNames()) + ' variables; ' + \
        str(lym_train.getNumInstances()) + ' instances.'
    print 'it has ' + str(lym_train.countInstances(['class'], ['malign_lymph'])) + ' cases of malign_lymph.'

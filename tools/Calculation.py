###
## This is a module providing some intermediate claculation functions, like
## probabilities and mutural information.
###

from __future__ import division
from Data import Data
from math import log


##
# Calculate the product of a list of number
# @param iterable obj
def prod(iterable):
    p= 1
    for n in iterable:
        p *= n
    return p

##
# Calculates the probability of P(X=v) from the training dataset, modified by
# using Laplace estimates with pseudocounts of m.
# @param data  A Data object defined in Data class.
# @param X  A list of variables. Must be discrete.
# @param v  A list of values for each of the variables.
# @param m  Laplace pseudocount
# @return A double, probability of P(X=v)
def calcProb(data, X, v, m = 1):
    numerator = data.countInstances(X, v) + m
    # a list of number of values in each variable in X
    numValues = [len(data.variables[name]) for name in X]
    denominator = data.getNumInstances() + m * prod(numValues)
    return numerator / denominator


##
# Calculates the conditional probability of P(X=v|Y=y), modified by
# using Laplace estimates with pseudocounts of m.
# @param data  A Data object defined in Data class.
# @param X  A list of variables. Must be discrete.
# @param v  A list of values for each of the variables in X.
# @param Y  A list of variables. Must be discrete.
# @param y  A list of values for each of the variables in Y.
# @param m  Laplace pseudocount
# @return A double, probability of P(X=v|Y=y)
def calcCondProb(data, X, v, Y, y, m = 1):
    numerator = data.countInstances(X + Y, v + y) + m
    denominator = data.countInstances(Y, y) + \
        m * sum([len(data.variables[x]) for x in X])
    return numerator / denominator

##
# Calculates the conditional probability of each observed attribute variable given its parent nodes.
# @param data  A Data object defined in Data class.
# @param X  A list of variables. Must be discrete.
# @param x  A list of values for each of the variables in X, and value of Y.
# @param graph  A graph structure describing the dependency relation among variables in X.
# @return Prodcut of P(X_i = x_i | Pa(xi)), for X_i in X
def calcProbsCondParents(data, X, x, graph):
    results = []
    for name in X:
        node = graph.getNode(name)
        parentNodes = node.getParents()
        parentNames = [p.getId() for p in parentNodes]
        parentValues = [x[i] for i in data.getColIndex(parentNames)]
        Xvalue = [x[i] for i in data.getColIndex([name])]
        condProb = calcCondProb(data, [name], Xvalue, parentNames, parentValues)
        #print name, Xvalue, parentNames, parentValues, condProb
        results.append(condProb)
    return prod(results)


## 
# Calculates the conditional mutial information of I(Xi,Xj).
# @param Xi  A name of variable. 
# @param Xj  A name of variable. 
# @param m  Laplace pseudocount
# @return A double, mutual information of I(Xi,Xj)
def calcMI(data, Xi, Xj, m = 1):
    vals_i = data.variables[Xi]
    vals_j = data.variables[Xj]
    MI = 0
    for xi in vals_i:
        for xj in vals_j:
            Pij = calcProb(data, [Xi, Xj], [xi, xj], m)
            Pi = calcProb(data, [Xi], [xi], m)
            Pj = calcProb(data, [Xj], [xj], m)
            MI += Pij * log(Pxy / (Pi * Pj), 2)
    return MI


## 
# Calculates the conditional mutial information of I(Xi,Xj|Y).
# @param Xi  A name of variable. 
# @param Xj  A name of variable. 
# @param Y  A name of variable. 
# @param m  Laplace pseudocount
# @return A double, mutual information of I(Xi,Xj|Y)
def calcCondMI(data, Xi, Xj, Y, m = 1):
    vals_i = data.variables[Xi]
    vals_j = data.variables[Xj]
    vals_y = data.variables[Y]
    MI = 0
    for y in vals_y:
        for xi in vals_i:
            for xj in vals_j:
                Pijy = calcProb(data, [Xi, Xj, Y], [xi, xj, y], m)
                Pij_y = calcCondProb(data, [Xi, Xj], [Y], [xi, xj], [y], m)
                Pi_y = calcCondProb(data, [Xi], [xi], [Y], [y], m)
                Pj_y = calcCondProb(data, [Xj], [xj], [Y], [y], m)
                MI += Pijy * log(Pij_y / (Pi_y * Pj_y), 2)
    return MI
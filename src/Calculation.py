###
## This is a module providing some intermediate claculation functions, like
## probabilities and mutural information.
###

from Data import Data


##
# Calculates the probability of P(X=v) from the training dataset, modified by
# using Laplace estimates with pseudocounts of 1.
# @param data  A Data object defined in Data class.
# @param X  A list of variables. Must be discrete.
# @param v  A list of values for each of the variables.
# @return A double, probability of P(X=v)
def calcProb(data, X, v):


##
# Calculates the conditional probability of P(X=v|Y=y), modified by
# using Laplace estimates with pseudocounts of 1.
# @param data  A Data object defined in Data class.
# @param X  A list of variables. Must be discrete.
# @param v  A list of values for each of the variables in X.
# @param Y  A list of variables. Must be discrete.
# @param y  A list of values for each of the variables in Y.
# @return A double, probability of P(X=v|Y=y)
def calcCondProb(data, X, v, Y, y):


## 
# Calculates the conditional mutial information of I(Xi,Xj).
# @param Xi  A name of variable. 
# @param Xj  A name of variable. 
# @return A double, mutual information of I(Xi,Xj)
def calcMI(data, Xi, Xj):


## 
# Calculates the conditional mutial information of I(Xi,Xj|Y).
# @param Xi  A name of variable. 
# @param Xj  A name of variable. 
# @param Y  A name of variable. 
# @return A double, mutual information of I(Xi,Xj|Y)
def calcCondMI(data, Xi, Xj, Y):

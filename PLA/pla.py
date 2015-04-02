# -*- coding: utf-8 -*-
"""
DATA: pla_train.dat
Question 15:
    implement a version of PLA by visiting examples in the naive cycle using the order of example in
the data set. Run the algorithm on the data set. What is the number of updates before the algorithm
halts?

Question 16:
    Implement a version of PLA by visiting examples in fixed, pre-determined random cycles throughout
the algorithm. Run the algorithm on the data set. Please repeat your experiment for 2000times, each
with a different random seed. What is the average number of updates before the algorithm halts?

Question 17:
    Implement a version of PLA by visiting examples in fixed, pre-determined random cycles throughout
the algorithm, while changing the update rule to be:
    wt+1 = wt +alpha*yn(t)xn(t)
with alpha = 0.5. Note that your PLA in the previous Question corresponds to alpha = 1.
Please repeat your experiment for 2000 times, each with a different random seed. What is the average
number of updates before the algorithm halts?
"""

import random
from numpy import array, inner, zeros

DATA_FILE = 'pla_train.dat'

sign = lambda x: 1 if x > 0 else -1


def load_data(infile):
    X = []
    Y = []
    with open(infile) as f:
        for line in f:
            recs = line.split()
            x = [1] + [float(v) for v in recs[:-1]]  # remember that we have a [−threshold*w0]!
            X.append(tuple(x))
            Y.append(int(recs[-1]))
        return array(X), array(Y)


def train(X, Y, rand=False, alpha=1):
    n = len(Y)
    d = len(X[0])
    W = zeros(d)

    idx = range(n)
    if rand:
        idx = random.sample(idx, n)
    t = 0
    k = 0
    flag = True
    while True:
        if k == n:
            if flag: break
            k = 0
            flag = True

        i = idx[k]
        if sign(inner(X[i], W)) != Y[i]:
            flag = False
            t += 1
            W = W + alpha*Y[i]*X[i]
        k += 1
    return t


def naive_cycle():
    X, Y = load_data(DATA_FILE)
    t = train(X, Y)
    print t


def predefined_random(n, alpha=1):
    X, Y = load_data(DATA_FILE)
    count = 0
    for i in xrange(n):
        #print i
        t = train(X, Y, rand=True, alpha=alpha)
        count += t
    print count/n


def main():
    predefined_random(2000, alpha=0.5)


if __name__ == '__main__':
    print 'for Question 15'
    naive_cycle()
    print '\n' + 'for Question 16'
    predefined_random(2000)
    print '\n' + 'for Question 17'
    main()

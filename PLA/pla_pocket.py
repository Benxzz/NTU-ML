# -*- coding: utf-8 -*-
"""
DATA: pla_train.dat
Question 18:
    as the test set for ``verifying'' the g returned by your algorithm (see lecture 4 about verifying).
The sets are of the same format as the previous one.Run the pocket algorithm with a total of 50 updates
on D, and verify the performance of wPOCKET using the test set. Please repeat your experiment for 2000
times, each with a different random seed. What is the average error rate on the test set?

Question 19:
    Modify your algorithm in Question 18 to return w50 (the PLA vector after 50 updates) instead of
w^ (the pocket vector) after 50 updates. Run the modified algorithm on D, and verify the performance
using the test set. Please repeat your experiment for 2000 times, each with a different random seed.
What is the average error rate on the test set?

Question 20:
    Modify your algorithm in Question 18 to run for 100 updates instead of 50, and verify the performance
of wPOCKET using the test set. Please repeat your experiment for 2000 times, each with a different random
seed. What is the average error rate on the test set?
"""

import random
from numpy import array, inner, zeros

DATA_FILE = 'Fhw1_18_train.dat'
TEST_FILE = 'Fhw1_18_test.dat'

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


def test(W, XT, YT):
    amount = len(YT)
    error = sum([1 for i in range(amount) if sign(inner(XT[i], W)) != YT[i]])
    return (error*1.0)/amount


def train(X, Y, updates=50, pocket=True):
    d = len(X[0])
    W = zeros(d)
    WP = W
    error = test(WP, X, Y)
    t = 0
    #idx = random.sample(range(len(Y)), len(Y)) 此句不可放在这里，放在这里的话每次update之后训练的都将是同一数据集！
    while t <= updates:
        idx = random.sample(range(len(Y)), len(Y))
        for i in idx:
            if sign(inner(X[i], W)) != Y[i]:
                t += 1
                W = W + Y[i]*X[i]
                e = test(W, X, Y)
                if e < error:
                    error = e
                    WP = W
                break
    if pocket:
        return WP
    else:
        return W


def main1():
    error = 0
    X, Y = load_data(DATA_FILE)
    XT, YT = load_data(TEST_FILE)
    for i in range(500):
        W = train(X, Y)
        error += test(W, XT, YT)
        print i
    print (error*1.0)/500


def main2():
    error = 0
    X, Y = load_data(DATA_FILE)
    XT, YT = load_data(TEST_FILE)
    for i in range(500):
        W = train(X, Y, pocket=False)
        error += test(W, XT, YT)
        print i
    print (error*1.0)/500


def main3():
    error = 0
    X, Y = load_data(DATA_FILE)
    XT, YT = load_data(TEST_FILE)
    for i in range(500):
        W = train(X, Y, updates=100)
        error += test(W, XT, YT)
        print i
    print (error*1.0)/500

if __name__ == '__main__':
    main1() #for question 18
    main2() #for question 19
    main3() #for question 20


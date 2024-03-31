import numpy as np


def gardient_descent(x,y):

    m_curr = b_curr = 0
    iterations = 100
    n = len(x)
    learning_rate = 0.01

    for i in range(iterations):
        yp = m_curr * x + b_curr #predict slope

        cost = (1/n) * sum([val ** 2 for val in(y-yp)]) # delta findout / Mean Squared Error
        md = -(2/n) * sum(x*(y-yp))
        bd = -(2/n) * sum(y-yp)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        print("m {}, b {}, cost {} iteration {}".format(m_curr, b_curr, cost, i))

    pass



x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])



gardient_descent(x,y)
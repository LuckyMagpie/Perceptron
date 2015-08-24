from math import exp
from random import uniform

vector_x = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)]

def train(vector_x):
    vector_w = [uniform(0, 1) for f in xrange(2)]
    while True:
        E1 = error_function(vector_w, vector_x)
        new_vector_w = [uniform(0, 1) for f in xrange(2)]
        E2 = error_function(new_vector_w, vector_x)
        if E2 < E1:
            vector_w = new_vector_w
        else:
            break
    return vector_w

def error_function(vector_w, vector_x):
    error = 0
    for input_data, output in vector_x:
        error += (sigmoidal(sum_product(input_data, vector_w)) - output)**2
    return error

def sum_product(vector_x, vector_w):
    return sum(x * w for x, w in zip(vector_w, vector_x))

def sigmoidal(z):
    return (1 / (1 + exp(-z)))

def test_one_PU(vector_w, vector_x):
    print 'Test with one processing unit'
    for input_data, output in vector_x:
        print str(input_data) + ' ->  '+ str(sigmoidal(sum_product(input_data, vector_w)) > 0.5)

vector_w = train(vector_x)
test_one_PU(vector_w, vector_x)

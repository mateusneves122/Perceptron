import numpy as np

class Perceptron(object):

    def __init__(self, no_of_inputs):
        self.weights = np.zeros(no_of_inputs + 1)


    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:] + [0])

        if summation > 0:
            activiation = summation
        else:
            activiation = 0

        return activiation

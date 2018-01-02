from numpy import mat, shape, ones
from numpy.ma import exp


def sigmoid(x):
    return 1.0 / (1 + exp(-x))


def gradient_ascent(matrix, labels):
    data_matrix = mat(matrix)
    label_matrix = mat(labels).transpose()
    m, n = shape(data_matrix)
    alfa, max_cycles, weights = 0.001, 500, ones((n, 1))
    for i in range(max_cycles):
        h = sigmoid(data_matrix * weights)
        error = label_matrix - h
        weights = weights + alfa * data_matrix.transpose() * error
    return weights


tokens = [x.strip().split() for x in open('data/testSet.txt').readlines()]
data = [[float(y) for y in x] for x in tokens]
matrix = [[1.0] + x[:2] for x in data]
labels = [int(x[-1]) for x in data]
# print(matrix)
# print(labels)
# ascent = gradient_ascent(matrix,labels)
print(gradient_ascent(matrix, labels))

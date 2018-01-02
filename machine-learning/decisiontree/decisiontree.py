import json
from math import log

'''
Decision tree is a classification algorithm. The input is a set of data with 
multiple attributes or features and the values of the features should be 
bound and discrete. Each data point should carry the same set of features and
a class label associated with it. This set is used for training the algorithm
and we can obtain a visual representation of the decision tree. Then unknown
data can be classified.

Decision trees are much like flowchart. 
Entropy is a measure of degree of disorder. 
'''


def entropy(data):
    size = len(data)
    labels = [x[-1] for x in data]
    counts = {x: labels.count(x) for x in set(labels)}
    probabilities = [float(counts[x] / size) for x in counts]
    return sum([abs(x * log(x, 2)) for x in probabilities])


def select(data, col, val):
    return [x[:col] + x[col + 1:] for x in data if x[col] == val]


def entropy_on_split(data, col):
    size = len(data)
    uniq_vals = set(x[col] for x in data)
    split_entropy = 0
    for v in uniq_vals:
        subset = select(data, col, v)
        probability = float(len(subset)) / size
        split_entropy += probability * entropy(subset)
    return split_entropy


def choose_feature_to_split(data):
    base_entropy = entropy(data)
    no_of_features = len(data[0]) - 1
    features_info_gain = {}
    for f in range(no_of_features):
        split_entropy = entropy_on_split(data, f)
        info_gain = base_entropy - split_entropy
        features_info_gain[info_gain] = f
    return features_info_gain[max(features_info_gain)]


def majority(labels):
    counts = {x: labels.count(x) for x in set(labels)}
    invert = {y: x for x, y in counts.items()}
    return invert[max(invert)]


def decision_tree(data, features):
    labels = [x[-1] for x in data]
    if len(set(labels)) == 1:
        return labels[0]
    if len(data[0]) == 1:
        return majority([x[0] for x in data])
    feature = choose_feature_to_split(data)
    feature_name = features[feature]
    tree = {feature_name: {}}
    features.remove(feature_name)
    for v in set([x[feature] for x in data]):
        features_copy = features[:]
        tree[feature_name][v] = decision_tree(select(data, feature, v), features_copy)
    return tree


data = [[1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']]
print(entropy(data))
print(choose_feature_to_split(data))
print(select(data, 0, 1))
#print(decision_tree(data, ['no-surfacing', 'flippers']))
lines = [x.strip().split(',') for x in open('data/cars.csv', encoding='UTF-8').readlines()]
print(lines)
features = lines.pop(0)
features.pop()
print(features, lines)
tree = decision_tree(lines, features)
print(json.dumps(tree, indent=4))

from functools import reduce
from numpy import ones
from numpy.ma import log


def generate_vocabulary(documents):
    return sorted(list(reduce(lambda x, y: x | set(y), [set()] + documents)))


def generate_vector(document, vocabulary):
    return [1 if x in document else 0 for x in vocabulary]


def generate_weighted_vector(document, vocabulary):
    return [document.count(w) for w in vocabulary]
    return 0


def train_bayes(documents, categories):
    prob_abusive = sum(categories) / float(len(documents))
    no_of_words = len(documents[0])
    print(no_of_words)
    abusive_no_prob_num, abusive_ys_prob_num = ones(no_of_words), ones(no_of_words)
    abusive_no_prob_den, abusive_ys_prob_den = 2.0, 2.0
    for document, category in zip(documents, categories):
        if category:
            abusive_ys_prob_num += document
            abusive_ys_prob_den += sum(document)
        else:
            abusive_no_prob_num += document
            abusive_no_prob_den += sum(document)
    abusive_no_prob_vec = log(abusive_no_prob_num / abusive_no_prob_den)
    abusive_ys_prob_vec = log(abusive_ys_prob_num / abusive_ys_prob_den)
    return abusive_no_prob_vec, abusive_ys_prob_vec, prob_abusive


def classify_bayes(vector, abusive_ys, abusive_no, abusive_pr):
    if sum(vector * abusive_ys) + log(abusive_pr) > sum(vector * abusive_no) + log(1 - abusive_pr):
        return 1
    return 0


posts = [
    ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
]
abusives = [0, 1, 0, 1, 0, 1]
vocabulary = generate_vocabulary(posts)

training_data = [generate_vector(post, vocabulary) for post in posts]
abusive_no_prob_vec, abusive_ys_prob_vec, prob_abusive = train_bayes(training_data, abusives)
for w, y, n in zip(vocabulary, abusive_ys_prob_vec, abusive_no_prob_vec):
    print(w, y, n)
unknown = ['stupid', 'garbage']
print(classify_bayes(generate_vector(unknown, vocabulary), abusive_ys_prob_vec, abusive_no_prob_vec, prob_abusive))

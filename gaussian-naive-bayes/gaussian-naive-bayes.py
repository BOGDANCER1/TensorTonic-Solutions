from collections import defaultdict
from math import log

def gaussian_naive_bayes(X_train, y_train, X_test):
    """
    Predict class labels for test samples using Gaussian Naive Bayes.
    """
    n = len(y_train)
    n_features = len(X_train[0])
    # Creating label indecies dictionary
    class_index = defaultdict(list)
    class_probas = {}
    for i, label in enumerate(y_train):
        class_index[label].append(i)

    # Converting to probas
    for label in class_index.keys():
        class_probas[label] = len(class_index[label]) / n

    # Compute the mean value for each label and feature
    means = {}
    for label, indecies in class_index.items():
        means[label] = [0 for i in range(n_features)]
        for index in indecies:
            for i in range(n_features):
                means[label][i] += X_train[index][i]
        means[label] = [feat_sum / len(indecies) for feat_sum in means[label]]
            
    # Compute the mean value for each label and feature
    variances = {}
    for label, indecies in class_index.items():
        variances[label] = [0 for i in range(n_features)]
        for index in indecies:
            for i in range(n_features):
                variances[label][i] += (X_train[index][i] - means[label][i]) ** 2
        variances[label] = [max(feat_sum / len(indecies), 1e-9) for feat_sum in variances[label]]

    # Making prediction for a sample from X_test
    result = []
    for sample in X_test:
        prediction = {label: log(class_probas[label]) for label in class_index.keys()}
        for label in class_index.keys():
            for i, (mean, variance) in enumerate(zip(means[label], variances[label])):
                prediction[label] -= (log(variance ** 2) + (sample[i] - mean) ** 2 / 2 * variance)
        result.append(max(prediction.keys(), key=prediction.get))

    return result
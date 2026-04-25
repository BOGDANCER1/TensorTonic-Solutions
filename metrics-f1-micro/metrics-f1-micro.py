def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    correct = 0
    mistake = 0
    # It's actually the same as accuracy
    for ground_truth, prediction in zip(y_true, y_pred):
        if ground_truth == prediction:
            correct += 1
        else:
            mistake += 1

    return correct / (correct + mistake)
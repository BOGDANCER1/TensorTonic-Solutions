def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    rec_set = set(recommended[:k])
    relevant_set = set(relevant)

    return [len(rec_set & relevant_set) / k, len(rec_set & relevant_set) / len(relevant)]
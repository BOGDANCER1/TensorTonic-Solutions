def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    words_count = {}
    for sentence in sentences:
        for word in sentence:
            words_count[word] = words_count.get(word, 0) + 1

    return words_count
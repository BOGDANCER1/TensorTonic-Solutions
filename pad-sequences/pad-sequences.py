import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not seqs:
        return np.array([])
    if not max_len:
        max_len = 0
        for seq in seqs:
            if (n:=len(seq)) > max_len:
                max_len = n

    padded = np.full(shape=(len(seqs), max_len), fill_value=pad_value, dtype=int)
    # Adding seqs values to the padded matrix
    for i in range(len(seqs)):
        if len(seqs[i]) > max_len:
            padded[i, :] = seqs[i][:max_len]
        else:
            padded[i, :len(seqs[i])] = seqs[i]

    return padded
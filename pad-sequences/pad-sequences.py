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
        max_len = max((len(seq) for seq in seqs))

    padded = np.full(shape=(len(seqs), max_len), fill_value=pad_value, dtype=int)
    # Adding seqs values to the padded matrix
    for i, seq in enumerate(seqs):
        seq_length_to_pad = min(max_len, len(seq))

        padded[i, :seq_length_to_pad] = seq[:seq_length_to_pad]

    return padded
import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    pos_matrix = np.zeros(shape=(seq_len, d_model))
    
    for i in range(seq_len):
        pos_matrix[i, :] = i

    for i in range((d_model + 1) // 2):
        pos_matrix[:, 2 * i] = np.sin(pos_matrix[:, 2 * i] / np.power(base, 2 * i / d_model))

    for i in range(d_model // 2):
        pos_matrix[:, 2 * i + 1] = np.cos(pos_matrix[:, 2*i + 1] / np.power(base, 2*i / d_model))

    return pos_matrix
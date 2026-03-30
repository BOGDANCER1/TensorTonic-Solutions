import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    
    pe_matrix = np.zeros(shape=(seq_length, d_model))

    for i in range(seq_length):
        pe_matrix[i, :] += i

    for i in range((d_model + 1) // 2):
        pe_matrix[:, 2 * i] = np.sin(pe_matrix[:, 2 * i] / np.power(10000, 2 * i / d_model))

    for i in range((d_model) // 2):
        pe_matrix[:, 2 * i + 1] = np.cos(pe_matrix[:, 2 * i + 1] / np.power(10000, 2 * i / d_model))

    return pe_matrix
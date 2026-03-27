def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    a, b = min(values), max(values)
    if a == b:
        return [0 for x in values]
    w = (b - a) / num_bins

    return [min(int((x - a) / w), num_bins - 1) for x in values]
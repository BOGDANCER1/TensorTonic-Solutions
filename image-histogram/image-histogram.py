def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    bins = [0 for _ in range(256)]
    
    for row in image:
        for pixel in row:
            bins[pixel] += 1

    return bins
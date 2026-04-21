def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    def have_intersection(box_a, box_b):
        case_1 = (box_a[0] <= box_b[0] <= box_a[2]) and (box_a[1] <= box_b[1] <= box_a[3])
        case_2 = (box_a[0] <= box_b[2] <= box_a[2]) and (box_a[1] <= box_b[3] <= box_a[3])
        return (case_1 or case_2)

    if not have_intersection(box_a, box_b):
        return 0.
    else:
        A = (max(box_a[0], box_b[0]), min(box_a[3], box_b[3]))
        B = (min(box_a[2], box_b[2]), max(box_a[1], box_b[1]))

        length = abs(B[0] - A[0])
        height = abs(B[1] - A[1])

        intersection = length * height
        area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
        area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

        return intersection / (area_a + area_b - intersection)
        
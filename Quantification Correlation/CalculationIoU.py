import numpy as np

def CalculateIoU(ERMArea, RetinalThicknessArea):
    RetinalThicknessAreaPixels = np.all(RetinalThicknessArea != [0, 0, 0], axis=-1)
    ERMAreaPixels = np.all(ERMArea != [0, 0, 0], axis=-1)

    intersection = np.logical_and(ERMAreaPixels, RetinalThicknessAreaPixels)
    union = np.logical_or(ERMAreaPixels, RetinalThicknessAreaPixels)
    iou = np.sum(intersection) / np.sum(union)

    return iou

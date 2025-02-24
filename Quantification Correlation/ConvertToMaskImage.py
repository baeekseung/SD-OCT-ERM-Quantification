import cv2
import os
import numpy as np

def Convert2MaskImage(patientinfo):
    RetinalThicknessClasses = ["Class1", "Class2", "Class3", "Class4", "Class5", "Class6", "Class7", "Class8", "Class9"]
    for RTClass in RetinalThicknessClasses:
        ThicknessArea = cv2.imread(f'./Data/Thickness map/ReinalThicknessArea/{patientinfo}/{RTClass}.png', 0)
        _, mask = cv2.threshold(ThicknessArea, 10, 255, cv2.THRESH_BINARY)
        mask[600:] = 0
        cv2.imwrite(f"./Data/Thickness map/ReinalThicknessArea/{patientinfo}/{RTClass}_MaskImage.png",mask, params=None)

    ERMarea = cv2.imread(f"./Data/ERM Area/{patientinfo}_Overlay.png")
    _, mask = cv2.threshold(ERMarea, 127, 255, cv2.THRESH_BINARY)
    mask = cv2.bitwise_not(mask)
    mask_ = mask[:, :, 0] != 0
    mask[mask_] = [255, 255, 255]

    mask[:110] = 0
    mask[534:] = 0
    cv2.imwrite(f"./Data/ERM Area/ERM Area MaskImage/{patientinfo}_ERMareaMask.png", mask, params=None)

import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

from RetinalThickness9ClassExtract import NineClassSegmentation
from ConvertToMaskImage import Convert2MaskImage
from CalculationIoU import CalculateIoU

def CorrelationEquation(IoUList):
    CorrelationList = []
    for i in range(0,9):
        Weight = -0.01*((i+1)**2)-0.07*(i+1)+1.666
        Calculated = Weight * IoUList[i]
        CorrelationList.append(Calculated)
    Correlation = sum(CorrelationList)/9
    return Correlation

def QuantificationCorrelation(patientInfo):
    IoUList = []
    RetinalThicknessClasses = ["Class1", "Class2", "Class3", "Class4", "Class5", "Class6", "Class7", "Class8", "Class9"]
    RetinalThicknessArea = np.zeros((640,640,3))
    NineClassSegmentation(patientInfo)
    Convert2MaskImage(patientInfo)

    ERMArea = cv2.imread(f"./Data/ERM Area/ERM Area MaskImage/{patientInfo}_ERMareaMask.png")

    for RTClass in RetinalThicknessClasses:
        RetinalThicknessClassArea = cv2.imread(f"./Data/Thickness map/ReinalThicknessArea/{patientInfo}/{RTClass}_MaskImage.png")
        RetinalThicknessArea += RetinalThicknessClassArea
        IoU = CalculateIoU(ERMArea,RetinalThicknessArea)
        IoUList.append(IoU)
    Correlation = CorrelationEquation(IoUList)
    print(f"Patient Infomation : {patientInfo} | Correlation : {Correlation}")

QuantificationCorrelation("0000021587_OS 2016-06-27")
QuantificationCorrelation("0000027135_OD 2021-02-01")
QuantificationCorrelation("0000175521_OS 2020-09-16")
QuantificationCorrelation("0000247266_OS 2020-12-04")
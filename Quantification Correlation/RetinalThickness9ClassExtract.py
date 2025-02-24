import cv2
import numpy as np
import os

def NineClassSegmentation(patientinfo):
    Thicknessmap = cv2.imread(f"./Data/Thickness map/{patientinfo}.png")
    hsv_Thicknessmap = cv2.cvtColor(Thicknessmap, cv2.COLOR_BGR2HSV)

    # 빨간색 범위 설정 0 ~ 13
    lower_red1 = np.array([0, 50, 50]); upper_red1 = np.array([3, 255, 255])
    lower_red2 = np.array([4, 50, 50]); upper_red2 = np.array([7, 255, 255])
    lower_red3 = np.array([8, 50, 50]); upper_red3 = np.array([13, 255, 255])
    red_mask1 = cv2.inRange(hsv_Thicknessmap, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv_Thicknessmap, lower_red2, upper_red2)
    red_mask3 = cv2.inRange(hsv_Thicknessmap, lower_red3, upper_red3)

    # 노란색 범위 설정 14 ~ 35
    lower_yellow1 = np.array([14, 100, 100]); upper_yellow1 = np.array([20, 255, 255])
    lower_yellow2 = np.array([21, 100, 100]); upper_yellow2 = np.array([27, 255, 255])
    lower_yellow3 = np.array([28, 100, 100]); upper_yellow3 = np.array([35, 255, 255])
    yellow_mask1 = cv2.inRange(hsv_Thicknessmap, lower_yellow1, upper_yellow1)
    yellow_mask2 = cv2.inRange(hsv_Thicknessmap, lower_yellow2, upper_yellow2)
    yellow_mask3 = cv2.inRange(hsv_Thicknessmap, lower_yellow3, upper_yellow3)

    # 초록색 범위 설정
    lower_green1 = np.array([36, 0, 0]); upper_green1 = np.array([48, 255, 255])
    lower_green2 = np.array([49, 0, 100]); upper_green2 = np.array([58, 255, 255])
    lower_green3 = np.array([59, 0, 100]); upper_green3 = np.array([68, 255, 255])
    green_mask1 = cv2.inRange(hsv_Thicknessmap, lower_green1, upper_green1)
    green_mask2 = cv2.inRange(hsv_Thicknessmap, lower_green2, upper_green2)
    green_mask3 = cv2.inRange(hsv_Thicknessmap, lower_green3, upper_green3)

    red_result1 = cv2.bitwise_and(Thicknessmap, Thicknessmap, mask=red_mask1)
    red_result2 = cv2.bitwise_and(Thicknessmap, Thicknessmap, mask=red_mask2)
    red_result3 = cv2.bitwise_and(Thicknessmap, Thicknessmap, mask=red_mask3)
    yellow_result1 = cv2.bitwise_and(Thicknessmap, Thicknessmap, mask=yellow_mask1)
    yellow_result2 = cv2.bitwise_and(Thicknessmap, Thicknessmap, mask=yellow_mask2)
    yellow_result3 = cv2.bitwise_and(Thicknessmap, Thicknessmap, mask=yellow_mask3)
    green_result1 = cv2.bitwise_and(Thicknessmap, Thicknessmap, mask=green_mask1)
    green_result2 = cv2.bitwise_and(Thicknessmap, Thicknessmap, mask=green_mask2)
    green_result3 = cv2.bitwise_and(Thicknessmap, Thicknessmap, mask=green_mask3)

    masklist = [red_result1,red_result2,red_result3,yellow_result1,yellow_result2,yellow_result3
                ,green_result1,green_result2,green_result3]
    maskname = ["Class1","Class2","Class3","Class4","Class5","Class6","Class7","Class8","Class9"]
    try:
        os.makedirs(f"./Data/Thickness map/ReinalThicknessArea/{patientinfo}")
    except FileExistsError:
        pass

    for mask,name in zip(masklist,maskname):
        cv2.imwrite(f"./Data/Thickness map/ReinalThicknessArea/{patientinfo}/{name}.png"
                    , mask, params=None)


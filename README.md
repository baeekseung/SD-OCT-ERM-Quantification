# SD-OCT-based Epiretinal Membrane Diagnostic Assistant System

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge)
![YOLO](https://img.shields.io/badge/YOLO-013243?style=for-the-badge)
![Pillow](https://img.shields.io/badge/Pillow-CC66CC?style=for-the-badge)

## Introduction
This project presents a low-cost and efficient method for detecting and quantifying Epiretinal Membranes (ERM) using Spectral-Domain Optical Coherence Tomography (SD-OCT). By applying deep learning techniques—specifically, YOLO object detection—we generate en face "ERM Projection Images" from B-scan data, enabling intuitive visualization and accurate measurement of ERM areas. The method also introduces a novel approach to quantify the association between ERM and retinal thickness, enhancing clinical decision-making. Our approach aims to bridge the diagnostic performance gap between SD-OCT and Swept-Source OCT (SS-OCT) while maintaining accessibility and reducing diagnostic burden.




## YOLO model evaluation

We evaluated three YOLO-based models (v5, v8, v11) for ERM detection using SD-OCT B-scan images.  
Each model was trained on two datasets (2,200 images for **Full**, 1,100 images for **Half**) and tested on 650 expert-labeled images.

| Model   | Size | Params (M) | Precision | Recall | mAP@50 | mAP@50:95 | Dataset Size |
|---------|------|------------|-----------|--------|--------|-----------|---------------|
| YOLOv5  | S    | 7.02       | 0.838     | 0.746  | 0.794  | 0.499     | Full          |
|         |      |            | 0.778     | 0.691  | 0.739  | 0.449     | Half          |
|         | M    | 20.87      | 0.721     | 0.714  | 0.751  | 0.477     | Full          |
|         |      |            | 0.650     | 0.698  | 0.666  | 0.381     | Half          |
|         | L    | 46.14      | 0.766     | 0.842  | 0.771  | 0.497     | Full          |
|         |      |            | 0.720     | 0.675  | 0.728  | 0.413     | Half          |
|         | X    | 86.22      | 0.812     | 0.829  | 0.836  | 0.540     | Full          |
|         |      |            | 0.489     | 0.642  | 0.522  | 0.259     | Half          |
| YOLOv8  | S    | 11.14      | 0.781     | 0.775  | 0.816  | 0.529     | Full          |
|         |      |            | 0.827     | 0.684  | 0.768  | 0.488     | Half          |
|         | M    | 25.86      | 0.787     | 0.684  | 0.760  | 0.481     | Full          |
|         |      |            | 0.722     | 0.724  | 0.716  | 0.429     | Half          |
|         | L    | 43.63      | 0.842     | 0.697  | 0.798  | 0.502     | Full          |
|         |      |            | 0.665     | 0.697  | 0.711  | 0.429     | Half          |
|         | X    | 68.15      | 0.764     | 0.746  | 0.755  | 0.464     | Full          |
|         |      |            | 0.608     | 0.638  | 0.615  | 0.339     | Half          |
| YOLOv11 | S    | 9.43       | 0.762     | 0.836  | 0.811  | 0.495     | Full          |
|         |      |            | 0.745     | 0.783  | 0.766  | 0.454     | Half          |
|         | M    | 20.05      | 0.811     | 0.783  | 0.817  | 0.538     | Full          |
|         |      |            | 0.768     | 0.763  | 0.784  | 0.485     | Half          |
|         | L    | 25.31      | 0.766     | 0.842  | 0.843  | 0.537     | Full          |
|         |      |            | 0.714     | 0.822  | 0.787  | 0.488     | Half          |
|         | X    | 56.87      | 0.812     | 0.829  | 0.836  | 0.540     | Full          |
|         |      |            | 0.738     | 0.783  | 0.755  | 0.490     | Half          |



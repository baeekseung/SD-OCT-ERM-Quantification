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
|---------|------|------------|-----------|--------|--------|-----------|--------------|
| YOLOv5  | S    | 7.02       | 0.752     | 0.703  | 0.722  | 0.423     | Full         |
|         |      |            | 0.694     | 0.642  | 0.664  | 0.376     | Half         |
|         | M    | 20.87      | 0.783     | 0.734  | 0.752  | 0.444     | Full         |
|         |      |            | 0.723     | 0.685  | 0.701  | 0.396     | Half         |
|         | L    | 46.14      | 0.813     | 0.762  | 0.784  | 0.463     | Full         |
|         |      |            | 0.745     | 0.704  | 0.726  | 0.414     | Half         |
|         | X    | 86.22      | 0.836     | 0.784  | 0.802  | 0.485     | Full         |
|         |      |            | 0.763     | 0.725  | 0.743  | 0.437     | Half         |
| YOLOv8  | S    | 11.14      | 0.781     | 0.736  | 0.764  | 0.447     | Full         |
|         |      |            | 0.723     | 0.676  | 0.701  | 0.393     | Half         |
|         | M    | 25.86      | 0.813     | 0.762  | 0.791  | 0.466     | Full         |
|         |      |            | 0.748     | 0.705  | 0.724  | 0.412     | Half         |
|         | L    | 43.63      | 0.844     | 0.792  | 0.823  | 0.482     | Full         |
|         |      |            | 0.774     | 0.731  | 0.754  | 0.436     | Half         |
|         | X    | 68.15      | 0.867     | 0.814  | 0.842  | 0.504     | Full         |
|         |      |            | 0.793     | 0.752  | 0.772  | 0.454     | Half         |
| YOLOv11 | S    | 9.43       | 0.804     | 0.752  | 0.783  | 0.468     | Full         |
|         |      |            | 0.746     | 0.692  | 0.714  | 0.417     | Half         |
|         | M    | 20.05      | 0.846     | 0.794  | 0.821  | 0.493     | Full         |
|         |      |            | 0.774     | 0.736  | 0.757  | 0.443     | Half         |
|         | L    | 25.31      | 0.873     | 0.823  | 0.854  | 0.524     | Full         |
|         |      |            | 0.807     | 0.773  | 0.793  | 0.476     | Half         |
|         | X    | 56.87      | 0.902     | 0.857  | 0.882  | 0.556     | Full         |
|         |      |            | 0.836     | 0.803  | 0.826  | 0.507     | Half         |




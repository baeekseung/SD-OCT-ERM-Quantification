from ultralytics import YOLO

def main():
    model = YOLO('yolo11m.pt')

    model.train(
        data='../Data/Train_data/ERMdata.yaml',
        epochs=50,
        imgsz=640,
        batch=16,
        name='ERM_YOLOv11m',
        device='cuda',  
        verbose=True
    )

    results = model.val()


if __name__ == '__main__':
    main()
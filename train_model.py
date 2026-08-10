from ultralytics import YOLO


def main():
    # 1. Load the model
    # We start with 'yolov8n.pt' (Nano), which is small and fast.
    print("Loading YOLOv8 Nano model...")
    model = YOLO('yolov8n.pt')

    # 2. Train the model
    # We pass the absolute path to your data config
    print("Starting training...")
    results = model.train(
        data='/home/apurv/SynthData_Factory/data.yaml',
        epochs=20,
        imgsz=640,
        project='/home/apurv/SynthData_Factory/runs',  # Explicitly save here
        name='cheezit_run'
    )

    print("Training Complete.")
    print(f"Best model saved at: {results.save_dir}/weights/best.pt")


if __name__ == '__main__':
    main()
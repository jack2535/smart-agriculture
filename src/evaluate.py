import torch
from yolov11n import YOLOv11nModel, evaluate

def evaluate_model():
    model = YOLOv11nModel("model/yolov11n_weights.onnx")
    dataset_path = "data/annotations/"
    
    # Placeholder for evaluation
    results = evaluate(model, dataset_path)
    print("Evaluation results:", results)

if __name__ == "__main__":
    evaluate_model()
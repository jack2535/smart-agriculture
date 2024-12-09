import cv2
import numpy as np
from src.agriculture_monitor import AgricultureMonitor

# Load model
monitor = AgricultureMonitor("model/yolov11n_weights.onnx")

# Input image
input_image_path = "test_images/sample1.jpg"
image = cv2.imread(input_image_path)

# Detect and annotate objects
output_image, counts = monitor.detect_and_count(image)

# Display results
print(f"Detected object counts: {counts}")
cv2.imshow("Detection", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
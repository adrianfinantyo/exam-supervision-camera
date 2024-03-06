import supervision as sv
import numpy as np
from ultralytics import YOLO
import os
from PIL import Image
import cv2


def detect():
    ROOT_DIR = os.path.abspath('./')
    VIDEO_PATH = os.path.join(ROOT_DIR, 'videos', 'rcam-compressed.mp4')
    WEIGHTS_PATH = os.path.join(ROOT_DIR, 'runs/detect/train7/weights', 'best.pt')

    model = YOLO(WEIGHTS_PATH)

    for result in model.predict(source=VIDEO_PATH, stream=True, save=True, classes=[1]):
        pass


if __name__ == "__main__":
    detect()
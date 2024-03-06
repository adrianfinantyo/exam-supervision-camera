from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def training():
    dataset_dir = os.path.abspath('dataset')
    model = YOLO('yolov8n.pt')
    model.train(data=os.path.join(dataset_dir, 'data.yaml'), epochs=100, batch=8, device=0, pos_weight=[1.08,12.60], verbose=True, name='train9-100epoch-pw-adjust')

# Init
if __name__ == '__main__':
    training()
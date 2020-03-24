# image.py
import tensorflow as tf
from controller.detector.utils import load_class_names, output_boxes, resize_image, return_outputs
import cv2
import numpy as np
from controller.detector.yolov3 import YOLOv3Net

physical_devices = tf.config.experimental.list_physical_devices('GPU')

model_size = (416, 416, 3)
num_classes = 80
class_name = 'controller/detector/coco.names'
max_output_size = 40
max_output_size_per_class = 20
iou_threshold = 0.5
confidence_threshold = 0.5
cfgfile = 'controller/detector/yolov3.cfg'
weightfile = 'controller/detector/weights/yolov3_weights.tf'


def main(img_path):
    model = YOLOv3Net(cfgfile, model_size, num_classes)
    model.load_weights(weightfile)
    class_names = load_class_names(class_name)
    image = cv2.imread(img_path)
    image = np.array(image)
    image = tf.expand_dims(image, 0)
    resized_frame = resize_image(image, (model_size[0], model_size[1]))
    pred = model.predict(resized_frame)
    boxes, scores, classes, nums = output_boxes(
        pred, model_size,
        max_output_size=max_output_size,
        max_output_size_per_class=max_output_size_per_class,
        iou_threshold=iou_threshold,
        confidence_threshold=confidence_threshold)
    image = np.squeeze(image)
    result = return_outputs(image, boxes, scores, classes, nums, class_names, img_path)
    return result


if __name__ == '__main__':
    main(img_path="dogandcat2.jpg")

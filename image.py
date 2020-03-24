# image.py
import tensorflow as tf
from utils import load_class_names, output_boxes, draw_outputs, resize_image, print_outputs
import cv2
import numpy as np
from yolov3 import YOLOv3Net

physical_devices = tf.config.experimental.list_physical_devices('GPU')

model_size = (416, 416, 3)
num_classes = 80
class_name = 'coco.names'
max_output_size = 40
max_output_size_per_class = 20
iou_threshold = 0.5
confidence_threshold = 0.5
cfgfile = 'yolov3.cfg'
weightfile = 'weights/yolov3_weights.tf'
img_path = "dogandcat2.jpg"


def main():
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
    img = print_outputs(image, boxes, scores, classes, nums, class_names, img_path)
    img = draw_outputs(image, boxes, scores, classes, nums, class_names)
    win_name = 'Image detection'
    cv2.imshow(win_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # If you want to save the result, uncommnent the line below:
    # cv2.imwrite('test.jpg', img)


if __name__ == '__main__':
    main()

import tensorflow as tf
import numpy as np
import cv2
import os


def non_max_suppression(inputs, model_size, max_output_size,
                        max_output_size_per_class, iou_threshold,
                        confidence_threshold):
    bbox, confs, class_probs = tf.split(inputs, [4, 1, -1], axis=-1)
    bbox = bbox / model_size[0]
    scores = confs * class_probs
    boxes, scores, classes, valid_detections = \
        tf.image.combined_non_max_suppression(
            boxes=tf.reshape(bbox, (tf.shape(bbox)[0], -1, 1, 4)),
            scores=tf.reshape(scores, (tf.shape(scores)[0], -1,
                                       tf.shape(scores)[-1])),
            max_output_size_per_class=max_output_size_per_class,
            max_total_size=max_output_size,
            iou_threshold=iou_threshold,
            score_threshold=confidence_threshold
        )
    return boxes, scores, classes, valid_detections


def resize_image(inputs, modelsize):
    inputs = tf.image.resize(inputs, modelsize)
    return inputs


def load_class_names(file_name):
    with open(file_name, 'r') as f:
        class_names = f.read().splitlines()
    return class_names


def output_boxes(inputs, model_size, max_output_size, max_output_size_per_class,
                 iou_threshold, confidence_threshold):
    center_x, center_y, width, height, confidence, classes = \
        tf.split(inputs, [1, 1, 1, 1, 1, -1], axis=-1)
    top_left_x = center_x - width / 2.0
    top_left_y = center_y - height / 2.0
    bottom_right_x = center_x + width / 2.0
    bottom_right_y = center_y + height / 2.0
    inputs = tf.concat([top_left_x, top_left_y, bottom_right_x,
                        bottom_right_y, confidence, classes], axis=-1)
    boxes_dicts = non_max_suppression(inputs, model_size, max_output_size,
                                      max_output_size_per_class, iou_threshold, confidence_threshold)
    return boxes_dicts


def return_outputs(img, boxes, objectness, classes, nums, class_names, img_name):
    boxes, objectness, classes, nums = boxes[0], objectness[0], classes[0], nums[0]
    boxes = np.array(boxes)
    classesDetected = list()
    imagesList = list()
    for i in range(nums):
        x1y1 = tuple((boxes[i, 0:2] * [img.shape[1], img.shape[0]]).astype(np.int32))
        x2y2 = tuple((boxes[i, 2:4] * [img.shape[1], img.shape[0]]).astype(np.int32))
        print('The coords for class {} are x1={}, x2={}, y1={}, y2={} and its accuracy is {:.4f}'
              .format(class_names[int(classes[i])], x1y1[0], x2y2[0], x1y1[1], x2y2[1], objectness[i]))
        path = os.getcwd()
        img = cv2.imread(img_name)
        crop_img = img[x1y1[1]:x2y2[1], x1y1[0]:x2y2[0]]
        filename = (str(class_names[int(classes[i])]) + '-' + str(i) + '.jpg')
        cv2.imwrite(os.path.join(path, 'controller/detector/cropped', filename), crop_img)
        classesDetected.append(class_names[int(classes[i])])
        imageDetails = {
            "imageName": filename,
            "imagePath": str(os.path.join(path, 'controller/detector/cropped', filename)),
            "class": class_names[int(classes[i])]
        }
        imagesList.append(imageDetails)

    result = {
              "images": imagesList,
              "classesDetected": list(set(classesDetected))
             }
    return result

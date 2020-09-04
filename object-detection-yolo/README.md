### Object detection with YOLOv2

The project allows to detect and classify objects on input images. It uses a Keras implementation of [YOLOv2](https://pjreddie.com/darknet/yolov2/) deep learning model and leverages pre-trained weights. The model accepts an input image and after some processing returns the image marked with bounding boxes, which represent detected objects. Each bounding box features a label that classifies the detected object.

<center>
<img src="https://github.com/molly-moon/projects/raw/master/images/mazio_hambugs.png" height=300/>
</center>

See the [Jupyter Notebook](https://github.com/molly-moon/projects/blob/master/object-detection-yolo/yolo_object_detection.ipynb) for more details. 

### Acknowledgements

Yolo is a deep learning model created by Joseph Redmon. The keras implementation of YOLOv2 I use in this project is one of my assignments from [Deep Learning Specialization course](https://www.coursera.org/specializations/deep-learning) created by deeplearning.ai. The course assignment was greatly inspired by [Yet Another Darknet 2 Keras project](https://github.com/allanzelener/YAD2K) by Allan Zelener.
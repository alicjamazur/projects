## Demo apps and projects
This repository containes demo applications and projects I created while getting to know data science and cloud computing concepts. 

<br>

+ [Object Detection Application](https://github.com/molly-moon/projects/tree/master/object_detection)

  Serverless application that uses a deep learning model YOLOv2 to detect objects on uploaded images.

  The app is a single page website that accepts an input image for back-end serverless processing with AWS Lambda. It responds with the provided input image that has been marked with bouding boxes which represent detected objects. Each bounding box features a label that classifies the detected object.
  <p align=center>
  <img src="https://github.com/molly-moon/projects/raw/master/images/mazio_hambugs.png" height=300/>
  </p>
  
<br>
<br>

+ [Image Classification Project]()
	
  The project allows to identify a number shown with hand gesture captured on images. It uses a ResNet deep learning model and leverages pre-trained weights. The model accepts an input image and returns a probability vector with 6 elements, corresponding to numbers 0-5. 

  <p align=center>
  <img src="https://github.com/molly-moon/projects/raw/master/image-classification-resnet/images/hand-gesture.png" height=200/>
  </p>

  <br>
  <br>

+ [Face Verification and Recognition Project]()

  This project implements Inception algorithm for face verification and face recognition. 

  Face verification part accepts user input that to claim their identity and asseses whether the claimed identity is    true or not. Model compared the input image with the ground truth records stored in a database. Test 1 was conveyed so that user input represented a true claimed identity, while during Test 2 a false claimed identity was introduced.

  <p align=center>
  <img src="https://github.com/molly-moon/projects/raw/master/face-verification-recognition/images/face-verification.png" width=300>
  </p>

  Face recognition part accepts a user's face image and returns its best prediction for their identity, based on a ground truth records stored in a database.

  <p align=center>
  <img src="https://github.com/molly-moon/projects/raw/master/face-verification-recognition/images/face-recognition.png" width=180>
  </p>

  <br>
  <br>

+ [Trigger Word Detection Project]()

  The model detects trigger word "activate" in input audio files. It triggers a chiming sound when the probability ultrapasses a certain threshold. The model is a uni-directional Recurrent Neural Network with Gated Recurrent Unit (GRU). It was trained on synthesized audio files from noise, trigger word and non-trigger word sounds. 

  <p align=center>
  <img src="https://github.com/molly-moon/projects/raw/master/images/trigger-word-detection.png" height=300/>
  </p>

  See the [Jupyter Notebook](https://github.com/molly-moon/projects/blob/master/trigger_word_detection/trigger_word_detection.ipynb) for more details. 

  <br>
  <br>
+ [Scratch, a note taking app]()

  Project inspired by the open-source project [Serverless Stack](https://serverless-stack.com/) by Anomaly Innovations. They created a step-by-step guide to help you build a full-stack serverless application hosted on AWS.
  <p align=center>
  <img src="https://github.com/molly-moon/projects/raw/master/app-notes/images/notes1.png" width="400"/>
  <br> 
  <img src="https://github.com/molly-moon/projects/raw/master/app-notes/images/notes2.png" width="400"/>
  <br> 
  <img src="https://github.com/molly-moon/projects/raw/master/app-notes/images/notes3.png" width="400"/>
  </p>
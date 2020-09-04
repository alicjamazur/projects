### Trigger word detection with RNN
This project is one of my assignments from [Deep Learning Specialization course](https://www.coursera.org/specializations/deep-learning) 

The model detects trigger word "activate" in input audio files. It triggers a chiming sound when the probability ultrapasses a certain threshold. The model is a uni-directional Recurrent Neural Network with Gated Recurrent Unit (GRU). It was trained on synthesized audio files from noise, trigger word and non-trigger word sounds. 

<img src="https://github.com/molly-moon/projects/raw/master/images/trigger-word-detection.png" height=300/>

See the [Jupyter Notebook](https://github.com/molly-moon/projects/blob/master/trigger_word_detection/trigger_word_detection.ipynb) for more details. 
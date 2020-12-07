# Mask-Detector

Automatic verification of protective masks on the face.

## Table of content
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)

## General info
The project was designed to automatically detect faces in pictures/videos and verify that they have a properly applied mask.

I trained the model on publicly available datasets

## Technologies
* Python 3.72
	
## Setup
To run this project

```
$ git clone https://github.com/jedrzejd/Mask-Detector.git
$ cd Mask-Detector
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python app.py
```

## Status

* Now
    * The app recognizes a face and draws a rectangle with the probability that the person has a correctly fitted mask.
    
* In Future
    - Added the ability to use multiple video sources.
    - Improving the accuracy of the model (currently 95% accuracy on the training set)
    - Greater generalization of the model, for example: for people with glasses, different skin color

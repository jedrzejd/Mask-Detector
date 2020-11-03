# Mask-Detector

Application for mask detection created in Python.

## Table of content
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)

## General info
This project is created for mask detection using pre-trained models.

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

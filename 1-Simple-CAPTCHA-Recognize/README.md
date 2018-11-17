# Simple CAPTCHA Recognize

 ![](https://img.shields.io/badge/Numpy-1.15.x-brightgreen.svg?style=flat-square) ![](https://img.shields.io/badge/pillow-5.3.0-brightgreen.svg?style=flat-square) ![](https://img.shields.io/badge/scikit--learn-0.20.0-brightgreen.svg?style=flat-square)

## Abstract

Nowadays, *CAPTCHA* becomes a required field when we want to login or register on a website. This is due to the situation that there are too many web spiders in the internet.

*CAPTCHA* is using to distinguish human and machine. However, developers try different ways to crack or bypass the *CAPTCHA*. *Machine learning* is one of the most popular method to solve this problem.

In this project, we aim to use the basic *machine learning* algorithm to break the simplest *CAPTCHA* which consist of only 4 digit from 0 ~ 9.



Example CAPTCHA:

![captcha_0](https://user-images.githubusercontent.com/10103993/48635619-9f1bc980-ea03-11e8-8f32-44877e56e5dd.jpg)



## Methodology

Briefly speaking, since the *CAPTCHA* is the most simplest, we can directly cut the image into 4 parts with fixed size. Like following images:

![captcha_0-digit_0](https://user-images.githubusercontent.com/10103993/48635635-acd14f00-ea03-11e8-8ffc-faf89f5b4867.jpg) ![captcha_0-digit_1](https://user-images.githubusercontent.com/10103993/48635640-b064d600-ea03-11e8-9c72-7010d85a8955.jpg) ![captcha_0-digit_2](https://user-images.githubusercontent.com/10103993/48635641-b2c73000-ea03-11e8-9964-d506c662cfdc.jpg) ![captcha_0-digit_3](https://user-images.githubusercontent.com/10103993/48635644-b490f380-ea03-11e8-9bc3-3c51480885c9.jpg)



Then, we can **binarize** the pixels by mapping the pixel from RGB format to 0 or 1. (0 means background and 1 means foreground).

```(255, 126, 167)  =&gt; 1
(255, 126, 167)  => 1
(45, 16, 23)     => 0
```



After that, the **pixel sequence** will become a **binary sequence**, which can be regard as a **feature vector**.

Finally, we can use the **feature vector** to train a classifier and then use it to predict.



## Tiny Demo

In this demo, we use python to process the image and build the classifier.

### Introduction

Simply, we use the *MLPClassifier* in *sklearn.neural* network* as the classifier.

training_set:

![captcha_0](https://user-images.githubusercontent.com/10103993/48635619-9f1bc980-ea03-11e8-8f32-44877e56e5dd.jpg) ![captcha_1](https://user-images.githubusercontent.com/10103993/48636278-6da3fd80-ea05-11e8-98ba-759127926b44.jpg)

training_labels:

```python
train_label_set = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 9
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 7
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 3
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 8
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 4
]
```



test_set:

![captcha_test](https://user-images.githubusercontent.com/10103993/48636330-8dd3bc80-ea05-11e8-9382-5da393198fae.jpg)

test_labels:

```python
test_label_set = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 7
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 3
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 4
]
```



Prediction Result:

```
[7 0 0 3]
```





### Get started

#### Install libraries

- [pillow](https://python-pillow.org/)
- [NumPy](http://www.numpy.org/)
- [scikit-learn](https://scikit-learn.org/)

```bash
pip install pillow numpy scikit-learn
```

#### Run 

```bash
python main.py
```
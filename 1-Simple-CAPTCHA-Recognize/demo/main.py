# -*-coding:utf-8-*-

import os
import numpy as np
from image_crop import crop_image
from feature_extract import feature_extract
from train import preprocess, train

if __name__ == "__main__":
    captcha_dir = os.path.join(os.path.curdir, 'captcha', 'train_set')
    captcha_file_list = os.listdir(captcha_dir)

    # train data
    train_feature_set = []
    for captcha_file_name in captcha_file_list:
        digits_path = crop_image(os.path.join(captcha_dir, captcha_file_name), captcha_file_name.split('.')[0])
        for digit_path in digits_path:
            train_feature_set.append(feature_extract(digit_path))

    # demo use only
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

    # test data
    test_digits_path = crop_image(os.path.join(os.path.curdir, 'captcha', 'test_set', 'captcha_test.jpg'), 'test')
    test_feature_set = []
    for digit_path in test_digits_path:
        test_feature_set.append(feature_extract(digit_path))
    test_label_set = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 7
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 3
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 4
    ]

    # train & predict
    scaler = preprocess(train_feature_set)
    scaler.transform(train_feature_set)
    scaler.transform(test_feature_set)

    clf = train(train_feature_set, train_label_set)
    prediction = clf.predict(test_feature_set)

    print(prediction)
    print(np.argmax(prediction, axis=1))









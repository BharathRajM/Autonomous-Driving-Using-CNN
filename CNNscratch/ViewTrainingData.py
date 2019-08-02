# test_model.py

import numpy as np
import cv2
import pandas as pd
from random import shuffle
from collections import Counter

train_data = np.load('check_new_output5_training_data.npy')

for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test',img)
    print(choice)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

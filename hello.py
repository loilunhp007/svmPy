#import library 
import numpy as np 
import pandas as pd 
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D,Dense,MaxPool2D,Flatten
from tensorflow.keras.regularizers import l2

import os
for dirname, _, filenames in os.walk('/Desktop/python/data'):
    for filename in filenames:
        print(os.path.join(dirname, filename)) 
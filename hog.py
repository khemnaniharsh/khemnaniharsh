# -*- coding: utf-8 -*-
"""Hog.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iEqRmkonCXOQduv-jfN8q8GKpGr_3x7q
"""

import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io
from PIL import Image
import matplotlib.pylab as plt
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure

url = ["https://th.bing.com/th/id/R.fd2bef4a8b6171f78afcea44eb61174b?rik=EcZx7S6dg1Osag&riu=http%3a%2f%2f66.media.tumblr.com%2f1a05c3c0dd84246980068cb66dead267%2ftumblr_o691obyVll1tf2beyo1_500.jpg&ehk=BEtQzHymlw%2fvYa5a8dfJRQaHuB4nhq4ZtqkPanIRqIQ%3d&risl=&pid=ImgRaw&r=0"]
image1 = io.imread(url[0])
image1 = cv.cvtColor(image1,cv.COLOR_BGR2RGB)
cv2_imshow(image1)

def plot_img(images,titles):
  flg,axs = plt.subplots(nrows = 1,ncols = len(images),figsize = (15,15))
  for i,p in enumerate(images):
    axs[i].imshow(p,'gray')
    axs[i].set_title(titles[i])
  plt.show()

ret, img_binary = cv.threshold(image1,127,255,cv.THRESH_BINARY)

images=[image1,img_binary]
titles = ['original image','THRESH_BINARY']
plot_img(images,titles)

ret, img_threshtozero = cv.threshold(image1,127,255,cv.THRESH_TOZERO)

images=[image1,img_threshtozero]
titles = ['original image','THRESH_TOZERO']
plot_img(images,titles)
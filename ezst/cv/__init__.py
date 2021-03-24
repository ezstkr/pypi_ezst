import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import requests

import cv2
from PIL import ImageFont

def read(file_path):
  return mpimg.imread(file_path)

def save(file_path, img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
  cv2.imwrite(file_path, img)

def show(img, grid=False, size=12):
  size = (size, size)
  plt.figure(figsize=size)
  plt.grid(grid)
  plt.imshow(img)
  plt.show()

def cut(img, position, thickness=3, color=(255, 0, 0)):
  top = position[0]
  right = position[1]
  bottom = position[2]
  left = position[3]

  return img[top:bottom, left:right]

def box(img, position, thickness=3, color=(255, 0, 0)):
  top = position[0]
  right = position[1]
  bottom = position[2]
  left = position[3]

  lt = (left, top)
  rb = (right, bottom)
  return cv2.rectangle(img, lt, rb, color, thickness=thickness)

def line(img, pt1, pt2, thickness=3, color=(255, 0, 0)):
  return cv2.line(img, pt1, pt2, color, thickness=thickness)

def circle(img, center, axes, thickness=3, color=(255, 0, 0)):
  return cv2.circle(img, center, radius, color, thickness=thickness)

def text(img, text, pt1, size=1, color=(255, 0, 0)):
  return cv2.putText(img, text, pt1, cv2.FONT_HERSHEY_SIMPLEX, size,color,2)
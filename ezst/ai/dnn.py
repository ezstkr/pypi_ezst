import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import numpy as np

class DNN:
  pass

dnn = DNN()


class CustomCallback(keras.callbacks.Callback):
    def on_train_begin(self, logs=None):
        print("훈련을 시작합니다.")

    def on_train_end(self, logs=None):
        print("훈련을 종료합니다.")

    def on_epoch_end(self, epoch, logs=None):
        if(dnn.repeat <= 100):
          keys = list(logs.keys())

          log_string = ''
          for key in keys:
            if key is 'loss':
              log_string = f"[오차: {round(logs[key], 4)}]"
            elif key is 'accuracy':
              log_string += f"[정확도: {round(logs[key], 4)}]"

          print(f"반복 훈련 종료 : {epoch}/{dnn.repeat} {log_string}")

    
def train(x, y, repeat=5):

  dnn.repeat = repeat
  
  batch_size = 20
  dnn.model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(512, input_dim=1, activation='relu'),
    tf.keras.layers.Dense(256, input_dim=1, activation='relu'),
    tf.keras.layers.Dense(128, input_dim=1, activation='relu'),
    tf.keras.layers.Dense(64, input_dim=1, activation='relu'),
    tf.keras.layers.Dense(1)
  ])

  dnn.model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics = ['accuracy'])

  print('딥러닝 모델 설정이 완료되었습니다.')

  history = dnn.model.fit(x, y, 
                epochs=repeat, 
                batch_size=batch_size, 
                callbacks=[CustomCallback()],
                verbose=0)

  return history

def predict(x):
  predictions = dnn.model.predict([x])
  return predictions[0]
  
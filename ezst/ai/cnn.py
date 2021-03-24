import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import numpy as np

class CNN:
  pass

cnn = CNN()


class CustomCallback(keras.callbacks.Callback):
    def on_train_begin(self, logs=None):
        print("훈련을 시작합니다.")

    def on_train_end(self, logs=None):
        print("훈련을 종료합니다.")

    def on_epoch_end(self, epoch, logs=None):
        keys = list(logs.keys())

        log_string = ''
        for key in keys:
          if key is 'accuracy':
            log_string = f"[정확도: {round(logs[key], 4)}]"

        print(f"반복 훈련 종료 : {epoch}/{cnn.repeat} {log_string}")

    
def train(train_dir, repeat=5):

  cnn.repeat = repeat
  cnn.categories = os.listdir( train_dir )

  data_count = 0
  for category in cnn.categories:
    files = os.listdir(os.path.join(train_dir, category))
    data_count += len(files)

  train_datagen = ImageDataGenerator( rescale = 1.0/255. )
  
  batch_size = 20
  train_generator = train_datagen.flow_from_directory(train_dir,
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    target_size=(150, 150))

  
  cnn.train_generator = train_generator
  cnn.class_count = len(train_generator.class_indices)
  

  cnn.model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(cnn.class_count, activation='softmax')
  ])

  cnn.model.compile(optimizer=RMSprop(lr=0.001),
              loss='categorical_crossentropy',
              metrics = ['accuracy'])

  print('딥러닝 모델 설정이 완료되었습니다.')

  history = cnn.model.fit(train_generator,
                    steps_per_epoch=data_count / batch_size,
                    epochs=repeat,
                    callbacks=[CustomCallback()],
                    verbose=0)

  return history

def predict(target_path):
  img=image.load_img(target_path , target_size=(150, 150))
  x=image.img_to_array(img)
  x=np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = cnn.model.predict(images, batch_size=20)
  index = np.argmax(classes[0])

  labels = (cnn.train_generator.class_indices)
  labels = dict((v,k) for k,v in labels.items())

  return labels[index]
  
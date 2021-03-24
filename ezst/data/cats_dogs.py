import os
import zipfile
import requests

base_dir = 'cats_dogs'
cats_folder = os.path.join('cats_dogs', 'cats')
dogs_folder = os.path.join('cats_dogs', 'dogs')

cat_fnames = []
dog_fnames = []

cats_path = []
dogs_path = []
  

def load():
  save_path = './cats_dogs.zip'
  url = 'https://www.dropbox.com/s/1sj4fxry2nhwod6/cats_dogs.zip?dl=1'
  r = requests.get(url, stream=True)
  with open(save_path, 'wb') as fd:
      for chunk in r.iter_content(chunk_size=128):
          fd.write(chunk)

  local_zip = 'cats_dogs.zip'

  zip_ref = zipfile.ZipFile(local_zip, 'r')

  zip_ref.extractall('./')
  zip_ref.close()

  os.remove("cats_dogs.zip")

  cat_fnames = os.listdir( cats_folder )
  dog_fnames = os.listdir( dogs_folder )

  for fname in cat_fnames:
    cats_path.append(os.path.join(cats_folder, fname))

  for fname in dog_fnames:
    dogs_path.append(os.path.join(dogs_folder, fname))



    
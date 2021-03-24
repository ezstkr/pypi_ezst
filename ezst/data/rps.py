import os
import zipfile
import requests

base_dir = 'rps'
paper_folder = os.path.join('rps', 'paper')
rock_folder = os.path.join('rps', 'rock')
scissors_folder = os.path.join('rps', 'scissors')

paper_fnames = []
rock_fnames = []
scissors_fnames = []

paper_path = []
rock_path = []
scissors_path = []
  

def load():
  save_path = './rps.zip'
  url = 'https://storage.googleapis.com/laurencemoroney-blog.appspot.com/rps.zip'
  r = requests.get(url, stream=True)
  with open(save_path, 'wb') as fd:
      for chunk in r.iter_content(chunk_size=128):
          fd.write(chunk)

  local_zip = 'rps.zip'

  zip_ref = zipfile.ZipFile(local_zip, 'r')

  zip_ref.extractall('./')
  zip_ref.close()

  os.remove("rps.zip")

  paper_fnames = os.listdir( paper_folder )
  rock_fnames = os.listdir( rock_folder )
  scissors_fnames = os.listdir( scissors_folder )

  for fname in paper_fnames:
    paper_path.append(os.path.join(paper_folder, fname))

  for fname in rock_fnames:
    rock_path.append(os.path.join(rock_folder, fname))

  for fname in scissors_fnames:
    scissors_path.append(os.path.join(scissors_folder, fname))



    
import os
import zipfile
import requests

base_dir = 'nahon'


def load():
  save_path = './nahon.zip'
  url = 'https://www.dropbox.com/s/v9mnnv1qyg3idol/nahon.zip?dl=1'
  r = requests.get(url, stream=True)
  with open(save_path, 'wb') as fd:
      for chunk in r.iter_content(chunk_size=128):
          fd.write(chunk)

  local_zip = 'nahon.zip'

  zip_ref = zipfile.ZipFile(local_zip, 'r')

  zip_ref.extractall('./')
  zip_ref.close()
  
  os.remove("nahon.zip")
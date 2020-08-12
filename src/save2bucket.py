import os
import yaml
from google.cloud import storage

config_path = '../config.yaml'
with open(config_path, 'r') as f:
    configs = yaml.load(f, Loader = yaml.FullLoader)
bucket_name = configs['server']['bucket-name']

client = storage.Client()
bucket = client.get_bucket(bucket_name)
   
def save(filepath):
    filename = os.path.basename(filepath)
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename=filepath)
    return blob.public_url

if __name__ == "__main__":
    filepath = ""
    save(filepath)

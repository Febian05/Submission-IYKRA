import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'prismatic-cider-363006-cec37421fdb6.json'

storage_client = storage.Client()

import urllib.request

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    try:
        file = urllib.request.urlopen(source_file_name)
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(file.read(), content_type='image/jpg')
        return True
    
    except Exception as e:
        return False

project_id = 'prismatic-cider-363006'
bucket_name = 'fellowship_data_bucket-777'
destination_blob_name = 'upload33.test'

source_file_name = 'https://upload.wikimedia.org/wikipedia/commons/b/b4/Donald_Trump_%2843627683740%29.jpg'

# Run Function
upload_blob(bucket_name, source_file_name, destination_blob_name)
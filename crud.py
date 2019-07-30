from google.cloud import storage
import os


storage_client = storage.Client()
def blobs_list(bucket_name):
   audio_files = []
   for f in storage_client.list_blobs(bucket_name): 
      audio_files.append(os.path.splitext(f.name))
   return audio_files

def blob_info(bucket_name, blob_name):
   bucket = storage_client.get_bucket(bucket_name)
   blob = bucket.get_blob(blob_name)
   return blob

def blob_exists(bucket_name, blob_name):
   bucket = storage_client.get_bucket(bucket_name)
   blob = bucket.blob(blob_name)
   return blob.exists()

def upload_blob(bucket_name, source_file_name, destination_blob_name):
   bucket = storage_client.get_bucket(bucket_name)
   blob = bucket.blob(destination_blob_name)

   blob.upload_from_filename(source_file_name)    
   return blob 

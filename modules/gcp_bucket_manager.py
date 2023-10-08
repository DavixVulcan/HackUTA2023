from google.cloud import storage
from modules import img2img_api
import json
import os

# Authorize admin account
PATH = os.path.join(os.getcwd() , 'hackuta2023-401318-15a9707a7cf6.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = PATH

# Connect to bucket
storage_client = storage.Client(PATH)
bucket = storage_client.get_bucket('hackuta2023-image-bucket')

# Get image url from file name
def get_image_url(file_name):
    return "http://hackuta2023-image-bucket.storage.googleapis.com/" + file_name

# Take image path as input, return url of final image in bucket
def process_image(file_name, prompt = None, seed = None):
    # Upload first image to bucket
    file_path = os.path.join(os.getcwd(), file_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_path)

    # Pass image url to img2img and cache result
    output_file_name = img2img_api.get_api_image(get_image_url(file_name), prompt, seed)

    # Upload result image to bucket
    output_file_path = os.path.join(os.getcwd(), output_file_name)
    blob = bucket.blob(output_file_name)
    blob.upload_from_filename(output_file_path)

    # Return result image url
    return get_image_url(output_file_name)
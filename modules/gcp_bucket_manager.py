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
    url = "http://storage.googleapis.com/hackuta2023-image-bucket/" + file_name +"?authuser=1"
    return url

# Upload image to cloud bucket, return image url
def push_image(file_name):
    # Upload first image to bucket
    file_path = os.path.join(os.getcwd(), file_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_path)

    # Pass image url to img2img and return output file name
    return get_image_url(file_name)

# Take image path url and AI params as input, return url of final image in bucket
def process_image(img_url, prompt = None, seed = None):
    # Process image and return output file name
    file_name = img2img_api.get_api_image(img_url, prompt, seed)

    # Upload result image to bucket
    file_path = os.path.join(os.getcwd(), file_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_path)

    # Return result image url
    return get_image_url(file_name)
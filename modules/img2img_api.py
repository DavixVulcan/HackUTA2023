
#Importing os environment variables
import os
from dotenv import load_dotenv

load_dotenv('.env')
api_key = os.getenv('API_TOKEN')
os.environ["REPLICATE_API_TOKEN"] = api_key

import replicate

from urllib.request import urlretrieve

def cache_image(url):
    if not os.path.exists( "img_stable_api/img0.png"):
        urlretrieve(url,   "img_stable_api/img0.png")
    elif not os.path.exists(  "img_stable_api/img1.png"):
        urlretrieve(url,   "img_stable_api/img1.png")
    elif not os.path.exists(  "img_stable_api/img2.png"):
        urlretrieve(url,   "img_stable_api/img2.png")
    else:
        os.remove(  "img_stable_api/img0.png")
        os.rename(  "img_stable_api/img1.png",   "img_stable_api/img0.png")
        os.rename(  "img_stable_api/img2.png",   "img_stable_api/img1.png")
        urlretrieve(url,   "img_stable_api/img2.png")

def get_api_image(image, prompt = "fantasy setting", seed = None):

    image = open(image, "rb")
    # Generate an image and assign it to the output variable
    if seed is None:
        url = replicate.run(
            "stability-ai/stable-diffusion-img2img:15a3689ee13b0d2616e98820eca31d4c3abcd36672df6afce5cb6feb1d66087d",
            input = {
                "image": image,
                "prompt": prompt
            }
        )[0]
    else:
        url = replicate.run(
            "stability-ai/stable-diffusion-img2img:15a3689ee13b0d2616e98820eca31d4c3abcd36672df6afce5cb6feb1d66087d",
            input = {
                "image": image,
                "prompt": prompt,
                "seed": seed
            }
        )[0]

    # Check for an API error [TODO]


    # Download the image from the url to the img_stable_api folder
    # cache_image(url)
    cache_image(url)
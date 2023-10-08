
#Importing os environment variables
import os
from dotenv import load_dotenv

load_dotenv('.env')
api_key = os.getenv('API_TOKEN')
os.environ["REPLICATE_API_TOKEN"] = api_key

import replicate

def get_prompt(image):
    output = replicate.run(
        "methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5",
        input={
            "image": image
            })
    print(output)
    return output
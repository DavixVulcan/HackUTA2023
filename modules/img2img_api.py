import replicate
import os
from urllib.request import urlretrieve

#urlretrieve(url, "../img_stable_api/img0")

def cache_image(url):
    if not os.path.exists("../img_stable_api/img0"):
        urlretrieve(url, "../img_stable_api/img0")
    elif not os.path.exists("../img_stable_api/img1"):
        urlretrieve(url, "../img_stable_api/img1")
    elif not os.path.exists("../img_stable_api/img2"):
        urlretrieve(url, "../img_stable_api/img2")
    else:
        os.remove("../img_stable_api/img0")
        os.rename("../img_stable_api/img1", "../img_stable_api/img0")
        os.remove("../img_stable_api/img1")
        os.rename("../img_stable_api/img2", "../img_stable_api/img1")
        urlretrieve(url, "../img_stable_api/img2")

def get_api_image(image, prompt = "A fantasy setting, trending on artstation", seed = None):
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
    #url = "https://www.dice.com/binaries/medium/content/gallery/dice/insights/2020/03/shutterstock_1375882658-e1583354582236.jpg"

    # Check for an API error [TODO]


    # Download the image from the url to the img_stable_api folder
    cache_image(url)
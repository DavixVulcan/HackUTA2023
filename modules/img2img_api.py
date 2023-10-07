import replicate
from urllib.request import urlretrieve

def get_api_image(image, prompt, seed):
    # Generate an image and assign it to the output variable
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
    urlretrieve(url, "../img_stable_api/img0")

#How to import your module from the modules folder
from modules import test, img2img_api
import os

#Used to inport env API token
# from dotenv import load_dotenv
# load_dotenv('.env')

os.environ["REPLICATE_API_TOKEN"] = "r8_XEtr5rDa65qpC1Yj9iLI1xUfhqcABAg2b5j8p"

print(os.getenv('REPLICATE_API_TOKEN'))
#Call module using modulename.modulefunction()
test.initial_test()
img2img_api.get_api_image("img_camera_out/dummy_img.jpg")
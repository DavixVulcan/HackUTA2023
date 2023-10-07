
#How to import your module from the modules folder
from modules import test, img2img_api

#Used to inport env API token
from dotenv import load_dotenv
load_dotenv('.env')

#Call module using modulename.modulefunction()
test.initial_test()
img2img_api.get_api_image("img_camera_out/dummy_img.jpg")
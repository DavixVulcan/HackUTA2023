
#How to import your module from the modules folder
from modules import test, img2img_api


#Call module using modulename.modulefunction()
# test.initial_test()
img2img_api.get_api_image("img_camera_out/dummy_img.jpg")
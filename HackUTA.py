
#How to import your module from the modules folder
from modules import test, img2img_api, qr_generator


#Call module using modulename.modulefunction()
# test.initial_test()

whiler = True
while(whiler):
    #take_picture("img_camera_out/MainPic.png")
    #imgurl1 = push_img("img_camera_out/MainPic.png")
    img2img_api.get_api_image("img_camera_out/PNG_Test.png", "Spider-Man hanging from the side of the frame")
    #img2img_api.get_api_image("imgurl1", "Spider-Man hanging from the side of the frame")
    #img2img_api.get_api_image("imgurl1", "Spider-Man hanging from the side of the frame")
    #img2img_api.get_api_image("imgurl1", "Spider-Man hanging from the side of the frame")

    

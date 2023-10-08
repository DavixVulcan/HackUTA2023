
#How to import your module from the modules folder
from modules import test, img2img_api, qr_generator, gcp_bucket_manager, img2text_api


#Call module using modulename.modulefunction()
# test.initial_test()

whiler = True
# while(whiler):
# while(whiler):
    #take_picture("img_camera_out/MainPic.png")

camera_image_url = gcp_bucket_manager.push_image("img_camera_out/raul.png")
img2text_api.get_prompt(camera_image_url)
output_image_url_1 = gcp_bucket_manager.process_image(camera_image_url, "Student in a classroom, realistic, high definition")
    #img2img_api.get_api_image("imgurl1", "Spider-Man hanging from the side of the frame")
    #img2img_api.get_api_image("imgurl1", "Spider-Man hanging from the side of the frame")
    #img2img_api.get_api_image("imgurl1", "Spider-Man hanging from the side of the frame")
qr_generator.create_qr(output_image_url_1)
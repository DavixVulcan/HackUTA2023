
#How to import your module from the modules folder
from modules import test, img2img_api, qr_generator, gcp_bucket_manager, img2text_api, camera_main_task
import json


#Call module using modulename.modulefunction()
# test.initial_test()
whiler = True
while(whiler):
    camera_main_task.take_picture("img_camera_out/MainPic.png")
    camera_image_url = gcp_bucket_manager.push_image("img_camera_out/MainPic.png")
    base_prompt = img2text_api.get_prompt(camera_image_url)
    base_prompt = base_prompt.strip()
    # print(base_prompt)


    f = open("prompt_appends.json")
    array_urls = json.load(f)
    for i, y in array_urls.items():
        # print(camera_image_url)
        print(y)
        output_image_url_1 = gcp_bucket_manager.process_image(camera_image_url, base_prompt + ", " + y)
        #img2img_api.get_api_image("imgurl1", "Spider-Man hanging from the side of the frame")
        #img2img_api.get_api_image("imgurl1", "Spider-Man hanging from the side of the frame")
        #img2img_api.get_api_image("imgurl1", "Spider-Man hanging from the side of the frame")
        qr_generator.create_qr(output_image_url_1, i)
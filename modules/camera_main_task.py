# Main function of the ArduCam Hawkeye
import os
def take_picture(location):
    os.system("libcamera-still -t 4000 --viewfinder-width 1920 --viewfinder-height 1080 --width 1280 --height 720 --mode 1280:720 -o "+location)

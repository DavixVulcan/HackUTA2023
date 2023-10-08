# Main function of the ArduCam Hawkeye
import os
def take_picture(location):
    os.system("libcamera-jpeg -t 4000 --viewfinder-width 2312 --viewfinder-height 1736 --width 1920 --1080 --mode 1920:1080 -o "+location)

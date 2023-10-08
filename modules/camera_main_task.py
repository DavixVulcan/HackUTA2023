# Main function of the ArduCam Hawkeye
import os
def take_picture(location):
    os.system("libcamera-still -e png -t 4000 --viewfinder-width 1920 --viewfinder-height 1080 --width 1920 --height 1080 --mode 1920:1080 -o "+location)

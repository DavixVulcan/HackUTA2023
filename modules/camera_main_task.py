# Main function of the ArduCam Hawkeye
import os
def take_picture(location):
    os.system("libcamera-jpeg -t 4000 --viewfinder-width 2312 --viewfinder-height 1736 -o "+location+" -q 25")

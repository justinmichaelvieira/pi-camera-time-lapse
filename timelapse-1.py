from datetime import datetime
import os
from picamera import PiCamera
from sys import argv
from time import sleep

WAIT_TIME = int(argv[1]) if len(argv) > 1 else 30
TOTAL_PICS = int(argv[2]) if len(argv) > 2 else 10
MAIN_DIR = '/home/pi/camera-experiments/timelapse-1'
SUB_DIR = datetime.now().strftime('%d-%m-%y-%H-%M-%S')

camera = PiCamera()

# create subdir
os.mkdir(f'{MAIN_DIR}/{SUB_DIR}')

# capture picture, then sleep for WAIT_TIME
for i in range(TOTAL_PICS):
    FILE_NAME = datetime.now().strftime('%H-%M-%S') + '.jpg'
    camera.capture(f'{MAIN_DIR}/{SUB_DIR}/{FILE_NAME}')                                                                       
    sleep(WAIT_TIME)


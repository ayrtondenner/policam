import os
import cv2

FILMED_VIDEOS_DICT = './videos/filmed'
PRINTS_DICT = './prints'

filmed_videos_list = os.listdir(FILMED_VIDEOS_DICT)

for filmed_video in filmed_videos_list:
    vidcap = cv2.VideoCapture(os.path.join(FILMED_VIDEOS_DICT, filmed_video))
    vidcap_folder = os.path.join(PRINTS_DICT, filmed_video.replace('.mp4', ''))

    if os.path.exists(vidcap_folder):
        for frame in os.listdir(vidcap_folder):
            os.remove(os.path.join(vidcap_folder, frame))
        os.rmdir(vidcap_folder)

    os.makedirs(vidcap_folder)

    count = 0
    success = True

    while success:
        success, image = vidcap.read()
        if count % 25 == 0:
            cv2.imwrite(os.path.join(vidcap_folder, "frame%d.jpg" % count), image)
        count += 1
from GUI import *
from flash_detect import detect_flashing_video


slider = create_slider()
threshold = get_val()
# print("Here is val: ", threshold)
video = select_video_file()

if detect_flashing_video(video, threshold):
    show_warning_message()
else:
    show_ok_message()





from GUI import *
from flash_detect import detect_flashing_video
from cam_shake import detect_camera_shake

root = create_root()
slider = create_slider(root)
root.mainloop()
threshold = get_val()

video = select_video_file(root)


# print("Here is val: ", threshold)

is_flashing = detect_flashing_video(video, threshold)
is_cam_shake = detect_camera_shake(video)

if is_flashing or is_cam_shake:
    if is_flashing:
        print("This video contains flashing")
    if is_cam_shake:
        print("This video contains a lot of camera movement")
    
    show_warning_message(root)
   
else:
    show_ok_message(root)

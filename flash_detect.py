import cv2
import numpy as np

def detect_flashing_video(video_path, threshold=30):
    # Load the video
    # print('This is the Frequency: %d Hrtz'%threshold)
    video = cv2.VideoCapture(video_path)

    # Initialize variables
    last_frame_avg = None
    frame_count = 0
    contains_flash = False

    while True:
        # Read the next frame
        ret, frame = video.read()

        # If the frame could not be read, then we have reached the end of the video
        if not ret:
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate the average brightness of the grayscale frame
        current_frame_avg = np.average(gray_frame)

        # If this is not the first frame
        if last_frame_avg is not None:
            # Calculate the absolute difference in brightness between the current and last frame
            diff = abs(current_frame_avg - last_frame_avg)

            # If the difference exceeds the threshold, raise an alert
            if diff > threshold:
                # print(f"Alert: Sudden change in brightness detected at frame {frame_count}")
                contains_flash = True
                break

        # Update the last frame average brightness
        last_frame_avg = current_frame_avg

        # Increment the frame count
        frame_count += 1

    # Release the video file
    video.release()
    return contains_flash

# Usage:
# detect_flashing_video('path_to_your_video.mp4')

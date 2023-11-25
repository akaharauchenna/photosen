import cv2
import numpy as np

def detect_camera_shake(video_path, threshold=7.5):
    # Load the video
    cap = cv2.VideoCapture(video_path)

    # Get the first frame
    ret, prev_frame = cap.read()
    i = 1
    while True:
        # Read the next frame
        ret, curr_frame = cap.read()

        if not ret:
            break

        # Convert the frames to grayscale
        prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

        # Calculate optical flow
        flow = cv2.calcOpticalFlowFarneback(prev_gray, curr_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # Compute the magnitude and angle of the 2D vectors
        magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        # print(f"{i} Checking")
        # i += 1

        # If the average magnitude exceeds the threshold, return True
        if np.mean(magnitude) > threshold:
            return True

        # Update the previous frame
        prev_frame = curr_frame.copy()
    print("Done")
    # If no camera shake was detected, return False
    return False



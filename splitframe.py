

import cv2
import os

# Path to your video file
video_path = "scene 5 edited.mov"

# Output folder for frames
output_folder = "framestheatre"
os.makedirs(output_folder, exist_ok=True)

# Open the video
cap = cv2.VideoCapture(video_path)

frame_count = 0

while True:
    ret, frame = cap.read()  # Read one frame
    if not ret:
        break  # End of video
    
    # Save the frame as an image
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)
    
    print(f"Saved {frame_filename}")
    frame_count += 1

cap.release()
print("Done! All frames saved.")

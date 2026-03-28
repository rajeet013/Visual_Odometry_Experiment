import cv2
import os
import sys

def extract_vo_dataset(video_path, output_folder):
    # 1. Check if the file actually exists before trying to open it
    if not os.path.isfile(video_path):
        print(f"Error: The file '{video_path}' was not found.")
        print(f"Current Working Directory: {os.getcwd()}")
        return

    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video = cv2.VideoCapture(video_path)
    
    # 2. Check if OpenCV can actually decode the video
    if not video.isOpened():
        print(f"Error: OpenCV could not open/decode '{video_path}'.")
        print("Check if you have the necessary video codecs installed.")
        return

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Success! Found {total_frames} frames. Starting extraction...")

    count = 0
    while True:
        success, frame = video.read()
        
        if not success:
            break
        
        # Save as PNG for Visual Odometry quality
        frame_name = f"frame_{count:06d}.png" 
        save_path = os.path.join(output_folder, frame_name)
        
        cv2.imwrite(save_path, frame)
        
        count += 1
        if count % 10 == 0: # Updated to update more frequently
            sys.stdout.write(f"\rExtracted: {count}/{total_frames} frames...")
            sys.stdout.flush()

    video.release()
    print(f"\nExtraction complete. {count} frames saved to '{output_folder}'")

# --- USE AN ABSOLUTE PATH IF IT STILL FAILS ---
# Example: r"F:\PycharmProjects\Visual Odometry Project\Video.mp4"
extract_vo_dataset("Video.mp4", "vo_dataset_frames")
import os
import shutil

folder_path = "C:/Users/Divyanshu Jangid/Desktop/automation project bj"

image_folder = os.path.join(folder_path, "images")
pdf_folder = os.path.join(folder_path, "pdfs")
video_folder = os.path.join(folder_path, "videos")
audio_folder = os.path.join(folder_path, "audio")

os.makedirs(image_folder, exist_ok=True)
os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(video_folder, exist_ok=True)
os.makedirs(audio_folder, exist_ok=True)
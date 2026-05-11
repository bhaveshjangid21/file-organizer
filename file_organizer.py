import os
import shutil

folder_path ="C:\\Users\\Divyanshu Jangid\\Desktop\\automation project bj"
print(os.path.exists(folder_path))
files = os.listdir(folder_path)

os.makedirs(os.path.join(folder_path,"images"),exist_ok=True)
os.makedirs(os.path.join(folder_path,"pdfs"),exist_ok=True)
os.makedirs(os.path.join(folder_path,"videos"),exist_ok=True)
os.makedirs(os.path.join(folder_path,"audio"),exist_ok=True)

for file in files:
    file_path = os.path.join(folder_path,file)
    if os.path.isfile(file_path):

        if file.endswith(".jpg"):
            shutil.move(file_path, os.path.join(folder_path, "images", file))
            print("moved image: ",file)
        elif file.endswith(".pdf"):
            shutil.move(file_path, os.path.join(folder_path,"pdfs",file))
            print("moved pdf:" , file)
        elif file.endswith(".mp4"):
            shutil.move(file_path,os.path.join(folder_path,"videos",file))
            print("moved video:",file)
        elif file.endswith(".mp3"):
            shutil.move(file_path,os.path.join(folder_path,"audio",file))
            print("moved audio:",file)
        
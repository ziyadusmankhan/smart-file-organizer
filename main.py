import os
import shutil


base_path = "/Users/Apple/PYTHON_PROJECTS" # enter the path of the place where the img, vids and doc are in order to organize


files = os.listdir(base_path) # list of all the files in directory


image_ext = [".jpg", ".png", ".jpeg"] # storing the extension of different formats in their specified list 
video_ext = [".mp4", ".mkv"]
doc_ext = [".pdf", ".docx", ".txt"]


images_folder = os.path.join(base_path, "Images") 
videos_folder = os.path.join(base_path, "Videos")
documents_folder = os.path.join(base_path, "Documents")


os.makedirs(images_folder, exist_ok=True)
os.makedirs(videos_folder, exist_ok=True) # creating the folders if they dont exist 
os.makedirs(documents_folder, exist_ok=True)

# no for moving into their specific folders
for file in files:


    source_path = os.path.join(base_path, file)

    
    if os.path.isdir(source_path):
        continue

    
    if file.endswith(tuple(image_ext)):
        shutil.move(source_path, os.path.join(images_folder, file))
        print(f"Moved Image: {file}")

    
    elif file.endswith(tuple(video_ext)):
        shutil.move(source_path, os.path.join(videos_folder, file))
        print(f"Moved Video: {file}")

    
    elif file.endswith(tuple(doc_ext)):
        shutil.move(source_path, os.path.join(documents_folder, file))
        print(f"Moved Document: {file}")

print("Files organized successfully!")


"""
THE END (*(*(*(*(*(*(*)))))))


"""
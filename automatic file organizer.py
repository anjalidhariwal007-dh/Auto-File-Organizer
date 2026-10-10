import os
import shutil

folder_path=input("Enter folder path to organize: ")

file_types={
    "Images":[".png",".jpg",".lpeg",".gif"],
    "Document":[".pdf",".docx",".txt"],
    "Videos":[".mp4",".mkv"],
    "Music":[".mp3",".wav"],
    "Others":[]
}

for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder),exist_ok=True)

for file in os.listdir(folder_path):
    file_path= os.path.join(folder_path,file)

    if os.path.isfile(file_path):
        moved=False
        for folder, extensions in file_types.items():
            if any(file.endswitch(ext) for ext in extensions):
                shutil.move(file_path,os.path.join(folder_path,folder, file))
                moved= True 
                break
            if not moved:
                shutil.move(file_path,os.path.join(folder_path,"others",file))

print("file organised successfully! :)")
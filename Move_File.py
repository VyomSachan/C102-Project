import os
import shutil

source = r"C:\Users\Sachan_Kids\Downloads\C102-ProjAssets"
destination = r"D:\Vyom\Coding\WhiteHat\Project solutions\(WHJ Project Module 4) Python\C102-Project"

list_of_files = os.listdir(source)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if extension == " ":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = source + '/' + file_name
        path2 = destination + '/' + "Document_Files"
        path3 = destination + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + " ...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + " ...")
            shutil.move(path1, path2)
import time
import os
import shutil

def removeFiles(path,days):
    now = time.time()
    daysinsec = days * 86400 
    if os.path.exists(path) :
        for root, dirs, files in os.walk(path):
            for name in files:
                file_path = os.path.join(root, name)
                if os.stat(file_path).st_mtime < now - daysinsec:
                    os.remove(file_path)
                    print("File Removed: ", name)
            for name in dirs:
                dir_path= os.path.join(root, name)
                if os.stat(dir_path).st_mtime < now - daysinsec:
                    shutil.rmtree(dir_path)
                    print("Directory Removed: ", name)
    else: 
        print("Path not exists!!!")


path = input("Enter the path of the directory from which you want to delete the old files: ")
days = int(input("Enter the number of days earlier file you want to delete: "))
removeFiles(path, days)
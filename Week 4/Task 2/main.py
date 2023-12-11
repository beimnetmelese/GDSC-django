import os
import datetime
import time

task = """Create a Python script that identifies and collects files (both created and modified) in the last 24 hours from the current directory. Update these files in some way and move them to a folder named "last_24hours."

Requirements:

Listing Files:
Use the os module to list all files in the current directory.
Identification of Files:
Implement a function to determine whether a file has been created or modified in the last 24 hours.
Consider both the modification time (st_mtime) and creation time (st_ctime) of the file.

Update Files:
Create a function to update the identified files. For example, append a timestamp to the content of each file.

Create "last_24hours" Folder:
Check if a folder named "last_24hours" exists. If not, create it using the os module.

Move Files:
Move the identified and updated files to the "last_24hours" folder using different method
Combine the functions to achieve the main objective.
"""
text = """Feel free to seek clarification on any part of the task. 
The primary goal is to enhance your understanding of file handling, time-based operations, and module usage in Python.
"""
with open("C:\\Users\\Lenovo\\Documents\\Week 4\\task 2\\task.txt", "w") as file:
    file.write(task)

with open("C:\\Users\\Lenovo\\Documents\\Week 4\\task 2\\text.txt", "w") as files:
    files.write(text)

file_list = os.listdir("C:\\Users\\Lenovo\\Documents\\Week 4\\task 2")
if os.path.exists("C:\\Users\\Lenovo\\Documents\\Week 4\\last_24hours"):
    print("The file exists")
else:
    os.makedirs("C:\\Users\\Lenovo\\Documents\\Week 4\\last_24hours")
for i in file_list:
    text_time = os.path.getctime(f"C:\\Users\\Lenovo\\Documents\\Week 4\\task 2\\{i}")
    text_ctime = datetime.datetime.strptime(time.ctime(text_time), "%a %b %d %H:%M:%S %Y")
    creation_time = datetime.datetime.now() - text_ctime
    text_time2 = os.path.getmtime(f"C:\\Users\\Lenovo\\Documents\\Week 4\\task 2\\{i}")
    text_mtime = datetime.datetime.strptime(time.ctime(text_time2), "%a %b %d %H:%M:%S %Y")
    modification_time = datetime.datetime.now() - text_mtime
    if creation_time <= datetime.timedelta(hours=24) or modification_time <= datetime.timedelta(hours=24):
        os.replace(f"C:\\Users\\Lenovo\\Documents\\Week 4\\task 2\\{i}",f"C:\\Users\\Lenovo\\Documents\\Week 4\\last_24hours\\{i}")
        print(f"{i} was moved to last 24 hours folder")


     



   

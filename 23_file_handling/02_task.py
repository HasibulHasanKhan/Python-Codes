import os

### 
# cwd = os.getcwd()
# print("Current working Directory:", cwd)

### Change directory :
# os.chdir(".././data")
# print("Changed Directory:", os.getcwd())

### List files and directories :
files = os.listdir("")
print("Files and Folders:", files)

### Create directory :
os.mkdir("new_folder")
os.makedirs("parent/child")
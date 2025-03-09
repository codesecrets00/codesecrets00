import os 
print(os.name)
print(os.getcwd())
path = "/storage/emulated/0/DCIM/folder1"
path2 = "/"
print(os.listdir(path))
print(os.listdir(path))
file = "text.txt"

os.system("ls -la")
if os.path.exists(file):
    os.remove(file)
    print("File deleted succesfully")
else:
    print("file not found")
    os.system("touch text.txt")
import os


path_image="images"
def func(path):
    l=[]
    it=os.scandir(path)
    for entry in it:
        if entry.is_file() and entry.name[:4]=="deep":
            l.append(entry.name)
    return l

if(len(func(path_image))==2):
    print("There are 2 files starting with deep in the image directory")



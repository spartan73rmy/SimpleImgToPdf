import os
import PIL.Image
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

directory = folder_selected

print(directory)

for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        currentDir=os.path.join(root, subdirectory)
        items = os.listdir(currentDir)
        print(currentDir)            
        print(items)
        for item in items:
            extension = os.path.splitext(item)[1]
            if(extension == ".jpg" or extension == ".png"):
                image1 = PIL.Image.open(currentDir +"/" + item)
                print(image1)
                im1 = image1.convert('RGB')
                print(item)
                print(item.split('.')[0])
                im1.save(currentDir + "/" + item.split('.')[0] + '.pdf')
print("Finalizado")

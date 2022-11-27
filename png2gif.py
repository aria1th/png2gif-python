from PIL import Image, ImageSequence
import os
import glob
from ast import literal_eval

try:
    size = literal_eval("Input image size to be resized (ex:232->232x232)\n")
except:
    size = 232
    print("Using default size 232x232\n")
base_path = input("First image to iterate(Optional, or leave it empty)\n")

folder_path = input('Folder path to merge\n')

frames = []
try:
    if len(base_path)>3:
        frames.append(Image.open(base_path).resize((size,size)))
except:
    print("Cannot find initial image!\n")

for frame in sorted(glob.glob(folder_path + '\\*.png'), key = lambda b:int(''.join(a for a in b if a.isnumeric()))):
    frames.append(Image.open(frame).resize((size,size)))

if len(base_path) <= 3:
    base_path = 'a.gif'
frames[0].save(folder_path +'\\'+ base_path.split('\\')[-1].split('.')[0] + '.gif',
               format = 'GIF',
               append_images = frames[1:],
               save_all = True,
               duration = 150,
               loop = 1
               )

print(r"File saved as {}".format(folder_path +'\\'+ base_path.split('\\')[-1].split('.')[0] + '.gif'))

import os
import shutil
import gui

folderpath = gui.source 

os.chdir(folderpath)

cwd = os.getcwd()
print('Current working directory: ', cwd)

# Getting all file names in a list

dirlist = os.listdir()
# print(dirlist)

# Getting extensions in a list

extlist = []
for file in dirlist:
    if os.path.isfile(file):
        ext = file.split('.')[-1]
        extlist.append(ext.upper())
extlist = set(extlist)  # Removing Duplicate extensions
# print(extlist)

#Main Sorting Logic
for ex in extlist:  
    
    if not os.path.exists(folderpath + "\\" + ex + ' files'):
        os.makedirs(folderpath + "\\" + ex + ' files')
        for file in dirlist:
            if os.path.isfile(file) and ex.lower() in file:
                shutil.move(file, folderpath + "\\" + ex + ' files')
    else:
        for file in dirlist:
            if os.path.isfile(file) and ex.lower() in file:
                shutil.move(file, folderpath + "\\" + ex + ' files')




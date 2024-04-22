import os, shutil

#defining the path
path=r"C:/Users/pc/python/file sorter/"
filename=os.listdir(path)
foldernames=['csv files','text files','png files']

#creating the folders
for loop in range(0,3):
    if not os.path.exists(path+foldernames[loop]):
        os.makedirs(path+foldernames[loop])

#loop to check the files
for file in filename:
    if '.xlsx' in file and not os.path.exists(path+'csv files/'+file):
        shutil.move(path+file,path+'csv files/'+file)
    if '.docx' in file and not os.path.exists(path+'text files/'+file):
        shutil.move(path+file,path+'text files/'+file)
    if '.PNG' in file and not os.path.exists(path+'png files/'+file):
        shutil.move(path+file,path+'png files/'+file)
    if '.jfif' in file and not os.path.exists(path+'png files/'+file):
        shutil.move(path+file,path+'png files/'+file)
    if '.png' in file and not os.path.exists(path+'png files/'+file):
        shutil.move(path+file,path+'png files/'+file)
    if '.jpg' in file and not os.path.exists(path+'png files/'+file):
        shutil.move(path+file,path+'png files/'+file)
    
    

     
     
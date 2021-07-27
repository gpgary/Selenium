import os, urllib
from selenium import webdriver

#def download_pic(file_path,file_name):
    

def file_rename(path):
    for file in os.listdir(path):
        print(os.path.splitext(path+file)) 
        file_name = os.path.splitext(file)[0]
        file_extention = os.path.splitext(file)[1]          
        
        if (os.path.isfile(path + file) and (file_extention == '.mp4')):
            os.rename(path + file, path + file_name.upper() + file_extention)
            # Download pic
            if os.path.exists(path + file_name.upper() + '.jpg'):                
                print( file_name + ' image file exist!!!')
            else:
                print ( 'Start download ' + file_name + ' image' )
        else:
            print( file + ' is not video file')        


    
                
    
file_rename('/home/gary/Videos/')
    

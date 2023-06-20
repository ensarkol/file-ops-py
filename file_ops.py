#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
 

def create_file():
    file_path = input("File path:")
    x = int(input("Number of files:")) 
    file_number = range(1,x+1)
    
    while x in file_number:
      
        if x >0:
            new_file = os.open("new_file_{}.txt".format(x), os.O_RDWR|os.O_CREAT)
            print("new_file_{} created".format(x))
            os.chdir(file_path)
            x = x-1
            os.close(new_file)
        
        else:
            return
            
def write_files():
    y = int(input("Number of files for write:"))
    numbers = range(1,y+1)
    for y in numbers:       
        if y >0:
            file_name_2write = os.open("new_file_{}.txt".format(y), os.O_WRONLY)
            os.write(file_name_2write, "new_file_{}.txt".format(y).encode())
            print("Write operation completed successfully for file {}".format(y))   
            y = y-1
            os.close(file_name_2write)
            
def read_files():
    file_name_2read = input("Enter the file name for read:")
    read_file = os.open("{}.txt".format(file_name_2read), os.O_RDONLY)
    caption = os.read(read_file, 1000)
    print(caption.decode())
    
    


    

    
create_file()
write_files()
while True:
    if input("For exit presss 0, For read files press Enter"):
        break
    else:
        read_files()    
        continue

#check is a file is empty or not 
import os 
size = os.stat("test.txt").st_size
if size == 0:
    print(False)
    

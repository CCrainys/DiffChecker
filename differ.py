import sys
import os
import platform

md5="md5"

folder1 = sys.argv[1]
folder2 = sys.argv[2]
dir1 = os.listdir(folder1)
dir2 = os.listdir(folder2)
new_dir1=[]
new_dir2=[]

for file in dir1:
    if(file.startswith(".")):
        continue
    new_dir1.append(file)

for file in dir2:
    if(file.startswith(".")):
        continue
    new_dir2.append(file)
    
for file in new_dir1:
    r1=os.popen('md5 %s'%(os.path.join(folder1,file))).read().strip()[-1]
    r2=os.popen('md5 %s'%(os.path.join(folder2,file))).read().strip()[-1]
    if(r1 == r2):
        print("%s match!"%file)
    else:
        print("warning: %s doesn't match in two side"%file)
        
        

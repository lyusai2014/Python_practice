#!/usr/bin/python

# This program is to remove unuseful direcories

# to practice the os (the operating system interface)


import os
os.mkdir('new_directory')
os.chdir('new_directory')
current_directory=os.getcwd()
print 'the current directory is ',current_directory

os.mkdir('1122')
os.chdir('/home/sxl1036/python')


root_list=[] # to declar an empty list
dir_list=[]

import shutil
shutil.rmtree('new2_directory')

# shutil is high level file/directories operations
for root,dirs,files in os.walk('/home/sxl1036/python/test_directory') :
        print root
        print dirs
        print files
        root_list.append(str(root))
        dir_list.append(str(dirs))
        # list.append() method
print 'the list of all the root is ',root_list
print 'the first root is root_list[0] ',root_list[0]
print 'the second root is root_list[1]',root_list[1]
print 'the list of all the directories is ',dir_list
print 'the first directory is dir_list[0] ',dir_list[0]
print 'the second directory is dir_list[1] ',dir_list[1]
print 'the first directory is dir_list[0][0] ',dir_list[0][0]
# the first index of list is 0.
print 'the length of the list is len(dir_list)',len(dir_list)
# At first to get the list of all direcories.
# a list containing lists dir_list[0] is also a list
print 'the splited string str.split()'
aaaa=dir_list[0].split(' ,') # , as delimiter
print aaaa[0] 
for list_index  in range(len(dir_list[0])) : 
    print 'the list_index  '+str(list_index),dir_list[0][list_index]
    print list_index 
for index in range (len(root_list)) :
   print 'the root list is ' ,root_list[index]

del index
# del the variable after using

for index in range(len(root_list)) :
   # if 'sxl1036' in str(root_list[index]) :
    if 'sxl1036' in root_list[index] and 'pbsjobs' in root_list[index]:
   # python logical operator
     print 'True',root_list[index]
     shutil.rmtree(root_list[index])
    else :
      print 'False'


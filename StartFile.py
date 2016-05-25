import os
from os.path import exists

a = raw_input ("Enter the name of the file that you want to open> ")

if exists(a):
    print "The file exists"
    print "Opening...."
    os.startfile(a)
else:
    print "REDO!"
        

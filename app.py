# -*- coding: utf-8 -*-
"""
2020-09-10

Extract first N lines of each text file in input directory
Place results in the output directory
Move the files from input to archive

ES

0.1 first working
"""

#relative to current directory
strInputDirectory = r".\input"
strOutputDirectory = r".\output"
strArchiveDirectory = r".\archive"


#how many lines of text do we want to keep?
intLineLimit = 20


#for creating archive folder
from datetime import date
today = date.today()
strDate = today.strftime("%Y%m%d") #YYYYMMDD format
#print("strDate =", strDate) #debugging


#for file handling
import os


strPathArchive = os.path.join(strArchiveDirectory, strDate) 
#print('strPathArchive =' + strPathArchive) #debugging    


#list files in a directory with a certain extension
for file in os.listdir(strInputDirectory):
    if file.endswith(".txt"):
        #check filename
        print('file =' + file) #debugging
        
        #filepath of file in input directory
        strFilepathIn = os.path.join(strInputDirectory, file)
        print('strFilepathIn =' + strFilepathIn) #debugging

        #filepath of file in output directory
        strFilepathOut = os.path.join(strOutputDirectory, file)
        print('strFilepathOut =' + strFilepathOut) #debugging

        #filepath for file in archive directory
        strFilepathArchive = os.path.join(strPathArchive, file)
        print('strFilepathArchive =' + strFilepathArchive) #debugging     



        #open file
        intLineCount = 0
        
        
        with open(strFilepathOut, "w") as fileOut:
        
            with open (strFilepathIn, 'rt') as myfile:  #open file for reading              
                # lstLines = myfile.read().splitlines()
                # print(str(lstLines))
                
            
            
                for myline in myfile:              # For each line, read to a string
                    intLineCount += 1
                    if intLineCount < intLineLimit:
                        print(myline) #debugging
                        

                        print(myline.rstrip())
                        
                        
                        #write to output file
                        fileOut.write(myline)
                    else:
                        print("got enough, breaking...")
                        break

        
        #make directory if not already there
        if not os.path.exists(strPathArchive):
            os.makedirs(strPathArchive)        
        
        # #move input file to archive
        # os.replace(strFilepathIn, strFilepathArchive)
        
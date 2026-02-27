#program to read content of a text file
#to open a file for read operation
filev = open("firstfile.txt","r")

# check file is open
if(filev):
        #to read all the content
        data = filev.read()
        #to check file is empty or not
        if(len(data) == 0):
                print("File is empty")
        else:
                print("Contents of file : ")
                print(data)

#close the file
filev.close()

#output
#Contents of file :
#Python is easy.
#I like programming.
#Files are used to store data.
#This is sentence four.
#Sentence five here.
#Sentence six here.
#Sentence seven here.
#Sentence eight here.
#Sentence nine here.
#Sentence ten here.

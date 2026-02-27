#program to write 10 sentences given by user into a text file
#to open a file for write operation
filev = open("firstfile.txt","w")
#----------------------------------------------

print("Enter any 10 sentence (hit Enter key for new sentence): ")
for x in range(10):
        sentence = input()
        #writing the data into the file
        filev.write(sentence)
        print("------------------------------")

print("Data written successfully into the file")
#close the file
filev.close()

#output
#Enter any 10 sentence (hit Enter key for new sentence):
#Python is easy.
#------------------------------
#I like programming.
#------------------------------
#Files are used to store data.
#------------------------------
#This is sentence four.
#------------------------------
#Sentence five here.
#------------------------------
#Sentence six here.
#------------------------------
#Sentence seven here.
#------------------------------
#Sentence eight here.
#------------------------------
#Sentence nine here.
#------------------------------
#Sentence ten here.
#------------------------------
#Data written successfully into the file

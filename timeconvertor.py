second = int(input("Enter time in seconds: "))
#--------------------------------------------
#initializing number of hours and minutes
minutes = 0
hours = 0
if(second >=3600):
    hours = second // 3600 #storing quatient as hours
    second = second%3600 #storing remainder as seconds 
if(second >=60):
    minutes = second // 60 #storing quatient as minutes
    second = second%60 #storing remainder as seconds

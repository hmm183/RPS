#To check rooms boooked under one username
import pickle
found=True
pincode=input("Enter the pincode:")
f=pincode+".dat"
fh=open(f,'rb')
try:
    while True:
        hotel=pickle.load(fh)
        print(hotel)
except EOFError:
    fh.close()
found=False
uname=int(input("Enter the username to search:"))

file=open(f,"rb+")
try:
    while True:
        i=1
        pos=file.tell()
        hotel=pickle.load(file)
        print(hotel)
        while i<120:
            if hotel[i][1]==roll_no:
                print(hotel)
                i=i+1
        found=True        
            
except EOFError:
    if found==False:
        print("Username not found, please try again")
    else:
        print("Rooms booked by the username-Successful!")
file.close()

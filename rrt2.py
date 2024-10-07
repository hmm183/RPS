#To check rooms boooked under one username
import pickle
pincode=input("Enter the pincode:")
f=pincode+".dat"
uname=input("Enter the username to search: ")
file=open(f, "rb")
found=False
try:
    while True:
        hotel=pickle.load(file)
        print(hotel)
        for i in hotel:
            if hotel[i][1]==uname:
                print(hotel[i])
                found=True
                break
except EOFError:
    if found==False:
        print ("Username not found.")
    else:
        print ("Rooms successfully checked.")

file.close()

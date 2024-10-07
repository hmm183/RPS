#To check rooms boooked under one username
import pickle
pincode=input("Enter the pincode:")
f=pincode+".dat"
file=open(f, "rb")
found=True
uname=input("Enter the username to search: ")
try:
    while found==True:
        hotel=pickle.load(file)
        print(hotel)
        for i in hotel:
            try:
                if hotel[i][1]==uname:
                    print(hotel[i][1])
                    found=False
                    file.close()
                    break
            except EOFError:
                found=False
                file.close()
                break
except EOFError:
    if found==True:
        print ("Username not found.")
    else:
        print ("Rooms successfully checked.")


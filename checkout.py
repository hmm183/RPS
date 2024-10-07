#To check out rooms booked under same username
import pickle
pincode=input("Enter the pincode:")
f=pincode+".dat"
fh=open(f,'rb')
y=[]
x=-1
z=True
try:
   while z==True:
      try:
         hotel=pickle.load(fh)
         print(hotel)
         y.append(hotel[1])
      except EOFError:
         z=False
         break
except EOFError:
   print('End of File')
found = False
d={}
print(y)
try:
    uname=input("Enter the username:")
    for i in range(len(y)):
        if uname in y[i]:
            print(i)
            x=i
        else:
            print('vsad')
    fh.close()
    if x>=0:
        fh=open(f,'wb')
        fh.close()
        y.pop(x)
        for i in range(len(y)):
            fh=open(f,'ab')
            z=[1,y[i]]
            dt=dict([z])
            pickle.dump(dt,fh)
    else:
        print('no')
except EOFError:
    if found == True:
        print("Check-out successful!")
    else :
        print("Username not found!")
print(y)
fh.close()

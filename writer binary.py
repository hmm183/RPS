import os
import pickle
pincode=input("Enter the pincode:")
f=pincode+".dat"
fh=open(f,'ab')
hotel={}
for i in range(0,120):
    val=[]
    date1=input("Enter the check-in date(yyyy-mm-dd):")
    if(os.path.getsize(f)==0 or len(hotel)==0):#check and put date booking
        print("Room",i+1,"is available")
        uname=input("Enter username:")
        date2=input("Enter the check-out date(yyyy-mm-dd):")
        status="Reserved"
        hotel[i+1]=[status, uname, date1, date2]
        print("Username:", hotel[i+1][1])
        print("Check-in date:", hotel[i+1][2])
        print("Check in time is 12:00 p.m.") 
        print("Check-out date:", hotel[i+1][3])
        print("Check out time is 11:00 a.m.")
        pickle.dump(hotel,fh)
        print("Reservation complete.")
        fh.close()
        print(hotel)
        break
    else:
        print("Room is not available.")
        ch=input("Try again(y/n):")
        if ch=='n':
            fh.close()
            break               
else:
    print("No rooms available")
    file.close()
fh.close()

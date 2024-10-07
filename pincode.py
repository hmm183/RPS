import mysql.connector
import mysql.connector as sqltor
from collections import ChainMap

#connection
mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

#creating cursor
cursor=mycon.cursor(buffered=True)

#selecting the data
sql = '''SELECT * from pincode'''

#Executing the query
cursor.execute(sql)


#fetching data from sql
userdata_sql=cursor.fetchall()
z={}

x=userdata_sql

y=[]
for t in x:
    for x in t:
        y.append(x)
w=[]
print(y)
op=int(input("enter a 6 digit no."))
z=[]
for i in range(1,len(y)):
    pl=int(y[i])
    zzzz=pl-op
    if zzzz>=0:
        z.append(zzzz)
    elif zzzz<=0:
        zzpos=zzzz*-1
        z.append(zzpos)
mini=min(z)
print(mini)
pincode=op+mini
print("this the nearest pincode",pincode)
    
    


#ending
cursor.close()
mycon.close()

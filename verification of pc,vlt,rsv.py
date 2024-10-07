import mysql.connector
import mysql.connector as sqltor
from collections import ChainMap

#connection
mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

#creating cursor
cursor=mycon.cursor(buffered=True)

#selecting the data
sql = '''SELECT * from chat'''

#Executing the query
cursor.execute(sql)


#fetching data from sql
userdata_sql=cursor.fetchall()
z={}

x=userdata_sql
print(x)
y=[]
for t in x:
    for x in t:
        y.append(x)
w=[]
print(y)
for i in range(0,len(y),3):
    if i==len(y)-2:
        break
    else:
        q=[y[i+1],y[i+2]]
        p=dict(name=q,user=y[i])
        i+=2
        w.append(p)
print(w)


res  = {}
user=input('what is ur username: ')
for i in range(0,len(w)):
    res.update(w[i])
    if user== res['user']:
        if ['yes','yes']== res['name']:
            print('ur reservation and valet parking is done')
        elif ["yes","no"]==res['name']:
            print('ur reservation is done')
        elif ["no","yes"]==res['name']:
            print('ur valet parking is done is done')
        elif ["no","no"]==res['name']:
            print('u have no reservation or valet parking')
    elif user != res['user']:
        continue
    else:
        continue
        
    
         


#ending
cursor.close()
mycon.close()

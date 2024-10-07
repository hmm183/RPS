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
y=[]
for t in x:
    for x in t:
        y.append(x)
w=[]
for i in range(0,len(y),3):
    if i==len(y)-2:
        break
    else:
        q=[y[i+1],y[i+2]]
        p=dict(name=q,user=y[i])
        i+=2
        w.append(p)

print(w)

user=input("what is ur name ")
for user in w[i].get('user'):
    if user in w[i].get('user'):
        if ['yes','yes']== w[i].get('name'):
            print('ur reservation and valet parking is done')
            break
        elif '["yes","no"]'==w[i].get('name'):
            print('ur reservation is done')
            break
        elif '["no","yes"]'==w[i].get('name'):
            print('ur valet parking is done is done')
            break
        elif '["no","no"]'==w[i].get('name'):
            print('u have no reservation or valet parking')
            break
    else:
        print('error')
        
    
         


#ending
cursor.close()
mycon.close()

import mysql.connector
import mysql.connector as sqltor

#connection
mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

#creating cursor
cursor=mycon.cursor(buffered=True)

#selecting the data
sql = '''SELECT * from userdata'''

#Executing the query
cursor.execute(sql)


#fetching data from sql
userdata_sql=cursor.fetchall()

print(userdata_sql)
k=dict(userdata_sql)
print(k)

#verification
username=input("enter your username: ")
password=input("enter your password: ")
if username in k and password ==k[username]:
    print('login approved')
elif username not in k:
    print('username invalid')
elif username in k and password !=k[username]:
    print('password invalid')

#ending
cursor.close()
mycon.close()

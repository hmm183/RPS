import mysql.connector
import mysql.connector as sqltor
#connection
mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')
#creating cursor
cursor=mycon.cursor(buffered=True)
username=input("w ")
pincode=input("p ")
#selecting the data
sql = 'delete from valet where username= '+'"'+username+'"'' and pincode='+'"'+pincode+'"'+';'
print(sql)
#Executing the query
cursor.execute(sql)
mycon.commit()
cursor.close()
mycon.close()

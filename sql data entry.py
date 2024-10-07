import mysql.connector
import mysql.connector as sqltor


#data input
username=input('username: ')
password=input('password: ')


#connection
mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

#making cursor
cursor=mycon.cursor()

#adding data through cursor
cursor.execute("insert into userdata(username,password) values(%s,%s)",(username, password))
mycon.commit()

#end
cursor.close()
mycon.close()



########gmail
g=input("enter your gmail id: ")


#saving gmail id
mycon1=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

#making cursor
cursor=mycon1.cursor()


#adding data through cursor
cursor.execute("insert into gmail_id(gmail) value(%s)",[g])
mycon1.commit()

cursor.close()
mycon1.close()


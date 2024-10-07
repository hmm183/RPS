import mysql.connector
import mysql.connector as sqltor


#connection
mycon1=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

#creating cursor
cursor=mycon1.cursor(buffered=True)

#selecting the data
sql_1 = '''SELECT * from gmail_id'''

#Executing the query
cursor.execute(sql_1)


#fetching data from sql
gmail_sql=cursor.fetchall()


#proper list in python
gmail=[]


#to store data in the properlist
for t in gmail_sql:
    for x in t:
        gmail.append(x)

        
k=gmail
print(k)

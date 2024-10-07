import smtplib
server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("botforproject@gmail.com", "dprzhddfvxtotxxb")
x=input('whats your gmail - ')
import random
y=random.randint(1000,9999)
n=str(y)
server.sendmail("botforproject@gmail.com",x,n)
server.quit()
z=float(input('what was the OTP?- '))
if z==y:
    print('access granted')
elif z!=y:
    print('access denied')



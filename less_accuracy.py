import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
file= open("/ml/accuracy.txt", "r")
acc=int(file.read())
acc*=100
file.close()
host_address = "**********@gmail.com"
host_pass = "**********"
guest_address = "*******@gmmail.com"
subject = "Regarding failure of main.py having less accuracy then the desired one"
content = '''Dear Admin, 
				Your trained model has not given best accuracy .It runed again by doing some changes.
				last accuracy was: '''+str(acc)+ '''
			-Jenkins'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')


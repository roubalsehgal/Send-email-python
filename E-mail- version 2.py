from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib #SMTP library

#Host and port no. of the service eg: Gmail, Yahoo, Outlook, etc.
host = "smtp.gmail.com"
port = 587

#credentials
from_email = "Your E-mail"
password = "Your Password"
to_email = ["Sender's E-mail"]

#Establish connection 
email_conn  = smtplib.SMTP(host, port)

#verify connection
email_conn.ehlo()

#start TLS handshake (For Security)
email_conn.starttls()

#logging in
email_conn.login(from_email, password)

the_msg = MIMEMultipart("alternative")
the_msg['Subject'] = "Hello there!" #subject of the email
the_msg['From'] = from_email 

#Message
html_txt = """\
<html>
	<head></head>
	<body>
		<p>Hey!<br>
		Testing the email <b>message</b>
		</p>
	</body>
</html>
"""
#pass variable through MIMEText for html conversion
part_1 = MIMEText(html_txt, "html")

#attach the html version of the text
the_msg.attach(part_1)

#send email
email_conn.sendmail(from_email, to_email, the_msg.as_string())
email_conn.quit()

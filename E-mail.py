import smtplib

#name of the host and port number
host = "smtp.gmail.com"
port = 587

#username from which email is to be sent
from_email = "Your Enail Address"
password = "Your Password"

#list of emails to which we have to send email
to_email = ["Sender's Email address 1, Sender's Email address 2"]
message = "Hello, this is a test email to you"

#conection establishment
email_conn  = smtplib.SMTP(host, port)

#verify connection by saying hello
email_conn.ehlo()

#to secure the connection TLS(Transport Layer Security)
email_conn.starttls()

#User credentials
email_conn.login(username, password)
email_conn.sendmail(from_email, to_email, message)

#Quit Connection
email_conn.quit()
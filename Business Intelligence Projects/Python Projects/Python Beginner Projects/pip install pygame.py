import smtplib

sender = "your_email@gmail.com"
password = "your_password"

receiver = "receiver@gmail.com"

message = "Hello! This is automated email from Python."

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)

server.sendmail(sender, receiver, message)

print("Email sent successfully!")

server.quit()

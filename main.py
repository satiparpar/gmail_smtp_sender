import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject="I am sati",
           body="finally i could send a message through gmail smtp",
           sender="<your gmail address here>",
           recipients=["satiparpar.com@gmail.com", ],  # write as much email address as you want on this list
           password="your gmail password here"
           )

import imghdr
import smtplib
from email.message import EmailMessage

password = "kjxt ejct ucxo iyvy"
sender= "sujeetguptapali@gmail.com"
receiver="sujeetguptapali@gmail.com"

def sendEmail(imagePath):
    email_message=EmailMessage()
    email_message["Subject"]="New customer showed up"
    email_message.set_content("Hey, we just saw a new customer")

    with open(imagePath,"rb") as file:
        content=file.read()
    email_message.add_attachment(content,maintype="image", subtype=imghdr.what(None, content))
    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender,password)
    gmail.sendmail(sender,receiver,email_message.as_string())
    gmail.quit()





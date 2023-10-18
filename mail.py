import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def emailsender(reciever,subject,content,image):
    hostmail='dotproduct456@gmail.com'
    hostpassword='wpaieaoevumeczav'
    recievermail=reciever
    
    asd=MIMEMultipart()
    asd['from']=hostmail
    asd['to']=recievermail
    asd['subject']=subject
    asd.attach(MIMEText(content,'plain'))

    with open(image,'rb') as image_file:
         image_data=image_file.read()
         image=MIMEImage(image_data,name='image.jpg')
         asd.attach(image)

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(hostmail,hostpassword)
    text=asd.as_string()
    server.sendmail(hostmail,recievermail,text)
    server.quit()
    print("email sent successfully,\nyou are welcome for my service")


print("welcome to email sender")
con='no'
while con=='no':
    subject=input("type something spicy: ")
    content=input("enter email content:  ")
    reciever=input("enter reciever's email: ")
    image=input("enter the image path: ")


    print("comfirm details: ")
    print("reciever's mail: ",reciever)
    print("subject: ",subject)
    print("content: ",content)

    confirm=input("send?? (type yes/no):")
    if confirm=='yes':
        emailsender(reciever,subject,content,image)
        break
    else:
        con='no'




import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from getpass import getpass

me = 'rob@ebeep.org'
you= ['rob.adams@astc-design.com','rob@ebeep.org']
auth = ('rob@ebeep.org', getpass())
mx=  ('smtp.gmail.com', 465)
# Any random URL that replies with an appropriate content-type
url= 'http://httpbin.org/response-headers?content-type=application/octet-stream'

text = MIMEText(
    '''<html>
         <head></head>
         <body>
           <p>
             <a href="{:s}">Click Me</a>
           </p>
         </body>
       </html>'''.format(url),
    'html')
attachment = MIMEApplication(
    'This is the attached data',
    'octet-stream')
attachment.add_header('Content-Disposition', 'attachment', filename='godzilla.bin')
msg = MIMEMultipart()
msg['Subject'] = 'Link'
msg['From'] = me
for to in you:
    msg.add_header('To', to)
msg.attach(text)
msg.attach(attachment)

#print msg.as_string()

s = smtplib.SMTP_SSL(*mx)
s.login(*auth)
s.sendmail(me, you, msg.as_string())
s.quit()

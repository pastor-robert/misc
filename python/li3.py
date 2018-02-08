import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from getpass import getpass

me = 'rob@ebeep.org'
you= ['rob.adams@astc-design.com','rob@ebeep.org']
auth = ('rob@ebeep.org', getpass())
mx=  ('smtp.gmail.com', 465)
# Some file that we'd like to include:
filename = 'motd'
url= 'http://httpbin.org/response-headers?content-type=application/octet-stream'

plain = MIMEText(
    'See attached.',
    'plain')
html = MIMEText(
    '''<html>
         <head></head>
         <body>
           <p>
             <a href="cid:motd">Click Me</a>
           </p>
         </body>
       </html>'''.format(url),
    'html')
with open('motd', 'rb') as fp:
    attachment = MIMEApplication(
        fp.read(),
        'octet-stream')
attachment.add_header('Content-Disposition', 'attachment', filename='motd.bin')
attachment.add_header('Content-ID', '<motd>')

msg = MIMEMultipart(
    'mixed',
    None,
    [MIMEMultipart(
        'alternative',
        None,
        [plain, html]),
     attachment])

msg['Subject'] = 'Link'
msg['From'] = me
for to in you:
    msg.add_header('To', to)

#print msg.as_string()

s = smtplib.SMTP_SSL(*mx)
s.login(*auth)
s.sendmail(me, you, msg.as_string())
s.quit()

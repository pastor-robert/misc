import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from getpass import getpass
from email.encoders import encode_base64, encode_quopri

me = 'rob@ebeep.org'
you= ['rob.adams@astc-design.com','rob@ebeep.org']
auth = ('rob@ebeep.org', getpass())
mx=  ('smtp.gmail.com', 465)
# Some file that we'd like to include:
filename = 'motd'
url= 'http://httpbin.org/response-headers?content-type=application/octet-stream'

plain = MIMEText(
    u'This is plan text.\u2020',
    'plain',
    'UTF-8')
html = MIMEText(
    u'''<html>
         <head></head>
         <body>
           <p>
             This is HTML text.\u2020
           </p>
         </body>
       </html>''',
    'html',
    'UTF-8')
encode_quopri(plain)
#encode_base64(html)
with open('/tmp/so.pdf', 'rb') as fp:
    pdf = MIMEApplication(
        'abc', #fp.read(),
        'pdf')

msg = MIMEMultipart(
    'mixed',
    None,
    [plain, html, pdf])

msg['Subject'] = 'multipart/mixed'
msg['From'] = me
for to in you:
    msg.add_header('To', to)

print msg.as_string()

#s = smtplib.SMTP_SSL(*mx)
#s.login(*auth)
#s.sendmail(me, you, msg.as_string())
#s.quit()

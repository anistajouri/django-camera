# Import smtplib for the actual sending function
import smtplib
 
# For guessing MIME type
import mimetypes
 
# Import the email modules we'll need
import email
import email.mime.application
import email.mime.multipart
import email.mime.text
 
#Import sys to deal with command line arguments
import sys,os


print("Hello: camera")
# Create a text/plain message
msg = email.mime.multipart.MIMEMultipart()
msg['Subject'] = 'Alerte : presence sur tapis'
msg['From'] = 'anis.tajouri@gmail.com'
msg['To'] = 'anis.tajouri@gmail.com'

         
# The main body is just another attachment
body = email.mime.text.MIMEText("""Bonjour, voir image captured """)
msg.attach(body)
         
# PDF attachment block code
# Nico: Ok, use a fixed image...and a jpg not pdf


# # ts=`date`
os.system("raspistill -o captured.jpg --mode 7")
# # echo "Our puppy $ts" | mail -a puppy.jpg -s PuppyCam your@email.com         
#         #directory=sys.argv[1]
directory = 'captured.jpg'
         
# Split de directory into fields separated by / to substract filename
         
spl_dir=directory.split('/')
         
#         # We attach the name of the file to filename by taking the last
#         # position of the fragmented string, which is, indeed, the name
#         # of the file we've selected
         
filename=spl_dir[len(spl_dir)-1]
         
# We'll do the same but this time to extract the file format (pdf, epub, docx...)
       
spl_type=directory.split('.')
         
type=spl_type[len(spl_type)-1]
         
fp=open(directory,'rb')
#att = MIMEApplication(fp.read(), _subtype=type)
att = email.mime.application.MIMEApplication(fp.read(),_subtype=type)
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)
        
# send via Gmail server
# NOTE: my ISP, Centurylink, seems to be automatically rewriting
# port 25 packets to be port 587 and it is trashing port 587 packets.
# So, I use the default port 25, but I authenticate.
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login('anis.tajouri','Fitality119')
s.sendmail('anis.tajouri@gmail.com','anis.tajouri@gmail.com', msg.as_string())
s.quit()


# Import the following module
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import glob
import datetime
import random
import string


# ---------------------------------------------------Email Alert--------------------------------------------------------------------------------------
''' This class is used to send Email Alert to respective departments when a Vehicle Crash is detected '''

# Gmail API is used here for Email service ,it is free to use service

class Email:

    def __init__(self,source):
        self.source = source
        self.location ="Location not recieved yet"
        self.folder_path = "outputs/frame_img/"
        self.files_path = os.path.join(self.folder_path, '*')
        self.files = sorted(glob.iglob(self.files_path), key=os.path.getctime, reverse=True)



        # print (files[0]) // latest file
        # print (files[0],files[1]) // latest two files

        self.last_file1 = self.files[0]
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # initialize connection to our
    # email server, we will use gmail here
    # Login with your Email and password
    def email_conn(self):
        self.smtp.ehlo()
        self.smtp.starttls()
        # enter the Sender Email (Gmail) and API code below
        self.smtp.login('Enter the Sender Email ID (Gmail) here', 'Enter the Email API Code here')

    # send our email message 'msg' to our boss
    def message(self,subject="Python Notification",
                text="", img=None,
                attachment=None):
        # build message contents
        msg = MIMEMultipart()

        # Add Subject
        msg['Subject'] = subject

        # Add text contents
        msg.attach(MIMEText(text))

        # Check if we have anything
        # given in the img parameter
        if img is not None:

            # Check whether we have the lists of images or not!
            if type(img) is not list:
                # if it isn't a list, make it one
                img = [img]

            # Now iterate through our list
            for one_img in img:
                # read the image binary data
                img_data = open(one_img, 'rb').read()
                # Attach the image data to MIMEMultipart
                # using MIMEImage, we add the given filename use os.basename
                msg.attach(MIMEImage(img_data,
                                     name=os.path.basename(one_img)))

        # We do the same for
        # attachments as we did for images
        if attachment is not None:

            # Check whether we have the
            # lists of attachments or not!
            if type(attachment) is not list:
                # if it isn't a list, make it one
                attachment = [attachment]

            for one_attachment in attachment:
                with open(one_attachment, 'rb') as f:
                    # Read in the attachment
                    # using MIMEApplication
                    file = MIMEApplication(
                        f.read(),
                        name=os.path.basename(one_attachment)
                    )
                file['Content-Disposition'] = f'attachment;\
    			filename="{os.path.basename(one_attachment)}"'

                # At last, Add the attachment to our message object
                msg.attach(file)
        return msg




    def send_email(self,send_message,location,mail,vcd_reference_code):

        current_date = datetime.date.today()
        current_time = datetime.datetime.now().time()



        # Call the message function
        msg = self.message(" Attention !, Vehicle Crash Detected !",
                      send_message
                           + "\nVehicle Crash Detection Reference Number : " + vcd_reference_code
                           + "\nDate : "+str(current_date)
                           + "\nTime : "+str(current_time)
                           + "\nLocation :" +location
                           + "\nNOTE : This is an Automatically Generated Mail ,Please do not reply to it"
                           + "\nThank you for your cooperation in this matter."
                           +  "\nSincerely,"
                           +  "\nRoad Safety Department"
                           , self.last_file1)
        # Make a list of emails, where you wanna send mail
        to = [mail]
        # Provide some data to the sendmail function!
        self.smtp.sendmail(from_addr="Enter the Sender Email ID (Gmail) here",
                      to_addrs=to, msg=msg.as_string())
        print("Email Alert Successfully Sent")

    # close the connection
    def quit_conn(self):
        self.smtp.quit()

    def run_mail(self):
        rto_message = open('messages/rto_message.txt').read().strip()
        hospital_message = open('messages/hospital_message.txt').read().strip()
        police_message = open('messages/police_message.txt').read().strip()

        # Define the length of the code
        code_length = 6
        # Generate a random code
        vcd_reference_code = "VCD" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=code_length))

        if self.source == 0:
            self.location = "ABC Street,Inner Circle,Bengaluru"
        else:
            self.location = "BE Road ,XYZ LAYOUT,Bengaluru"

        print(self.location)
        self.email_conn()
        # Enter Receiver Email IDs for Email Alert
        self.send_email(hospital_message, self.location, "Enter the Receiver Email ID here",vcd_reference_code)
        self.send_email(police_message, self.location, "Enter the Receiver Email ID here",vcd_reference_code)
        self.send_email(rto_message, self.location, "Enter the Receiver Email ID here",vcd_reference_code)
        self.quit_conn()




# Import the following module
import requests

# ---------------------------------------------------SMS Alert--------------------------------------------------------------------------------------
''' This class is used to send SMS alert to respective departments when a Vehicle Crash is detected '''

# Here Fast2SMS provides API for bulk SMS ,it is a paid service
# https://www.fast2sms.com/

class Sms:

    def __init__(self, source):
        self.source = source
        self.message = "This is a Message send from Vehicle Crash Detector System , An accident involving a Vehicle Crash was detected from the CCTV Footage,detailed information" \
                       " including location and image of the incident is send as the mail for reference," \
                       " Please Send the Required Forces to the Location immediately."
        self.location = "Location not received yet"

    def send_sms(self):
        url = "https://www.fast2sms.com/dev/bulkV2"
        if self.source == 0:
            self.location = "ABC Street,Inner Circle,Bengaluru"
        else:
            self.location = "BE Road ,XYZ LAYOUT,Bengaluru"

        print(
            self.message + "\n Location Recieved :" + self.location + "\nThis is an automatically generated SMS – please do not reply to it.For any queries regarding the same, please contact the Road Safety Department")
        # Enter the Fast2SMS api code for SMS service in authorization row below ,also enter the mobile numbers to which SMS Alert is to be send in the numbers row
        querystring = {"authorization": " Enter API Code here for SMS Service by Fast2SMS ",
                       "message": self.message + "\n Location Received :" + self.location + "\nThis is an automatically generated SMS – please do not reply to it.For any queries regarding the same, please contact the Road Safety Department",
                       "language": "english",
                       "route": "q", "numbers": "Enter the Mobile Numbers to which SMS is to be send here (put ',' after each number)"}

        headers = {'cache-control': "no-cache"}

        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            print("SMS Alert Successfully Sent")
        except:
            print("Oops! Something wrong while trying to send SMS Alert")

    def run_sms(self):
        self.send_sms()

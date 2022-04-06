import os
from twilio.rest import Client
from sampleCSV import readCSV
from getMyGSheet import getMyGSheet

# create a twilio client with creds from env
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


# create the content of the SMS and send
def textRemindersCSV():

    #get CSV data
    myCSVArray = readCSV()

    # loop CSV 
    for i in myCSVArray:
        
        # format message
        messageContent = 'Hi ' + i[0] + '' + i[1] + '! Your' + i[3] + i[2] + ' are on the way!'

        # fire off message
        messaging_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID']
        message = client.messages \
                .create(
                    body= messageContent,
                    from_='+17404964447',
                    status_callback='http://postb.in/1234abcd',
                    to='+19168122142'
                )
    print(message.sid)


# create the content of the SMS and send using GSheet
def textRemindersGSheet():

    #get GSheet Data
    myString = getMyGSheet()
    myArray = []
    i = 0

    # split data into consumable array format
    for line in myString.splitlines():
        line = line.replace('"', '')
        myArray.append(line.split(','))

    #delete header
    myArray.pop(0)
    # loop CSV 
    for i in myArray:
        
        # format message
        messageContent = 'Hi ' + i[0] + ' ' + i[1] + '! Your' + ' ' + i[2] + ' ' + i[3] + ' are on the way!'

        # fire off message
        messaging_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID']
        message = client.messages \
                .create(
                    body= messageContent,
                    from_='+17404964447',
                    status_callback='http://postb.in/1234abcd',
                    to='+19168122142'
                )
    print(message.sid)



# textRemindersCSV()
textRemindersGSheet()

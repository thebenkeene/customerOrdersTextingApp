import requests

def getMyGSheet():

    #GET request to data
    url = 'https://docs.google.com/spreadsheets/d/1i9x9pGkYY32daz2A-rB8JWEuayEDG8tzx6SE_8hVqPA/gviz/tq?tqx=out:csv&sheet=Orders'
    myFile = requests.get(url)

    #get the content (type string) of the request and store it
    myText = myFile.text

    # print(myText)
    return myText


getMyGSheet()

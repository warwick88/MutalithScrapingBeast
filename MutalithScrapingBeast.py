
# Instructions - I would recommend reading these.


# 1. Install required libraries for application to work: BeautifulSoup, Requests, Selenium, Twilio, Logging. If you don't know how ask in reddit and ill provide youtube links to /assist.
# 2. I would recommend making a folder (on your desktop, avoid permissioned files and system files etc), then place this file within it. This program creates log files in the folder it exists within.
# 3. Personally I set the task up with Task Scheduler on Windows, to run every 15 minutes, that way you scrape the site, if it's in stock you will get a text.
# 4. You need a virtual phone number to send the texts from..if you have one use that. If you don't use the FREE service and go to https://www.twilio.com/en-us
# 4A. Sign up for a free Twilio account and continue until you can generate a FREE number to text from. You don't need to spend any money etc.
# 5. Update the block that looks like this. You need to put values for TO and FROM there is an example of a to number
# 5A. To is YOUR cellphone you want the texts to go to. FROM is the virtual number we got from Twilio.
# Send a text message
#    message = client.messages.create(
#        #to='+1234567890',  # Receiver's phone number
#        to='+',     #You need to add your number here, use the example above
#        from_='+',  # You need to populate the virtual number from Twilio you got when signing up.
#        body='Your Item is in stock purchase it!' # This is the text message you wil receive.
#    )
# 6.Update the block 
#    account_sid = 'Put your number here' - You need to put your TWILIO Account_SID here  from signing up with Twilio
#    auth_token = 'Auth Code Here.' - Put your Twilio Auth code here



from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from twilio.rest import Client
import logging

#Ive caught part of the problem. It's running as incognito for whatever reason.

driver = webdriver.Chrome()

url = "https://www.games-workshop.com/en-US/Mutalith-Vortex-Beast"

driver.get(url)

#Wait for Javascript content to load )you might need to adjust the waiting time)
driver.implicitly_wait(10)

#Get the page source after JavaScript Execution
page_source = driver.page_source

# Create Beautiful Object
soup = BeautifulSoup(page_source,"html.parser")

# Extract Data



#Extra the <span Class="product-details__stock-message product-details__stock-message"

elements_with_class = soup.find_all(class_="product-details__stock-message product-details__stock-message--outOfStock test-availability-outOfStock")
xy = []


for element in elements_with_class:
    xy.append(element.text)

#So. This was added because if the item IS back in stock, the list will be empty and it throws the program off
#Now, if the item length is Temporarily found in the string it's out of stock if it prints xy is empty well it's in stock buddy.
if len(xy) > 0:
    cleaned_xy = [item.strip() for item in xy]
    vb = cleaned_xy[0]
    if 'Temporarily' in vb:
        print("'Temporarily' found in the string.")
    else:
        print("'Temporarily' not found in the string.")
else:

    print("List 'xy' is empty.")
    print("This means that the item is currently in stock!")
    # Your Twilio Account SID and Auth Token
    account_sid = 'Put your number here'
    auth_token = 'Auth Code Here.'

    # Create a Twilio client
    client = Client(account_sid, auth_token)

# Send a text message
    message = client.messages.create(
        #to='+1234567890',  # Receiver's phone number
        to='+',     #You need to add your number here, use the example above
        from_='+',  # You need to populate the virtual number from Twilio you got when signing up.
        body='Your Item is in stock purchase it!' # This is the text message you wil receive.
    )

    print(f"Message sent with SID: {message.sid}")

   
    logging.basicConfig(
        filename='beastlog.txt',   # When the item is found, this also creates a LOG file so if you get false positives you can potentially review the HTML elements present.
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        filemode='a'  # Append mode, to add new log entries without overwriting
    )
    beast_logger = logging.getLogger('beast_logger')  # Create a logger instan
    beast_logger.info(soup.prettify())
    #logging.info(soup.prettify())
    # Clear handlers associated with beast_logger
    beast_logger.handlers.clear()

    # Delete the logger instance
    del beast_logger



# We are now going to add logic pertaining to Logging
logging.basicConfig(
    filename="MutalithVortexRegular.txt",  # Specify the log file name
    level=logging.INFO,                # Set the logging level (INFO or DEBUG)
    format='%(asctime)s %(message)s',  # Define the log format
    filemode='a'                       # Write mode, overwriting the file each time
    )
other_logger = logging.getLogger('MutalithVortexRegular')  # Create another lo
# Log the prettified HTML content
other_logger.info('Program ran successfully.')


#logging.info('The program has ran successfully')
driver.quit()



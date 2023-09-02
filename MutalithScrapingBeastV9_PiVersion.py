# And so it begins

#1. First round of end notes pre 8.29 - Could not get PIP installed so that took time, got pathways fixed. 
#1A: Don't forget you call it with py not Python
# USE CHAT GPT WHEN YOU GET STUCK FUCK MAN It makes shit easy
#2 Ok, so using Chat GPT it's apparent you can't just scrape with Beautiful without using something like Selenium. These are the errors we got.
#2A:Please turn JavaScript on and reload the page. - Use Selenium should solve, already PIP installed it.
#2B: Please enable Cookies and reload the page.


#Some notes for sprint version 9
# Let's put if it works into a function, so we can MAKE sure it's actually completing, Because it won't text sometimes
#and we know it's not making log files, so maybe make a function for works yes/no, and then a function for logs
#You need to work on passing Chrome the right settings so that it doesnt open like a dummy

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from twilio.rest import Client
import logging

#Ive caught part of the problem. It's running as incognito for whatever reason.

driver = webdriver.Chrome()

url = "https://www.games-workshop.com/en-US/Mutalith-Vortex-Beast"
#url = "https://www.games-workshop.com/en-US/magnus-the-red"
driver.get(url)

#Wait for Javascript content to load )you might need to adjust the waiting time)
driver.implicitly_wait(10)

#Get the page source after JavaScript Execution
page_source = driver.page_source

# Create Beautiful Object
soup = BeautifulSoup(page_source,"html.parser")

# Extract Data



#Extra the <span Class="product-details__stock-message product-details__stock-message"
#I'm really going to need to target it so I can get what's in it.
elements_with_class = soup.find_all(class_="product-details__stock-message product-details__stock-message--outOfStock test-availability-outOfStock")
xy = []
# So Successfully printed the element within that field. We can see it's out of stock. Now...does it use the same class when it's IN stocK
# Conduct analysis of in stock items to see if class is the same.
for element in elements_with_class:
    #print(element.text)  # Print the text content of the element
    #print("---")  # Separator between elements
    xy.append(element.text)

#So. This was added because if the item IS back in stock, the list will be empty and it throws the program off
#Now, if the item length is Temporarily found in the string it's out of stock if it prints xy is empty well it's in stock buddy
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
        to='+',
        from_='+',  # Your Twilio phone number
        body='Your Item is in stock purchase it!'
    )

    print(f"Message sent with SID: {message.sid}")
    # Configure the logging settings
   
    logging.basicConfig(
        filename='beastlog.txt',   # Specify the log file name
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


print("hello")
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
print("hello2")

#logging.info('The program has ran successfully')



driver.quit()



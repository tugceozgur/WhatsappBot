from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

#how many times the message required to send will be specified here. 

with open("references.dat", 'r') as mc:
    message_count = mc.read()

#used to write in message block and finding the users.
 
with open("message.dat", 'r') as cm:
    custom_message = cm.read()

with open('filename.dat', 'r') as un: 
    all_user_names = un.read().splitlines()
    

#USERDATA for adding to the cookeies automatically after scanning. 

options = Options()
options.add_argument("user-data-dir=~/USERDATA")

#user defines the path where chromedriver extracted. 

driver = webdriver.Chrome(chrome_options = options, executable_path = '/home/tugce/WhatsappWebProject/WhatsappBot/chromedriver')
driver.get('https://web.whatsapp.com/')

# suggested waiting time. 

time.sleep(3)
    
'''
    Procedure: 

    identifies the user name, finds the message box and button, writes the message and sends. 

'''

for row in all_user_names:

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(row))
    user.click()
    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(0,int(message_count)):
        
        msg_box.send_keys(custom_message)
        button = driver.find_element_by_class_name('hnQHL')
        button.click()

driver.close()

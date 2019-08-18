from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

#download chromedriver then add it to path using the following
options = Options()
options.add_argument("user-data-dir=~/USERDATA")
driver = webdriver.Chrome(chrome_options=options,executable_path='./chromedriver')

driver.get('https://web.whatsapp.com/')

#time duration between opening whatsapp Web and writing the message. 
time.sleep(3)

#tells how many times yo want to send the message. 
message_count = 5

#open and read the file which contains the message. 
x = open("message.dat", 'r').read()

with open('filename.dat', 'r') as user_name:
    #reading names from file can both be performed with cvs or splitlines methods. 
    #reader = csv.reader(f, dialect='excel', delimiter='\n')
    all_user_names = user_name.read().splitlines()
    
    #for each name, it will go to message space, and click there.
    for row in all_user_names:

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(row))
        user.click()
        msg_box = driver.find_element_by_class_name('_3u328')
        
        # take the message from the file and writes it into the empty message block and click the send button. 
        for i in range(0,message_count):

            msg_box.send_keys(x)
            button = driver.find_element_by_class_name('hnQHL')
            button.click()

driver.close()

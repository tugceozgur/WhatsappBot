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

#link of WhatsApp. 
driver.get('https://web.whatsapp.com/')

#time duration between opening whatsapp and writing. 
time.sleep(3)

#tells how many times yo want to send the message. 
count = 2

#open and read the file which contains the message. 
x = open("message.dat", 'r').read()

'''opens and reads the file contains name of the people who will receive the message. It will read line
 by line which later is called row (in each line place a people name)'''
with open('filename.dat', 'r') as f:
    #reading names from file can both be performed with cvs or splitlines method. 
    #reader = csv.reader(f, dialect='excel', delimiter='\n')
    data= f.read().splitlines()
    
    #for each name, it will go to message space, and click there.
    for row in reader:

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(row[0]))
        user.click()
        msg_box = driver.find_element_by_class_name('_2S1VP')
        
        # take the message from the file and writes it into the empty message block and click the send button. 
        for i in range(0,count):

            msg_box.send_keys(x)
            button = driver.find_element_by_class_name('_35EW6')
            button.click()

driver.close()

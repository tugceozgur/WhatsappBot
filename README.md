# WhatsappBot
#HOW TO RUN THE CODE
Create a file and name My_Whatsapp_Project.
If you do not want to download ChromeDriver from here then Download ChromeDriver from http://chromedriver.chromium.org/downloads Then extract it and place it to the file named My_Whatsapp_Project. 
Write message that you want to sed to file named message.dat 
Write name of the people that you want to send messages to file named filename.dat
I personally used Visual Studio Code and open all files there and typed to terminal crontab -e. At the top, I wrote: 
* * * * * env DISPLAY=:0 /usr/bin/python3 /home/user/My_Whatsapp_Project/WhatsAppBot.py This enables the code to run every minute without manually running. You can change the time as you wish by placing values. (for more info search as crontab time).
The main code is in WhatsAppBot.py. You will run this file. All other files are referred into this file. 

#FIRST TIME RUNNING
Be careful to scan the QR code first time you run the code from terminal. After that it will remember your account and automatically opens the section and closes it after execution. 
Also be careful there should be no WhatsAppWeb tab open after and before execution of the code. 

#WhatsAppWeb.py
Selenium is a tool to test your web application. Therefore import selenium. Also install selenium if it is not installed before. 
from selenium import webdriver. 

In the options, USERDATA is for storing cookies of whatsapp so that it can remember you and you do not need to scan the code everytime you run the code. 

ChromeDriver path is written in the code.

Then link of the whatsappWeb is provided from chromedriver. 

I found accurate to wait 3 seconds. Since, After installing the page, the code can execute otherwise the code execute before the page installed which ends up with termination of the code. 

I indicate the count inside the code and you can change the number manually. Alternatively, you can input the value. 


'_2S1VP' value is for indicating message space. The code  will write the message to message space. 

Then click the send button. 






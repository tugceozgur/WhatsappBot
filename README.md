# WhatsappBot

WhatsappBot allows to send messages to selected users at user specified regular intervals without dealing with scanning to verify user account each time.

### Prerequisites

Download ChromeDriver from ``` chromedriver``` or Download ChromeDriver from ```http://chromedriver.chromium.org/downloads``` Then extract it.

### Installing

Installation recommended for user in python on linux environment.

Install Selenium :

```pip install selenium```
 

### Usage

Fill the file named [message.dat](https://github.com/tugceozgur/WhatsappBot/blob/master/message.dat) with the messages that you want to be sent. 

Fill the file named [filename.dat](https://github.com/tugceozgur/WhatsappBot/blob/master/filename.dat) each user name per line. 

Define the path of chromedriver to the code below. Code is in this file: [WhatsAppBot.py](https://github.com/tugceozgur/WhatsappBot/blob/master/WhatsAppBot.py)

```driver = webdriver.Chrome(chrome_options=options,executable_path='./chromedriver')```

Define time interval (ex: every minute) by typing to terminal:     ```crontab -e```

At the top, adjust ```*``` symbols and give the path. Below it is adjusted for every minute. 

```* * * * * env DISPLAY=:0 /usr/bin/python3 /home/user/My_Whatsapp_Project/WhatsAppBot.py```

## Inputs

Time sleep is found to be accure as 3 seconds but it can be increased according to how fast the web opens. 

Also count can be adjusted. 

### Notes And First Time Runing!

It is required to scan QR code to enter Whatsapp Web at first time running. 

Also there should be no WhatsAppWeb tab open after and before execution of the code.






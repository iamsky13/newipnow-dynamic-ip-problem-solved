from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import json 
import os.path

options = Options()
# options.headless = True
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome('C:\Program Files (x86)\Google\chromedriver.exe',chrome_options=options) #ChromeDriver path

while True:
    username = 'xxxx' #username of ipdashboard
    password='xxxxx'  #password of ipdashboard
    driver.get('https://www.newipnow.com/paid-proxies.html#login')
    username_field = driver.find_element_by_id('user')
    username_field.send_keys(str(username))
    password_field = driver.find_element_by_id('password')
    password_field.send_keys(str(password))
    driver.find_element_by_id('x').click()
    ip_box=driver.find_element_by_id('all-authips')
    ips=ip_box.get_attribute('value')

    #get current ip
    current_ip = requests.get('https://api.ipify.org').text

    if not os.path.isfile('ip.json'):
        with open('ip.json','w') as new_file:
            print(ips)
            json.dump(ips,new_file)
    with open('ip.json') as json_file:
        data = json.load(json_file)
        if current_ip in data:
            print(current_ip)
            time.sleep(600) #every 10 minutes
        else:
            with open('ip.json','w') as json_file:
                data = data +current_ip+'\n'
                json.dump(data,json_file)
                ip_box.send_keys(data)
                driver.find_element_by_name('button').click()

                print(data)
                time.sleep(600)





    
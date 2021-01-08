# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:55:29 2021

@author: Kevin Yan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:59:45 2021

@author: Kevin Yan
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

options = Options()
#options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#driver = uc.Chrome(chrome_options = options)
#driver.get('https://pt.surebet.com/users/sign_in')
time.sleep(10)


driver = webdriver.Chrome(options = options)
driver.get('https://pt.surebet.com/users/sign_in')


def login(a,b):
    username = driver.find_element_by_name('user[email]')
    password = driver.find_element_by_name('user[password]')
    button_ok = driver.find_element_by_name('commit')
    
    username.send_keys(a)
    password.send_keys(b)
    button_ok.click()
    
    driver.find_element_by_class_name('alert')
    
    alert = ((driver.find_element_by_class_name('alert')).text).split('.')
    if alert[0] == 'Logado com sucesso':
        return True
    else:
        return False







def get_info(content):
#    content = driver.find_element_by_class_name('surebet_record')
    lucro = (content.find_element_by_class_name('profit')).text
    idade = (content.find_element_by_class_name('age')).text
    calc = (((content.find_element_by_class_name('btn-group'))).find_element_by_tag_name('a')).get_attribute('href')
    esporte = (content.find_element_by_class_name('booker')).find_element_by_class_name('minor').text
    casa_aposta_1 =  (content.find_elements_by_class_name('booker'))[0].find_element_by_tag_name('a').text
    evento_1      =  (content.find_elements_by_class_name('event'))[0].find_element_by_tag_name('a').text
    link_evento_1 =  (content.find_elements_by_class_name('event'))[0].find_element_by_tag_name('a').get_attribute('href')
    aposta_1      =  ((content.find_elements_by_class_name('coeff'))[0].find_element_by_tag_name('abbr')).get_attribute('title')+' '+((content.find_elements_by_class_name('coeff'))[0].find_element_by_tag_name('abbr')).text
    odd_1         =  ((content.find_elements_by_class_name('value'))[0].find_element_by_tag_name('a')).text
    casa_aposta_2 =  (content.find_elements_by_class_name('booker'))[1].find_element_by_tag_name('a').text
    evento_2      =  (content.find_elements_by_class_name('event'))[1].find_element_by_tag_name('a').text
    link_evento_2 =  (content.find_elements_by_class_name('event'))[1].find_element_by_tag_name('a').get_attribute('href')
    aposta_2      =  ((content.find_elements_by_class_name('coeff'))[1].find_element_by_tag_name('abbr')).get_attribute('title')+' '+((content.find_elements_by_class_name('coeff'))[0].find_element_by_tag_name('abbr')).text
    odd_2         =  ((content.find_elements_by_class_name('value'))[1].find_element_by_tag_name('a')).text
    mensagem = ( 'NOVA APOSTA CERTA ENCONTRADA!'+'\n'
                 'LUCRO: '+lucro+'\n'
                 'IDADE: '+idade+'\n'
                 'ESPORTE: '+esporte+'\n'               
                 'CALCULADORA: '+calc+'\n'               
                 '+-+-+Primeira aposta+-+-+'+'\n'
                 ' '+casa_aposta_1+'\n'
                 ' '+evento_1+'\n'
                 ' '+link_evento_1+'\n'
                 ' '+aposta_1+'\n'
                 ' '+odd_1+'\n'
                 '+-+-+Segunda aposta+-+-+'+'\n'
                 ' '+casa_aposta_2+'\n'  
                 ' '+evento_2+'\n'  
                 ' '+link_evento_2+'\n'  
                 ' '+aposta_2+'\n'
                 ' '+odd_2+'\n'  
                 )
    return mensagem

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1223273819:AAGIleGROBgbWyGT77tqeSZR9QZbMyhXMpM'
    bot_chatID = '-1001298510060'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

user = 'darlan_18lisboa@hotmail.com'
pass_ = 'a1b2c3d4'

try:
    if login(user,pass_) is True:
        telegram_bot_sendtext('Logado com sucesso')
    else:
        telegram_bot_sendtext('Usuário e senha errado!')
except:
    telegram_bot_sendtext('Problemas para se autenticar')

try:
    lista = []
    content = driver.find_elements_by_class_name('surebet_record')
    loop = driver.find_element_by_css_selector("i[class='fa fa-play-circle']") 
    for i in content:
        telegram_bot_sendtext(get_info(i))
except:
    telegram_bot_sendtext('erro antes do primeiro laço ')
    telegram_bot_sendtext('autenticando novamente..')
    if login(user,pass_) is True:
        telegram_bot_sendtext('Logado com sucesso')
    else:
        telegram_bot_sendtext('Usuário e senha errado!')
    
loop.click()

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Server Running.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

while True:
    try:
        content = driver.find_elements_by_class_name('surebet_record')
        for i in content:
            try:
                new = (i.find_element_by_css_selector("span[class='profit new']"))
                data = (((i.find_element_by_class_name('btn-group'))).find_element_by_tag_name('a')).get_attribute('href')
                if data not in lista:
                    lista.append(data)
                    telegram_bot_sendtext(get_info(i))
            except:
                continue
    except:
        telegram_bot_sendtext('erro antes do segundo laço ')
    time.sleep(2)
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 07:21:55 2020

@author: Kevin Yan
"""

#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:23:15 2020

@author: k_matos
"""

# Importa as bibliotecas

from bs4 import BeautifulSoup
import requests
#import time
#import sys


def get_info_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    try:
        page = requests.get(url, headers=headers)
    except:
        return False
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        result = soup.find(id='surebets-table')
        page.close()
        return result
    else:
        page.close()
        return False

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1223273819:AAGIleGROBgbWyGT77tqeSZR9QZbMyhXMpM'
    bot_chatID = 'usuario'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


url_apostas='https://pt.surebet.com/surebets?utf8=%E2%9C%93&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Bmin_profit%5D=0.9&selector%5Bmax_profit%5D=1&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=0&selector%5Bbookies_settings%5D=0%3A66%3A%3A%3B0%3A69%3A%3A%3B0%3A65%3A%3A%3B0%3A71%3A%3A%3B4%3A70%3A%3A%3B0%3A68%3A%3A%3B0%3A109%3A%3A%3B0%3A127%3A%3A%3B0%3A121%3A%3A%3B0%3A21%3A%3A%3B0%3A23%3A%3A%3B4%3A26%3A%3A%3B0%3A134%3A%3A%3B0%3A120%3A%3A%3B0%3A%3A%3A%3B0%3A32%3A%3A%3B0%3A99%3A%3A%3B0%3A29%3A%3A%3B4%3A10%3A%3A%3B0%3A45%3A%3A%3B0%3A14%3A%3A%3B0%3A11%3A%3A%3B0%3A38%3A%3A%3B0%3A55%3A%3A%3B0%3A33%3A%3A%3B0%3A49%3A%3A%3B0%3A62%3A%3A%3B0%3A12%3A%3A%3B0%3A46%3A%3A%3B0%3A141%3A%3A%3B0%3A112%3A%3A%3B0%3A130%3A%3A%3B0%3A24%3A%3A%3B0%3A82%3A%3A%3B0%3A124%3A%3A%3B0%3A140%3A%3A%3B0%3A131%3A%3A%3B0%3A103%3A%3A%3B0%3A5%3A%3A%3B0%3A6%3A%3A%3B0%3A4%3A%3A%3B0%3A30%3A%3A%3B0%3A15%3A%3A%3B0%3A123%3A%3A%3B0%3A50%3A%3A%3B0%3A87%3A%3A%3B0%3A9%3A%3A%3B0%3A41%3A%3A%3B0%3A125%3A%3A%3B0%3A128%3A%3A%3B0%3A3%3A%3A%3B0%3A8%3A%3A%3B0%3A113%3A%3A%3B0%3A83%3A%3A%3B0%3A119%3A%3A%3B0%3A39%3A%3A%3B0%3A31%3A%3A%3B0%3A51%3A%3A%3B0%3A2%3A%3A%3B0%3A138%3A%3A%3B0%3A7%3A%3A%3B0%3A1%3A%3A%3B0%3A105%3A%3A%3B0%3A101%3A%3A%3B0%3A139%3A%3A%3B0%3A118%3A%3A%3B0%3A25%3A%3A%3B0%3A135%3A%3A%3B0%3A114%3A%3A%3B0%3A43%3A%3A%3B0%3A18%3A%3A%3B0%3A59%3A%3A%3B0%3A80%3A%3A%3B0%3A115%3A%3A%3B0%3A122%3A%3A%3B0%3A86%3A%3A%3B0%3A17%3A%3A%3B0%3A104%3A%3A%3B0%3A53%3A%3A%3B0%3A28%3A%3A%3B0%3A44%3A%3A%3B0%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=0+43+32+3+28+8+44+9+26+34+10+11+12+39+47+46+48+49+30+13+52+29+45+19+36+33+31+40+42+41+20+50+51+21+37+23+35+38&selector%5Bextra_filters%5D=&narrow='


raw_content = get_info_url(url_apostas)


content = raw_content('tbody')
for i in content:
    booker = i.find_all('td', class_ = 'booker')
    date = i.find_all('td', class_ = 'time')
    event = i.find_all('td', class_ = 'event')
    bet = i.find_all('td', class_ = 'coeff')
    print('_______________________________________________')  
    print('                Inicio da aposta')  
    print('Primeira aposta')  
    print(' '+booker[0].a.text);
    print(' '+date[0].get_text("-"))
    print(' '+event[0].get_text("-"))
    print(' https://pt.surebet.com'+event[0].a['href'])
    print(' '+bet[0].abbr['title']+bet[0].text)
    
    print('Segunda aposta')  
    print(' '+booker[1].a.text);
    print(' '+date[1].get_text("-"))
    print(' '+event[1].get_text("-"))
    print(' https://pt.surebet.com'+event[1].a['href'])
    print(' '+bet[1].abbr['title']+bet[1].text)
    print('                  Fim da aposta')  
    print('_______________________________________________')
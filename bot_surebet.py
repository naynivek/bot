# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:19:15 2020

@author: k_matos
"""

# Importar bibliotecas

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


# Declarando caminho padrão e variaveis de controle
dir_path = r'driver'+'\\'  # Para Windows

# Instanciando Chromedriver

opt = Options()
opt.add_argument(r'user-data-dir=cache/')
driver = webdriver.Chrome(dir_path+'chromedriver', options=opt)
driver.get('https://pt.surebet.com/surebets?utf8=%E2%9C%93&filter%5Bselected%5D%5B%5D=&filter%5Bselected%5D%5B%5D=33753220&filter%5Bsave%5D=&filter%5Bcurrent_id%5D=33753220&selector%5Border%5D=profit&selector%5Boutcomes%5D%5B%5D=&selector%5Boutcomes%5D%5B%5D=2&selector%5Boutcomes%5D%5B%5D=3&selector%5Bmin_profit%5D=&selector%5Bmax_profit%5D=&selector%5Bmin_roi%5D=&selector%5Bmax_roi%5D=&selector%5Bsettled_in%5D=0&selector%5Bbookies_settings%5D=0%3A66%3A%3A%3B0%3A69%3A%3A%3B0%3A65%3A%3A%3B0%3A71%3A%3A%3B4%3A70%3A%3A%3B0%3A68%3A%3A%3B0%3A109%3A%3A%3B0%3A127%3A%3A%3B0%3A121%3A%3A%3B0%3A21%3A%3A%3B0%3A23%3A%3A%3B4%3A26%3A%3A%3B0%3A120%3A%3A%3B0%3A%3A%3A%3B0%3A32%3A%3A%3B0%3A99%3A%3A%3B0%3A29%3A%3A%3B0%3A10%3A%3A%3B0%3A45%3A%3A%3B0%3A14%3A%3A%3B0%3A11%3A%3A%3B0%3A38%3A%3A%3B0%3A55%3A%3A%3B4%3A33%3A%3A%3B0%3A49%3A%3A%3B0%3A62%3A%3A%3B0%3A12%3A%3A%3B0%3A46%3A%3A%3B0%3A112%3A%3A%3B0%3A130%3A%3A%3B0%3A24%3A%3A%3B0%3A82%3A%3A%3B0%3A124%3A%3A%3B0%3A131%3A%3A%3B0%3A103%3A%3A%3B0%3A5%3A%3A%3B0%3A102%3A%3A%3B0%3A6%3A%3A%3B0%3A4%3A%3A%3B0%3A30%3A%3A%3B0%3A15%3A%3A%3B0%3A123%3A%3A%3B0%3A50%3A%3A%3B0%3A129%3A%3A%3B0%3A87%3A%3A%3B0%3A9%3A%3A%3B0%3A41%3A%3A%3B0%3A125%3A%3A%3B0%3A128%3A%3A%3B0%3A3%3A%3A%3B0%3A8%3A%3A%3B0%3A113%3A%3A%3B0%3A83%3A%3A%3B0%3A119%3A%3A%3B0%3A63%3A%3A%3B0%3A61%3A%3A%3B0%3A39%3A%3A%3B0%3A31%3A%3A%3B0%3A51%3A%3A%3B0%3A2%3A%3A%3B0%3A7%3A%3A%3B0%3A1%3A%3A%3B0%3A105%3A%3A%3B0%3A101%3A%3A%3B0%3A118%3A%3A%3B0%3A25%3A%3A%3B0%3A114%3A%3A%3B0%3A43%3A%3A%3B0%3A18%3A%3A%3B0%3A59%3A%3A%3B0%3A80%3A%3A%3B0%3A115%3A%3A%3B0%3A122%3A%3A%3B0%3A86%3A%3A%3B0%3A17%3A%3A%3B0%3A104%3A%3A%3B0%3A53%3A%3A%3B0%3A28%3A%3A%3B0%3A44%3A%3A%3B0%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=0+41+32+3+28+8+42+9+26+34+10+11+12+37+45+44+46+47+30+13+50+29+43+19+35+33+31+38+40+39+20+48+49+21+36+23&selector%5Bextra_filters%5D=&narrow=')
time.sleep(15)
# Bloco principal / Criação do serviço rodando na porta 8080


result = driver.find_element_by_class_name('surebet_record')
results = driver.find_elements_by_class_name('surebet_record')



for result in results:
    # Declarando as variaveis
    profit = (result.text).split('\n')[0]
    time_spent = (result.text).split('\n')[1]
    book_1 = (result.text).split('\n')[3]
    sport_1 = (result.text).split('\n')[4]
    event_1 = (result.text).split('\n')[5]
    league_1 = (result.text).split('\n')[6]
    bet_1 = (result.text).split('\n')[7]
    link_1 = (result.find_element_by_xpath("tr/td[5]/a")).get_attribute('href')
    book_2 = (result.text).split('\n')[8]
    sport_2 = (result.text).split('\n')[9]
    event_2 = (result.text).split('\n')[10]
    league_2 = (result.text).split('\n')[11]
    bet_2 = (result.text).split('\n')[12]
    link_2 = (result.find_element_by_xpath("tr[2]/td[5]/a")).get_attribute('href')
    # Transformando profit string em profit float
    profit = (profit.replace('%',''))
    profit = (profit.replace(',','.'))
    if float(profit) > 0.9:
        print('A aposta mais lucrativa é de '+profit+'\n'+
              'Tempo da aposta: '+time_spent+'\n'
              'O primeiro evento é: '+event_1+' deve apostar em '+bet_1+' na banca '+book_1+' Link: '+link_1+'\n'
              'O segundo evento é: '+event_2+' deve apostar em '+bet_2+' na banca '+book_2+' Link: '+link_2+'\n'
              'Mais informações:\n'
              'O esporte é: '+sport_1+'\n'
              'A  liga é: '+league_1+'\n')

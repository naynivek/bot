# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:23:15 2020

@author: k_matos
"""

from bs4 import BeautifulSoup
import requests
import json  
import time
import telepot


#bot = telepot.Bot('1223273819:AAGIleGROBgbWyGT77tqeSZR9QZbMyhXMpM')
#bot.getMe()
#bot.getUpdates()

def json_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    data_json = soup.find(id='initial-data').get('data-json')
    return json.loads(data_json)

# Função que recebe url do anúncio
# e mostra nome do vendedor, telefone,
# descrição do produto e preço
def mostra_dados_do_anuncio(url):
    data = json_from_url(url)
    descricao = (data['ad']['body']).replace('<br>','\n')
    phone =  data['ad']['phone']['phone']
    user = data['ad']['user']['name']
    preco = data['ad']['price']
    print('Vendedor=',user)
    print('Telefone=',phone)
    print('Descrição=',descricao)
    print('preco=',preco)

# Pega a lista de produtos da área de eletrônicos
url_eletronicos='https://df.olx.com.br/?ot=1&q=iphone&sf=1'
data = json_from_url(url_eletronicos)

# Entra em cada anúncio e mostra o telefone
lista = []
adList = data['listingProps']['adList']
for anuncio in adList:
    subject = anuncio.get('subject')
    lista.append(anuncio.get('listId'))
    if subject: 
        print('------------------------')
        descricao = anuncio.get('subject')        
        url = anuncio.get('url')
        print('Descricao do produto:',descricao)
        print('URL do produto=',url)
        mostra_dados_do_anuncio(url)

while True:
    time.sleep(300)
    try:
        data_new = json_from_url(url_eletronicos)
        adList = data_new['listingProps']['adList']    
        for anuncio in adList:
            subject = anuncio.get('subject')
            if subject and anuncio.get('listId') not in lista:
                lista.append(anuncio.get('listId'))
                print('\n------------------------')
                print('Nova oferta encontrada!')
                descricao = anuncio.get('subject')        
                url = anuncio.get('url')
                print('Descricao do produto:',descricao)
                print('URL do produto=',url)
                mostra_dados_do_anuncio(url)
                print('------------------------')
    except:
        print('\nsErro ao buscar ofertas\n')








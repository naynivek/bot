#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:23:15 2020

@author: k_matos
"""

# Importa as bibliotecas

from bs4 import BeautifulSoup
import requests
import json  
import time
import telepot
import sys

# Função que coleta dados da página 
def json_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    data_json = soup.find(id='initial-data').get('data-json')
    return json.loads(data_json)

# Função que recebe url do anúncio e mostra nome do vendedor, telefone, descrição do produto e preço
def mostra_dados_do_anuncio(url):
    data = json_from_url(url)
    descricao = (data['ad']['body']).replace('<br>','\n')
    phone =  data['ad']['phone']['phone']
    user = data['ad']['user']['name']
    preco = data['ad']['price']
    vendedor = 'Vendedor: '+user
    telefone = 'Telefone: '+phone
    descri = 'Descrição: '+descricao
    price = 'preco: '+str(preco)
    bot.sendMessage(89627667, vendedor)
    bot.sendMessage(89627667, telefone)
    bot.sendMessage(89627667, descri)
    bot.sendMessage(89627667, price)

# Declara o token do bot
bot = telepot.Bot('1223273819:AAGIleGROBgbWyGT77tqeSZR9QZbMyhXMpM')


# Estipula os filtros

busca = sys.argv[1]
prec_min = sys.argv[2]
prec_max = sys.argv[3]

# Pega a lista de produtos na página solicitada com filtros

url_eletronicos='https://df.olx.com.br/distrito-federal-e-regiao?ot=1&pe='+prec_max+'&ps='+prec_min+'&q='+busca
data = json_from_url(url_eletronicos)

# Entra em cada anúncio e mostra o telefone
lista = []
adList = data['listingProps']['adList']
for anuncio in adList:
    subject = anuncio.get('subject')
    lista.append(anuncio.get('listId'))
    if subject: 
        descricao = anuncio.get('subject')        
        url = anuncio.get('url')
        mensagem = ('-----------------------------------'+'\n'
        'Nova oferta encontrada!'+'\n'
        'Descrição do produto: '+descricao+'\n'
        'Link do produto: '+url            )
#        bot.sendMessage(89627667, mensagem)
#        mostra_dados_do_anuncio(url)
#        bot.sendMessage(89627667, 'bot rodando')
print('bot rodando')       
while True:
    time.sleep(300)
    data_new = json_from_url(url_eletronicos)
    a=0
    try:
        adList = data_new['listingProps']['adList']    
        for anuncio in adList:
            subject = anuncio.get('subject')
            if subject and anuncio.get('listId') not in lista:
                lista.append(anuncio.get('listId'))
                descricao = anuncio.get('subject')        
                url = anuncio.get('url')
                mensagem = ('-----------------------------------'+'\n'
                'Nova oferta encontrada!'+'\n'
                'Descrição do produto: '+descricao+'\n'
                'Link do produto: '+url            )
                bot.sendMessage(89627667, mensagem)
                mostra_dados_do_anuncio(url)
                a=1
#        if a == 0:
#            print('Nenhuma oferta nova no momento')
    except:
        bot.sendMessage(89627667, 'Erro ao buscar as ofertas')



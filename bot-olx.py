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
    try:
        page = requests.get(url, headers=headers)
    except:
        return False
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        data_json = soup.find(id='initial-data').get('data-json')
        return json.loads(data_json)
    else:
        return False
        

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
    bot.sendMessage(usuario, vendedor)
    bot.sendMessage(usuario, telefone)
    bot.sendMessage(usuario, descri)
    bot.sendMessage(usuario, price)

# Declara o token do bot
bot = telepot.Bot('1223273819:AAGIleGROBgbWyGT77tqeSZR9QZbMyhXMpM')

# Estipula os filtros

busca = sys.argv[1]
prec_min = sys.argv[2]
prec_max = sys.argv[3]
usuario = sys.argv[4] #89627667


# Pega a lista de produtos na página solicitada com filtros

url_eletronicos='https://df.olx.com.br/distrito-federal-e-regiao?ot=1&pe='+prec_max+'&ps='+prec_min+'&q='+busca+'&sf=1'
data = json_from_url(url_eletronicos)
if data is False:
    time.sleep(5)
    data = json_from_url(url_eletronicos)
    if data is False:
        time.sleep(10)
        data = json_from_url(url_eletronicos)
        if data is False:
            time.sleep(20)
            data = json_from_url(url_eletronicos)
            if data is False:
                bot.sendMessage(usuario, 'Problemas para acessar o site, ele pode estar fora do ar')

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
bot.sendMessage(usuario, 'Bot rodando com o seguinte filtro \n \
                Busca: '+busca+' \n \
                Preço mínimo: '+prec_min+'\n \
                Preço máximo: '+prec_max+'\n \
                Usuário: '+usuario+'\n \
                ')      
while True:
    time.sleep(300)
    data_new = json_from_url(url_eletronicos)
    if data_new is False:
        bot.sendMessage(usuario, 'Site falhou 1x, tentando novamente')
        time.sleep(5)
        data_new = json_from_url(url_eletronicos)
        if data_new is False:
            bot.sendMessage(usuario, 'Site falhou 2x, tentando novamente')
            time.sleep(10)
            data_new = json_from_url(url_eletronicos)
            if data_new is False:
                bot.sendMessage(usuario, 'Site falhou 3x')
                time.sleep(20)
                data_new = json_from_url(url_eletronicos)
                if data_new is False:
                    bot.sendMessage(usuario, 'Problemas para acessar o site, ele pode estar fora do ar')
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
            bot.sendMessage(usuario, mensagem)
            mostra_dados_do_anuncio(url)


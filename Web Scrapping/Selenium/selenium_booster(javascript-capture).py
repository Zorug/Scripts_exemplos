# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:58:02 2019
@author: Zorug
O arquivo csv atualizado está disponivel em:
https://steam.tools/cards/
"""

from selenium import webdriver


def gera_site(game_appid):
  import pandas as pd
  dados = pd.read_csv('STC_set_data.csv') #aqui acho a lista dos appids
  dados = pd.DataFrame(data={'Game':dados['Game'],'AppId':dados['AppId']})
  #dados.head(5)
  
  index_value = dados.loc[dados['AppId'] == game_appid].index[0] #localiza o index
  game_appid = str(game_appid)
  #index_value
  
  game_name = dados['Game'].iloc[index_value] #localiza o game
  #game_name, game_appid
  
  name_changed = game_name.replace(" ","%20")
  #name_changed
  
  site = 'https://steamcommunity.com/market/listings/753/' + game_appid + '-' + name_changed + '%20Booster%20Pack'
  print(site)
  return site


game_appid = 385070
site = gera_site(game_appid)


def filtro(comprar, vender):
  word = comprar
  print(word)
  buy_requests = word[:word.find(' ')]
  print('buy_requests =', buy_requests)
  z1 = word[word.find('$')+1:]
  buy_value = z1[:z1.find(' ')]
  print('buy_value =', buy_value)
  
  print('<<<=+=+=+=+=+=+=+=+=+=+=>>>')
  
  word = vender
  print(word)
  sale_requests = word[:word.find(' ')]
  print('sale_requests =', sale_requests)
  sale_value = word[word.find('$')+1:]
  print('sale_value =', sale_value)
  
  #return word[:word.find(' ')
  
  
# open it, go to a website, and get results
wd = webdriver.Chrome('chromedriver')
wd.get(site)

vender = wd.find_element_by_id('market_commodity_forsale')
comprar = wd.find_element_by_id('market_commodity_buyrequests')
vender, comprar = vender.text, comprar.text

filtro(comprar, vender)
# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = 'Zb1qCprIQO1X3FYthAOp'
client_secret = '13pox1GnON'

def main():

    node = 'news'
    srcText = input('검색어를 입력하세요: ')

    cnt = 0
    jsonResult = []

    jsonResponse
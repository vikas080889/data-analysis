import requests
import re
from scipy.stats import rankdata
from datetime import datetime, date
from bs4 import BeautifulSoup
import time

id_short = ['18294', '17998', '18005', '18008', '18036', '18040', '18041', '39852', '18055', '18057', '18075', '18080', '978762', '18094', '18122', '18137', '39867', '18180', '18187', '18184', '18186', '18198', '991131', '18209', '18213', '18224', '18226', '18276', '18334', '18361', '18364', '18376', '39910', '18422', '18436', '18467']
name_short = ['Adani Port and Special Economic Zone Ltd', 'Ambuja Cements Ltd.', 'Apollo Tyres Ltd', 'Arvind Ltd.', 'Berger Paints India Ltd', 'Bharat Petroleum Corp. Ltd.', 'Bharti Airtel Ltd.', 'Bharti Infratel Ltd', 'Cadila Healthcare Ltd.', 'Canara Bank Ltd', 'Coal India Ltd', 'Coromandel International Ltd', 'Crompton Greaves Consumer Electricals Ltd', 'Dewan Housing Finance Corp. Ltd.', 'Exide Industries Ltd.', 'GAIL Ltd', 'GRUH Finance Ltd', 'Hexaware Technologies Ltd.', 'Hindalco Industries Ltd.', 'Hindustan Petroleum Corporation Ltd', 'Hindustan Zinc Ltd.', 'ICICI Bank Ltd', 'ICICI Prudential Life Insurance Company Ltd', 'Indian Bank', 'Indraprastha Gas Ltd', 'ITC Ltd', 'JSW Steel Ltd', 'Marico Ltd', 'Petronet LNG Ltd', 'Reliance Capital Ltd', 'Reliance Infrastructure Ltd', 'State Bank Of India', 'Sun Pharma Advanced Research Company Ltd', 'Tata Global Beverages Ltd', 'Torrent Power Ltd', 'Wipro Ltd']
nse_name = []

#for i ,name in zip (id_short ,name_short):
url = "https://in.investing.com/indices/cnx-200-components"
data = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
soup = BeautifulSoup(data.text, 'lxml')
payload = {'pairID': '18294', 'period': '3600', 'viewType': 'normal'}
tech_url = requests.post(url='https://in.investing.com/instruments/Service/GetTechincalData',
                             data=payload, headers={'X-Requested-With': 'XMLHttpRequest',
                                                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
tech_url = BeautifulSoup(tech_url.content, "lxml")
print(tech_url)
ten_ma = tech_url.find("td", text="MA10").find_next_sibling("td").text
print(ten_ma)
'''
ten_ma = re.sub('\s+', '',ten_ma)
#print(ten_ma,name)
pattern = re.compile(r'(\d+\.\d+)(\w+)')
matches = pattern.finditer(ten_ma)

for match in matches:
    ten_ma, verdict = round(float(match.group(1)),2), match.group(2)
ltp = float(soup.find('td', {'class': 'pid-' + i + '-last'}).text.replace(',', ''))	

if(ltp<ten_ma):
    print(name,verdict,ten_ma,ltp)
time.sleep(5)
'''
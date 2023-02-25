#import pandas as pd
import requests
from bs4 import BeautifulSoup
ban = """
#############
 DOMAINS on IP
~####ZMARTLABS####~
"""
print(ban)

header = {'Cookie': 'session_token=cp6dv9tjvqigdf58d4rk5t3ml4',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Connection': 'keep-alive'}
url = 'https://networksdb.io/domains-on-ip/' 
ip = input("Enter IP: ")
api = url + ip
try:
    print('\nPlease Wait...')
    html = requests.get(api, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser' )
    ati = soup.find('div', class_='main-container block')
    dom = ati.find('pre').get_text(strip=True, separator=' ')
    print(dom)
    fl = str('Domains_on_'+ip)
    ch = input("\n\n|### SAVE RESULT?###| y/n  ")
    if ch == 'y':
        with open(f'{fl}.txt', 'w') as fi:
            fi.write(dom)
            fi.close
        print('\nFile saved as >>> ',fl)
    elif ch == 'n':
        pass
    else:
        exit()
except AttributeError:
    print('IP Not Found')
    exit()
except requests.ConnectionError:
    print("Can't connect to internet")
    exit()


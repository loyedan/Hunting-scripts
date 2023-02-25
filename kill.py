#!/usr/bin/python
# Author : Zack Marumo
# @VenomNoob
#Group link https://t.me/zackhosthunter
#Whatsapp +27676418732
# version : 0.02

import requests,sys
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

print("   ____    ___    ___          _		")   
print("  |___ \  / _ \  / _ \   ___  | |	")
print("    __) || | | || | | | / _ \ | |/ /	")
print("   / __/ | |_| || |_| || (_) ||   <	")
print("  |_____| \___/  \___/  \___/ |_|\_\ ")
print("   Happy Scanning Script by: Zack")
print("             @VenomNoob             	")   
print("      https://t.me/zackhosthunter   	")  

# COLORS #
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if (len(sys.argv) != 2):
  print("\n Error: Type python3 shoot.py yourfile.txt\n")
  sys.exit()

else:
  f = open(sys.argv[1],'r') 
  lines = f.readlines()
  f.close()

  filename = 'output_files/' + sys.argv[1].replace('../','') + '_output.txt'
  out = open(filename, 'w+')

  
for line in lines:
    try:
      
      if 'http://' in line.strip() or 'https://' in line.strip():
        url = line.strip()
      else:
        
        url = 'http://' + line.strip()
      
      s = requests.Session()
#      retry = Retry(connect=1, backoff_factor=0.5)
      
#      s.mount('http://github.com', HTTPAdapter(max_retries=1))
      r = s.head(url, timeout=1)
      response = r.headers
  
      out.write(url + ':' + str(r.status_code) + '\n')

    except requests.ConnectionError as e:
      print("\n", bcolors.ENDC + url + bcolors.FAIL + " Failed to connect ")
      continue
    except requests.Timeout as e:
        print("[!] : Timeout Error")
        continue
    except requests.RequestException as e:
        print("[!] : General Error")
        continue
    
    except KeyboardInterrupt:
      out.close()
      print("\nOutput saved in : " + filename + '\n')
      exit()
    
    # Printing the results
    if (r.status_code == 200):
    	try:
        	print("\n", '\x1b[6;30;42m' '[OK]200', bcolors.ENDC, ':' , url,r.headers['server'])
    	except KeyError:
    		print('server not found')
    
    if (r.status_code == 308):
    	try:
    		print("\n", '\x1b[6;39;40m' '[308]',bcolors.OKBLUE, ':' , url,r.headers['server'])
    	except KeyError:
    		print('server not found')
    		    
    if (r.status_code == 302):
       		print('\n', bcolors.FAIL, r.status_code, ' : ' , url,r.headers)

    if (r.status_code == 301):
    	try:
    		print("\n", '\x1b[6;39;40m' '[301]',bcolors.OKCYAN, ':' , url,r.headers['server'])
    	except KeyError:
    		print('server not found')
    
    if (r.status_code == 403):
    	try:
    		print("\n", '\x1b[6;39;40m' '[403]',bcolors.OKGREEN, ':' , url,r.headers['server'])
    	except KeyError:
    		print('server not found')
    		  
print("\nOutput saved in : " + filename + '\n')
out.close()



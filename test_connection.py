

import urllib.request
from urllib.error import HTTPError,URLError
from datetime import datetime
import time
import os

def check_internet(interval=60,urls=[r'http://www.google.com',r'https://github.com'],save_log=os.getcwd()):
    print('checking connection every '+str(interval/60)+' minutes')
    os.chdir(save_log)
    while True:
        for url in urls:
                
            now = datetime.now()
            string_salvar = "{:02d}/{:02d}/{:04d} {:02d}:{:02d}".format(now.day,
                                                                        now.month,
                                                                        now.year,
                                                                        now.hour,
                                                                        now.minute)
            try:
                test = urllib.request.urlopen(url,timeout = 15) 
                salvar_log = open('log.txt','a+')
                salvar_log.write(   string_salvar+' '+str(url)+ ' OK \n')
                salvar_log.close()
                print (string_salvar +' '+str(url)+' OK')
            except (HTTPError, URLError):
                salvar_log = open('log.txt','a+')
                salvar_log.write(string_salvar+' '+str(url)+ ' ERRO \n')
                salvar_log.close()
                print (string_salvar +' '+str(url)+ ' ERRO')
    
                
        time.sleep(interval)
        
if __name__ == '__main__':
    check_internet()
    
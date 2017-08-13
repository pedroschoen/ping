import urllib.request
from urllib.error import HTTPError,URLError
from datetime import datetime
import time
import os
import argparse

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
                salvar_log.write(string_salvar+' '+str(url)+ ' ERROR \n')
                salvar_log.close()
                print (string_salvar +' '+str(url)+ ' ERROR')
    
                
        time.sleep(interval)
     
        
parser = argparse.ArgumentParser()
parser.add_argument("-i","-interval",nargs='?',default=True)
parser.add_argument("-u","-url",nargs='?',default=True)
parser.add_argument("-s","-save",nargs='?',default=True)
args = parser.parse_args()

if args.i:
    interval=60
else:
    try:
        interval =  int(args.i)
    except:
        interval=60
        
if args.u:
    urls=[r'http://www.google.com',r'https://github.com']
else:
    try:
        urls = args.u.split(',')
        print(urls) 
    except:
        urls=[r'http://www.google.com',r'https://github.com']
        
if args.s:
    save_log=os.getcwd()
else:
    try:
        save_log=args.s
    except:
        save_log=os.getcwd()
        
                
        
if __name__ == '__main__':
    check_internet(interval=interval,urls=urls,save_log=save_log)
    
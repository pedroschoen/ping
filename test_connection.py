DEFAULT_URLS = ['http://www.google.com', 'https://github.com']

import urllib.request
from urllib.error import HTTPError,URLError
from datetime import datetime
import time
import os
import argparse

def check_internet(interval=60,urls=DEFAULT_URLS,save_log=os.getcwd()):
    print('checking connection every '+str(interval/60)+' minutes')
    os.chdir(save_log)
    while True:
        for url in urls:
                
            now = datetime.now()
            string_save = "{:02d}/{:02d}/{:04d} {:02d}:{:02d}".format(now.day,
                                                                        now.month,
                                                                        now.year,
                                                                        now.hour,
                                                                        now.minute)
            try:
                test = urllib.request.urlopen(url,timeout = 15) 
                with open('log.txt','a+') as save_log:
                    save_log.write('%s %s OK \n' %(string_save,str(url)))
               
                print ('%s %s OK' %(string_save,str(url)))
            except (HTTPError, URLError):
                with open('log.txt','a+') as save_log:
                    save_log.write('%s %s ERROR \n' %(string_save,str(url)))
                print ('%s %s ERROR' %(string_save,str(url)))
    
                
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
    urls=DEFAULT_URLS
else:
    try:
        urls = args.u.split(',')
        print(urls) 
    except:
        urls=DEFAULT_URLS
        
if args.s:
    save_log=os.getcwd()
else:
    try:
        save_log=args.s
    except:
        save_log=os.getcwd()
        
      
if __name__ == '__main__':
    check_internet(interval=interval,urls=urls,save_log=save_log)
    
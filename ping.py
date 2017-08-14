
import urllib.request
from urllib.error import HTTPError,URLError
from datetime import datetime
import time
import os
import argparse

DEFAULT_URLS = ['http://www.google.com', 'https://github.com']
DEFAULT_INTERVAL=60

def ping(interval=DEFAULT_INTERVAL,
                   urls=DEFAULT_URLS,
                   save_log=os.getcwd()):
    print(('checking connection every {} minutes').format(str(interval/60)))
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
                    save_log.write('{} {} OK \n'.format(string_save,str(url)))
               
                print ('{} {} OK'.format(string_save,str(url)))
            except(HTTPError, URLError):
                with open('log.txt','a+') as save_log:
                    save_log.write('{} {} ERROR \n'.format(string_save,str(url)))
                print ('{} {} ERROR'.format(string_save,str(url)))
        time.sleep(interval)
     
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-interval", "-i", nargs='?',default=DEFAULT_INTERVAL)
    parser.add_argument("-urls", "-u", nargs='?',default=DEFAULT_URLS)
    parser.add_argument("-save_log", "-s", nargs='?',default=os.getcwd())
    args = parser.parse_args()

    interval=int(args.interval)
    urls = args.urls
    if urls != DEFAULT_URLS:
        urls = args.urls.split(',')
    save_log = args.save_log
    
    ping(interval=interval,urls=urls,save_log=save_log)
    
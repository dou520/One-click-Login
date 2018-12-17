import requests
import os
import time

def openwifi():
    os.system('netsh wlan connect name=i-NUIST')
    time.sleep(5)
    
def killtask():
    os.system('TASKKILL /F /IM Google Chrome.exe ')
    
def login():
    thedata={'domain':'CMCC',
           'enablemacauth':'0',
           'password':'MTIzMzIx',
           'username':'18351803258'
          }     
    theheader={
    'Host': 'a.nuist.edu.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With':'XMLHttpRequest',
    'Referer':'http://a.nuist.edu.cn/',
    'Content-Length': '66',

    'Cookie':'unriseUsername=18351803258; sunriseDomain=CMCC; think_language=zh-CN; PHPSESSID=gibnas2673vgude396g6ie0qk3; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1',
    'Connection':'keep-alive',
}

    url="http://a.nuist.edu.cn/index.php/index/login"
    p=requests.post(url,data=thedata,headers=theheader)

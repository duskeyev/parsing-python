import requests
import queue
import threading

q= queue.Queue()
validProxies=[]

with open('ip_list.txt','r') as f:
    proxies = f.read().split('\n')
    for p in proxies:
        q.put(p)

def checkP():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json",
                               proxies={'http':proxy,
                                        'https':proxy})
        except:
            continue
        if res.status_code ==200:
            print(proxy)

for _ in range(10):
    threading.Thread(target=checkP).start()

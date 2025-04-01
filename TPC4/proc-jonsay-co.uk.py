import re
import shelve
import requests
from bs4 import BeautifulSoup as bs

d = shelve.open('pagecache.db')

def myget(url):
    if url not in d:
        print(f"... fetching {url}")
        d[url] = requests.get(url).text
    return d[url]
        
d_pt_cn = [] 
def proc_filho(txt, dom):
    dtf = bs(txt, 'lxml')
    for table in dtf.find_all('table', class_='mytable'):
        for tr in table.find_all('tr'):
            filhos = tr.find_all('td') 
            if len(filhos) == 3: # 3 colunas
                pt, py, cn = filhos
                d_pt_cn.append({'pt': pt.text, 'py': py.text,'cn': cn.text, "domain": dom})

def main():
    url = "https://www.jonsay.co.uk/dictionary.php?langa=Portuguese&langb=Chinese"
    txt = myget(url)
    dt = bs(txt, 'lxml')

    n = 1
    for link in dt.find_all('a', class_='nav'): # cada elemento da navbar
        dom = link.text
        txt2 = myget(link['href'])
        proc_filho(txt2, dom)
        n+=1
        if n == 3: break


main()

print(d_pt_cn)

d.close()


import re
import shelve
import requests
import jjcli
from bs4 import BeautifulSoup as bs

d = shelve.open('pagecache.db')

def myget(url):
    if url not in d:
        print(f"... fetching {url}")
        d[url] = requests.get(url).text
    return d[url]
        

def main():
    cl = jjcli.clfilter("s:")
    sep = cl.opt.get('-s', ' :: ') # permite passar um separador como argumento, senão usa ' :: '

    for url in cl.args:
        txt = myget(url)
        dt = bs(txt, 'lxml')
        n = 0
        for table in dt.find_all('table'):
            n += 1
            csv=""
            for tr in table.find_all('tr'):
                filhos = [re.sub(r"\s+", " ", f.text) for f in tr.find_all('td')]
                csv += sep.join(filhos) + "\n"
            print(f"==> {url}//{n}\n{csv}")
            

if __name__ == '__main__':
    main()
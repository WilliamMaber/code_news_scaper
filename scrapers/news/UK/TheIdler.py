Q ='[[wikidata:Q1411108]]'
urls = [
    "https://www.idler.co.uk/"
]
feeds = [
    "https://www.idler.co.uk/feed"
]
header={
    'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Linux',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}


from bs4 import BeautifulSoup
import requests

def article(url):
    content = requests.get(url,headers=header).content
    soup = BeautifulSoup(content, 'html.parser')
    headline =  soup.select('h1.entry-title')[0]
    for s in soup.select('script'):
        s.extract()
    content =  soup.select('.entry-content')[0]
    
article("https://www.idler.co.uk/article/who-modern-stoicism-misses-the-point/")

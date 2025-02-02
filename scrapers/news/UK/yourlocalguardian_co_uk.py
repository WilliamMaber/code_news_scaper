Q ='[[wikidata:Q17022580]]'
urls = [
    "https://www.yourlocalguardian.co.uk/"
]
feeds = [
    "https://www.yourlocalguardian.co.uk/news/rss/",
    "https://www.yourlocalguardian.co.uk/news/croydonnews/rss/",
    "https://www.yourlocalguardian.co.uk/news/suttonnews/rss/",
    "https://www.yourlocalguardian.co.uk/news/educationnews/rss/",
    "https://www.yourlocalguardian.co.uk/sport/nonleague/rss/",
    "https://www.yourlocalguardian.co.uk/sport/rss/",
    "https://www.yourlocalguardian.co.uk/sport/nonleague/rss/",
    "https://www.yourlocalguardian.co.uk/sport/nonleague/carshaltonathletic/rss/",
    "https://www.yourlocalguardian.co.uk/sport/nonleague/hamptonandrichmond/rss/",
    "https://www.yourlocalguardian.co.uk/sport/nonleague/tootingandmitcham/rss/",
    "https://www.yourlocalguardian.co.uk/sport/nonleague/other/rss/",
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
    headline =  soup.select('#article > h1')[0]
    #time =  soup.select("article > time")[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#subscription-content >:not(p,h1,h2,h3,h4,h5,h6,strong)'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('p:has([data-link-tracking="InArticle|Link"])'):
        s.extract()
    bodyCopy =  soup.select('.p402_hide')[0]
    
async def scan():
    return False
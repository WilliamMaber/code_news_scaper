Q ='[[wikidata:Q7363318]]'
urls = [
    "https://www.romseyadvertiser.co.uk/"
]
feeds = [
    "https://www.romseyadvertiser.co.uk/news/news/rss/",
    "https://www.romseyadvertiser.co.uk/news/business/rss/",
    "https://www.romseyadvertiser.co.uk/yoursay/rss/"
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
    headline =  soup.select('h1')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.article-first-paragraph > :not(p,h2,h3,h4,h5,h6)'):
        s.extract()
    bodyCopy =  soup.select('.p402_hide')[0] ### READ THE FULL STORY
    
async def scan():
    return False
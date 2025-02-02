Q ='[[wikidata:Q494792]]'
urls = [
    "https://www.thirdway.org/"
]
feeds = [

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
    headline =  soup.select('#main-content')[0]
    # time =  soup.select('#native-content-pub-date')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.article-body > :not(.teaser-content,.remainder-content)'):
        s.extract()
    for s in soup.select('.remainder-content > section > div > :not([data-qa="drop-cap-letter"])'):
        s.extract()
    for s in soup.select('.markup:contains("Support The Yorkshire Post and become a subscriber today")'):
        s.extract()
    bodyCopy =  soup.select('.article-body')[0]
    
async def scan():
    return False
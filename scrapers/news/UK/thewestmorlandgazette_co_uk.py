Q ='[[wikidata:Q17030995]]'
urls = [
    "https://www.thewestmorlandgazette.co.uk/"
]
# NO feed
feeds = [
    "https://www.thewestmorlandgazette.co.uk/news/rss/",
    "https://www.thewestmorlandgazette.co.uk/give-them-a-break/rss/",
    "https://www.thewestmorlandgazette.co.uk/tourism_guide/rss/",
    "https://www.thewestmorlandgazette.co.uk/obituaries/rss/"
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
    headline =  soup.select('h1.headline')[0]
    # time =  soup.select('#native-content-pub-date')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#subscription-content > :not(p)'):
        s.extract()
    bodyCopy =  soup.select('.p402_hide')[0]
    
async def scan():
    return False
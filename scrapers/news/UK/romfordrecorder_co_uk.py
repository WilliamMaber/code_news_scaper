Q ='[[wikidata:Q7363195]]'
urls = [
    "https://www.romfordrecorder.co.uk/"
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
    headline =  soup.select('[class="article__title mdc-typography--headline4"]')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('[class="article__detail-text mdc-typography--body1"] > :not(p,h2,h3,h4,h5,h6)'):
        s.extract()
    bodyCopy =  soup.select('[class="article__detail-text mdc-typography--body1"]')[0] ### READ THE FULL STORY
    
async def scan():
    return False
Q ='[[wikidata:Q22000337]]'
urls = [
    "https://www.theblackshirt.org/"
]
feeds = [
    "https://www.theblackshirt.org/rss/"
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
    headline =  soup.select('.post-full-title')[0]
    subtext =  soup.select('.post-full-custom-excerpt')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.post-content figure'):
        s.extract()
    bodyCopy = soup.select('.post-content')[0]
    
article("https://www.theblackshirt.org/2021/11/08/the-mystery-of-the-zodiac-killer/")
## ERROR uninow
Q ='[[wikidata:Q20746268]]'
urls = [
    "https://www.coventrytelegraph.net/"
]
feeds = [
"https://www.coventrytelegraph.net/news/?service=rss y",
"https://www.coventrytelegraph.net/news/coventry-news/?service=rss",
"https://www.coventrytelegraph.net/news/uk-world-news/?service=rss",
"https://www.coventrytelegraph.net/news/health/?service=rss",
"https://www.coventrytelegraph.net/all-about/crime?service=rss",
"https://www.coventrytelegraph.net/all-about/politics?service=rss",
"https://www.coventrytelegraph.net/all-about/education?service=rss",
"https://www.coventrytelegraph.net/news/motoring/?service=rss",
"https://www.coventrytelegraph.net/news/history/?service=rss",
"https://www.coventrytelegraph.net/news/news-opinion/?service=rss",
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
    headline =  soup.select('[itemprop="headline name"]')[0]
    subheadline =  soup.select('[itemprop="description"]')[0]
    for s in soup.select('[itemprop="articleBody"] > :not(p)'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:contains("Read more")'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:contains("Keep up with the latest news with our email alerts directly to your inbox")'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select('[itemprop="articleBody"]')[0] ### READ THE FULL STORY
    
async def scan():
    return False

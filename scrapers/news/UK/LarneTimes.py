urls = []
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
    headline =  soup.select("article > h1 ")[0]
    subheadline =  soup.select("article > h2 ")[0]
    #time =  soup.select("article > time")[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#content-wrapper >:not(.markup)'):
        s.extract()
    bodyCopy =  soup.select("#content-wrapper")[0]
    print(bodyCopy)
article("https://www.larnetimes.co.uk/news/crime/court-hears-concerned-member-of-public-stopped-over-the-limit-carnlough-driver-3447086")
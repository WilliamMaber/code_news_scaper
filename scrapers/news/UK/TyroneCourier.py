urls = [
    "https://www.tyronecourier.co.uk/"
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
    headline =  soup.select('h1[itemprop="headline name"] ')[0]
    # time =  soup.select('#native-content-pub-date')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('[itemprop="text"] > p:contains("Full stories and photos in this week\'s Courier.")'):
        s.extract()
    for s in soup.select('[itemprop="text"] > p:contains("Click here for Digital ePaper")'):
        s.extract()
    bodyCopy =  soup.select('[itemprop="text"]')[0]
    print(bodyCopy)
article("https://www.tyronecourier.co.uk/news/2021/11/11/news/fivemiletown-fraudster-unmasked-and-jailed-19772/")
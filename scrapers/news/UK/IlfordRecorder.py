urls = [
    "https://www.ilfordrecorder.co.uk/"
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
    headline =  soup.select('h1')[0]
    # for s in soup.select('.article-wrapper > :not(p,b,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    for s in soup.select('#main > :not(p, h1,h2,h3,h4,h5,h6) '):
        s.extract()
    article =  soup.select('#main')[0]
    print(article)
article("https://www.independent.co.uk/news/obituaries/nicholas-bagnall-independent-on-sunday-columnist-who-also-spent-more-than-half-a-century-with-the-telegraph-papers-a6882811.html")

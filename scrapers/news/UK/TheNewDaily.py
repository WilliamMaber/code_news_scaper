urls = [
    "https://thenewdaily.com.au/"
]
feeds = [
    "https://thenewdaily.com.au/feed"
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
    headline =  soup.select('[itemprop="name headline"] ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('[class="tnd-content-style tnd-content-style--article"]> :not(p)'):
        s.extract()
    content =  soup.select('[class="tnd-content-style tnd-content-style--article"]')[0]
    print(content)
article("https://thenewdaily.com.au/news/state/vic/2021/11/11/nsw-storm-floods/?breaking_live_scroll")

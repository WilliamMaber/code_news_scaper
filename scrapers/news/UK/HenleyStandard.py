urls = [
    "https://www.henleystandard.co.uk/"
]
feeds = [
    "https://www.henleystandard.co.uk/rss.jsp?sezione=2"
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
    datePublished =  soup.select('[itemprop="datePublished"]')[0]
    try:
        tags = soup.select('[itemprop="keywords"]')[0]
    except:
        pass
    for s in soup.select('#content-wrapper > div:not(.markup)'):
        s.extract()
    article =  soup.select('[itemprop="text"] > div')[0]
    print(article)
article("https://www.henleystandard.co.uk/news/goring/166227/physio-appears-on-crimewatch-with-back-care-advice.html")
### NEED JAVASCRIPT
urls = [
    "https://www.cheshire-live.co.uk/"
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
    # Need to add author
    article_body =  soup.select(".p402_hide")[0]
    for s in soup.select("script"):
        s.extract()
    headline =  soup.select('h1.headline')
    print(article_body)
article("https://www.yourlocalguardian.co.uk/news/19687215.police-arrest-man-armed-knife-sutton/")
urls = [
    "https://www.dudleynews.co.uk/"
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
    headline =  soup.select('.headline ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('div.cell_right_sub1 > a > img'):
        s.extract()
    bodyCopy =  soup.select('div.p402_hide')[0]
    print(bodyCopy)
article("https://www.dudleynews.co.uk/news/19690545.classical-concert-gig-caritas-set-former-stourbridge-church/")

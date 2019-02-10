import requests
from bs4 import BeautifulSoup
import json
ROOT_URL = 'https://inshorts.com/en/read'


def headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        print(headline.text)


def get_headers():
    return {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "_ga=GA1.2.474379061.1548476083; _gid=GA1.2.251903072.1548476083; __gads=ID=17fd29a6d34048fc:T=1548476085:S=ALNI_MaRiLYBFlMfKNMAtiW0J3b_o0XGxw",
        "origin": "https://inshorts.com",
        "referer": "https://inshorts.com/en/read/",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
response = requests.get(ROOT_URL)
assert response.status_code == 200
headlines(response.text)
##########################################
url = 'https://inshorts.com/en/ajax/more_news'
news_offset = 'apwuhnrm-1'

while True:
    response = requests.post(url, data={"category": "", "news_offset": news_offset}, headers=get_headers())
    if response.status_code !=200:
        print("Status code != 200")
        break

    response_json = json.loads(response.text)
    headlines(response_json["html"])
    news_offset = response_json["min_news_id"]

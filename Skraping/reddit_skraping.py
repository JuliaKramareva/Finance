import requests
from bs4 import BeautifulSoup

ROOT_URL = 'https://old.reddit.com/r/datascience/'

result_dict = {}

response = requests.get(ROOT_URL)
assert response.status_code == 200
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

from bs4 import BeautifulSoup
import requests

url = "https://boston.craigslist.org/search/sof"
response = requests.get(url)
assert response.status_code == 200
# print(response)
data = response.text
# print(data)
soup = BeautifulSoup(data, 'html.parser')
# tags = soup.find_all('a')
# for tag in tags:
#     print(tag.get('href'))
titles = soup.find_all("a", {"class":"result-title"})
# for title in titles:
#     print(title.text)

adresses = soup.find_all("span", {"class":"result-hood"})

# for adress in adresses:
#     print(adress.text)

jobs = soup.find_all('p', {"class":{'result-info'}})

for job in jobs:
    title = job.find('a', {'class':'result-title'}).test
    location_tag = job.find('span', {'class':'result-hood'})
    location = location_tag.text[2:-1] if location_tag else 'N/A'
    date = job.find('time', {'class':'result-date'}).text
    link = job.find('a', {'class':'result-title'}).get('href')
    print('Job Title:', title, '\nLocation', location, '\nDate:', date, '\nlink', link, '\n---')

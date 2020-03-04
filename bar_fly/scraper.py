# import requests

# url = 'https://iba-world.com/contemporary-classics/'
# page = requests.get(url)
# print(page)



from urllib.request import urlopen
from bs4 import BeautifulSoup

website = 'https://iba-world.com/iba-cocktails/'
page = urlopen(website)

soup = BeautifulSoup(page, 'html.parser')
results = soup.findAll('a', href=True, attrs={'class':'btn-readmore'})

for drink in results:
    print(drink['href'])
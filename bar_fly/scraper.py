
from urllib.request import urlopen
from bs4 import BeautifulSoup

website = 'https://iba-world.com/iba-cocktails/'
page = urlopen(website)

soup = BeautifulSoup(page, 'html.parser')
results = soup.findAll('a', href=True, attrs={'class':'btn-readmore'})

ingredients = []

def parseDrink(drink):
	website = str(drink['href'])
	page = urlopen(website)
	soup = BeautifulSoup(page, 'lxml')
	results = soup.find('div', attrs={'class':'col-sm-9'}).findAll('li')
	
	ingredients.append(results)

	# print(results)



for drink in results:
	parseDrink(drink)

for i in ingredients:
	for l in i:
		print(l.text)


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
	
	for i in results:
		for l in i:
			array = list(l)
			newArray = ' '
			for c in array:
				if c.isalpha() == False:
					array.remove(c)
				else:
					newArray.join(c)
				print(newArray)






			# ingredients.append(l)




for drink in results:
	parseDrink(drink)

for i in ingredients:
	print(i)
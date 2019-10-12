import bs4 as bs
import urllib
import sys

baseUrl = "https://www.mobafire.com"

champion = raw_input("Enter Champion... ")
url = baseUrl + '/league-of-legends/' + champion + '-guide'

sauce = urllib.urlopen(url).read()
soup = bs.BeautifulSoup(sauce,'lxml')

try:
	runesUrl = baseUrl + soup.find('div', class_='browse-list').find('a')['href']
except:
	print 'No such champion'
	sys.exit()
	
sauce = urllib.urlopen(runesUrl).read()
soup = bs.BeautifulSoup(sauce,'lxml')

def findRunes(type, index):
	spans = soup.findAll('div', class_='new-runes__' + type)[index].findAll('span')[1:]
	return list(map(lambda x : x.text, spans))
	
def findRunesTitles(index = 0):
	divs = soup.findAll('div', class_='new-runes__title')[2*index:2*+1]
	return list(map(lambda x : x.text, divs))

def findBonusRunes():
	spans = soup.find('div', class_='new-runes__shards').findAll('span')
	return list(map(lambda x : x['shard-type'], spans))

def findPrimaryRunes(index = 0):
	return findRunes('primary', index)

def findSecondaryRunes(index = 0):
	return findRunes('secondary', index)
# SEC.py

from urllib.request import urlopen

def getSearchPage(url):
	socket = urlopen(url)
	data = socket.read()
	socket.close()
	s = str(data, 'utf-8')
	return s

def findModifyPage()

#main------------------------------
company = input("Enter the docket of the company you'd like to search: ")
searchPage = getSearchPage("https://www.sec.gov/edgar/searchedgar/companysearch.html")
f = open("Search", "w")
f.write(searchPage)
f.close();
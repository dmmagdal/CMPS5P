# Edgar.py
# test the Edgar API for python

import time
from SECEdgar.crawler import SecCrawler

def getfilings():
	t1 = time.time()

	# create object
	seccrawler = SecCrawler()

	companyCode = 'AAPL' # compnay ticker symbol for Apple
	cik = '0000320193' # cik code for Apple
	date = '20010101' # date from which filings should be downloaded (01/01/2001 in this case)
	count = '10' # the number of filings

	seccrawler.filing_10Q(str(companyCode), str(cik), str(date), str(count))
	seccrawler.filing_10K(str(companyCode), str(cik), str(date), str(count))
	seccrawler.filing_8K(str(companyCode), str(cik), str(date), str(count))
	seccrawler.filing_13F(str(companyCode), str(cik), str(date), str(count))

	t2 = time.time()
	print("Total time taken: ")
	print(t2-t1)

if __name__ == "__main__":
	getfilings()

# program should return the compnay's 10Q, 10K, 8K, and 13F filings and save it to SEC-Edgar-data folder which 
# is created on runtime
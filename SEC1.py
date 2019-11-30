# user defined companyidx_links.txt is a text file with one line for each quarter  – 1993QTR1company.idx https://www.sec.gov/Archives/edgar/full-index/1993/QTR1/company.idx
 
links = 'companyidx_links.txt'
dir = 'company_idx/'
 
# import libraries
import urllib.request
 
# download and rename
with open(links) as linksfile:
        for line in linksfile:
            id = line[:19]
            url = line[20:]
            urllib.request.urlretrieve(url, dir + id)

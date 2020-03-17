# Interact-with-SEC-Filings
Codes to work with SEC Filings, from EDGAR system. Its a two parts process.

**1. SEC Filings: Download company.idx (SEC1.py)**

In this one you have to first download links of all the files, which are available on SEC server. You begin with 'companyidx_links.txt' and the program downloads all the idx file for you.
The current file has index till 2019, you could add the latest ones from this website: https://www.sec.gov/Archives/edgar/full-index/

**2. SEC Filings: Download forms listed in company.idx (SEC2.py)

Here you specify the forms you would like to download under "formtype_list", and directory where you would like to save. 

All the best !!

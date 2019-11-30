# user defined
companyidx_dir = 'company_idx'
formtype_list = ['DEF 14A', ' DEF 14A', 'DEF 14A ']
dir = 'DEF14A/'
 
# import libraries
import urllib.request
import os
 
# download
def down_form(companyidx, formtype_list):
 
    if not os.path.exists(dir + companyidx[11:20]):
        os.makedirs(dir + companyidx[11:20])
 
    with open(companyidx) as idxfile:
        for row in idxfile:
            array = row.split('  ') # double space
            array = [x for x in array if x != '']
 
            if len(array) > 4 and array[1] in formtype_list:
                url = 'https://www.sec.gov/Archives/' + array[4]
                id = array[4][11:].replace('/' , '_')
                urllib.request.urlretrieve(url, dir + companyidx[11:20] + '/' + id)
 
idxall = [os.path.join(companyidx_dir,f) for f in os.listdir(companyidx_dir)]
for idx in idxall:
    down_form(idx, formtype_list)

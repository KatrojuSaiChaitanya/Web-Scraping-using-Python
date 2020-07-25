# packages

from tld import get_tld
import requests
import re
import csv
import json
import pandas as pd
from bs4 import BeautifulSoup
try: 
	from googlesearch import search 
except ImportError: 
	print("No module named 'google' found")
	
#code to googlesearch
search_list = []
# open the web_urls file to clean the already present data   
f = open("web_urls.txt", "r+")  
  
# absolute file positioning 
f.seek(0)  
  
# to erase all data  
f.truncate()

k = 0
m=True
while(m):
        s=input('Type y/n whether you want to enter the organization name: ')
        if(s=='y'):
                query = input('enter the organization: ')
                search_list.append(query)
                file = open("web_urls.txt", "a")
                for o in search(query, tld="co.in", num=1, stop=1, pause=2): 
                        url_site=o
                        file.write(url_site)
                        file.write('\n')
        if(s=='n'):
                m=False 
                print('Thankyou...')
                file.close()

# function to remove duplicates

def remove_dup_email(x):
  return list(dict.fromkeys(x))

def remove_dup_phone(x):
  return list(dict.fromkeys(x))

def get_email(html):
    try:
        email = re.findall("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",html)
        nodup_email = remove_dup_email(email)
        return nodup_email
    except:
        pass

def get_phone(html):
    try:
        phone = re.findall(r"(\d{2} \d{3,4} \d{3,4})", html)
        phone1= re.findall(r"((?:\d{2,3}|\(\d{2,3}\))?(?:\s|-|\.)?\d{3,4}(?:\s|-|\.)\d{4})",html)
        for p in phone1:
             phone.append(p)
        nodup_phone = remove_dup_phone(phone)
        return nodup_phone
    except:
        pass

urls = ''


# load website url links

with open('web_urls.txt', 'r') as f:
    for line in f.read():
        urls +=line

#convert a string to a list of urls
        
urls = list(filter(None, urls.split('\n')))

# Looping over the urls

for url in urls:

    #http requests to the urls
        
    res = requests.get(url)
    print('searched home url: ', res.url) 

    # parse the response
    
    info = BeautifulSoup(res.text,'lxml')


    # extract contact data from home url

    emails_home = get_email(info.get_text())
    phones_home = get_phone(info.get_text())

    emails_f = emails_home
    phones_f = phones_home

    
    # create a data structure to store the contacts

    contacts_f = {'Searches':search_list[k],'website':res.url,'Email':'','Phone':''}
    k=k+1

    # extract contact of the link if available
    try:
        contact = info.find('a', text = re.compile('contact', re.IGNORECASE))['href']
        if 'http' in contact:
            contact_url = contact
        else:
            contact_url = res.url[0:-1] + contact

        # searching contact URL
        
        res_contact = requests.get(contact_url)

        contact_info = BeautifulSoup(res_contact.text, 'lxml').get_text()


        print('searched contact url:', res_contact.url)

        # extract contact data
        
        emails_contact = get_email(contact_info)
        phones_contact = get_phone(contact_info)

        #combining email contacts and email home into a single list

        emails_f = emails_home

        for ele1 in emails_contact:
            emails_f.append(ele1)

        #combining phone contacts and phone contacts into a single list
    
        phones_f = phones_home

        for ele2 in phones_contact:
            phones_f.append(ele2)
        
    except:
        pass


            
    # removing duplicates

    emails_f = remove_dup_email(emails_f)
    phones_f = remove_dup_email(phones_f)

    contacts_f['Email']= emails_f
    contacts_f['Phone']= phones_f
    
    # converting into a data set
    
    print('\n', json.dumps(contacts_f, indent=2))

    # dumping the data into the csv file

    with open('organization_info.csv', 'a') as f:

        #creater csv writer object

        writer = csv.DictWriter(f, fieldnames=contacts_f.keys())

        #writer.writeheader()

        #append rows to the csv

        writer.writerow(contacts_f)

 


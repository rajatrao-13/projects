#site name:http://cert-in.org.in/s2cMainServlet?pageid=PUBWEL01

import requests
from bs4 import BeautifulSoup
print "enter the site"
url = raw_input()
source_code = requests.get(url)
plain_text = source_code.content
soup = BeautifulSoup(plain_text, "lxml")
#div = soup.find('span','BContent')
#print ''.join(map(str, div.contents))
links = 'Link:'
content = 'Title:'
dates = 'Date:'
i = 0
for link in soup.findAll('td',{'class':'Content'}):
    i = i + 1
    for val in link.findAll('a'):
        print i
        print content + val.get_text()
        print links + val.get('href')
    for date in link.findAll('span',{'class':'DateContent'}):
        print dates + date.get_text()

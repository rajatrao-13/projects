import requests
from bs4 import BeautifulSoup
print "Enter the site"
url = raw_input()
source_code = requests.get(url)
plain_text = source_code.content
soup = BeautifulSoup(plain_text, "lxml")
for link in soup.find_all('a'):
        value = link.get('href')
        for line in  value.splitlines():
            if "facebook" in line:
                print line
            if "youtube" in line:
                print line
            if "twitter" in line:
                print line
            if "linkedin" in line:
                print line
            if "xml" in line:
                print line
            if "rss" in line:
                print line
          

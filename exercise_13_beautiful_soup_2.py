import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter URL: ')
count = int(input('Enter Count: '))
position = int(input('Enter Position: '))

# Retrieve all of the anchor tags
for count in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')[position-1]     
    url = tag.get('href', None)

print(url)
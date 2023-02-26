import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

# info = json.loads(data)
# print('User count:', len(info))

count_sum = sum([int(x['count']) for x in json.loads(data)['comments']])

print(count_sum)
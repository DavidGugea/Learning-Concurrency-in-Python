import urllib.request
import time
from bs4 import BeautifulSoup

t0 = time.perf_counter()

req = urllib.request.urlopen("http://example.com")

t1 = time.perf_counter()

print("Total time to fetch page: {0} seconds".format(t1 - t0))

soup = BeautifulSoup(req.read(), "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))

t2 = time.perf_counter()

print("Total execution time: {0} seconds".format(t2-t0))
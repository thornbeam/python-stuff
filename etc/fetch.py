#import urllib.request
#contents = urllib.request.urlopen("http://archive.sensor.community").read()

from bs4 import BeautifulSoup
import requests
from datetime import date
from datetime import timedelta
import time

start = time.time()

website = "http://archive.sensor.community"
yesterday = date.today() - timedelta(days = 1)
base_url = website + "/" + str(yesterday)
page = requests.get(base_url)
soup = BeautifulSoup(page.content, "html.parser")

for i in soup.find_all("a", href = True):
    if (str(yesterday) in i["href"]):
        url = base_url + "/" + i["href"]
        print(url)

end = time.time()

time = end - start
print("time:", time)

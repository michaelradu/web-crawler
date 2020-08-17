import os
import requests
from bs4 import BeautifulSoup

url = ['']


def vizitate(site):
    file = open("visited.txt", "w+")
    file.write(site)
    file.close()
    parsed1 = BeautifulSoup(requests.get(site).text, "html.parser")
    print(requests.get(site).headers)
    for link in parsed1.findAll('a'):
        if (link.get("href").find('/') == 0) and (link.get("href").find('.pdf') == -1):
            url.append(link.get("href"))

vizitate(url[0])
print(url)

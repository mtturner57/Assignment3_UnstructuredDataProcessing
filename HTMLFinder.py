import requests
from bs4 import BeautifulSoup, SoupStrainer
import csv

urlArray = list()
urlArray2 = list()
urlArray3 = list()
urlArray4 = list()
urlArray5 = list()

foundUrls = list()
foundUrlsNum = list()

r = requests.get('http://www.utexas.edu/')

soup = BeautifulSoup(r.content, "lxml")

for link in soup.find_all('a',  href=True):
    try:
        url = link['href']
        if(url[:21] != 'http://www.utexas.edu'):
                url = "http://www.utexas.edu" + url
        r = requests.get(url)
        if url not in urlArray:
            urlArray.append(url)
        if url not in foundUrls:
            foundUrls.append(url)
        else:
            print("First Level: Duplicate url found: " + url)
    except requests.exceptions.SSLError as e:
        pass
    except requests.exceptions.ConnectionError as c:
        pass
    except requests.exceptions.InvalidURL as i:
        pass
#        else:
#            ind = foundUrls.index("http://www.utexas.edu" + url)

print(len(urlArray))

for a in urlArray:
    try:
        r = requests.get('' + a)
        soups = BeautifulSoup(r.content, "lxml")
        for link in soups.find_all('a', href=True):
            url = link['href']
            if(url[:21] != 'http://www.utexas.edu'):
                url = "http://www.utexas.edu" + url
            r = requests.get(url)
            if url not in urlArray2:
                urlArray2.append(url)
            if url not in foundUrls:
                foundUrls.append(url)
            else:
                print("Second Level: Duplicate url found: " + url)
#                else:
#                    ind = foundUrls.index("http://www.utexas.edu" + url)
    except requests.exceptions.SSLError as e:
        pass
    except requests.exceptions.ConnectionError as c:
        pass
    except requests.exceptions.InvalidURL as i:
        pass

print(len(urlArray2))

for a in urlArray2:
    try:
        r = requests.get('' + a)
        soups = BeautifulSoup(r.content, "lxml")
        for link in soups.find_all('a', href=True):
            url = link['href']
            if(url[:21] != 'http://www.utexas.edu'):
                url = "http://www.utexas.edu" + url
            r = requests.get(url)
            if url not in urlArray3:
                urlArray3.append(url)
            if url not in foundUrls:
                foundUrls.append(url)
            else:
                print("Third Level: Duplicate url found: " + url)
    except requests.exceptions.SSLError as e:
        pass
    except requests.exceptions.ConnectionError as c:
        pass
    except requests.exceptions.InvalidURL as i:
        pass

print(len(urlArray3))

for a in urlArray3:
    try:
        r = requests.get('' + a)
        soups = BeautifulSoup(r.content, "lxml")
        for link in soups.find_all('a', href=True):
            url = link['href']
            if(url[:21] != 'http://www.utexas.edu'):
                url = "http://www.utexas.edu" + url
            r = requests.get(url)
            if url not in urlArray4:
                urlArray4.append(url)
            if url not in foundUrls:
                foundUrls.append(url)
            else:
                print("Fouth Level: Duplicate url found: " + url)
 #               else:
 #                   ind = foundUrls.index("http://www.utexas.edu" + url)
    except requests.exceptions.SSLError as e:
        pass
    except requests.exceptions.ConnectionError as c:
        pass
    except requests.exceptions.InvalidURL as i:
        pass

print(len(urlArray4))

for a in urlArray4:
    try:
        r = requests.get('' + a)
        soups = BeautifulSoup(r.content, "lxml")
        for link in soups.find_all('a', href=True):
            url = link['href']
            if(url[:21] != 'http://www.utexas.edu'):
                url = "http://www.utexas.edu" + url
            r = requests.get(url)
            if url not in urlArray5:
                urlArray5.append(url)
            if url not in foundUrls:
                foundUrls.append(url)
            else:
                print("Fifth Level: Duplicate url found: " + url)
 #               else:
 #                   ind = foundUrls.index("http://www.utexas.edu" + url)
    except requests.exceptions.SSLError as e:
        pass
    except requests.exceptions.ConnectionError as c:
        pass
    except requests.exceptions.InvalidURL as i:
        pass

#print(len(urlArray5))
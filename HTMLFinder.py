import requests
from bs4 import BeautifulSoup, SoupStrainer

urlArray = list()
urlArray2 = list()
urlArray3 = list()
urlArray4 = list()
urlArray5 = list()

foundUrls = list()
foundUrlsNum = list()

r = requests.get('http://www.utexas.edu/')

soup = BeautifulSoup(r.content, "lxml")

for link in soup.find_all('a', class_='sub-nav-link', href=True):
    url = link['href']
    if url not in foundUrls:
         if(url[:4] == 'http'):
            urlArray.append(url)
            foundUrls.append(url)
#         else:
#            urlArray2.append("http://www.utexas.edu" + url)
#            foundUrls.append("http://www.utexas.edu" + url)
    else:
        if(url[:4] == 'http'):
            ind = foundUrls.index(url)
#        else:
#            ind = foundUrls.index("http://www.utexas.edu" + url)

print(len(urlArray))

for a in urlArray:
    try:
        r = requests.get('' + a)
        soups = BeautifulSoup(r.content, "lxml")
        for link in soups.find_all('a', class_='sub-nav-link', href=True):
            url = link['href']
            if url not in foundUrls:
                if(url[:4] == 'http'):
                    urlArray2.append(url)
                    foundUrls.append(url)
                else:
                    urlArray2.append("http://www.utexas.edu" + url)
                    foundUrls.append("http://www.utexas.edu" + url)
            else:
                if(url[:4] == 'http'):
                    ind = foundUrls.index(url)
#                else:
#                    ind = foundUrls.index("http://www.utexas.edu" + url)
    except requests.exceptions.SSLError as e:
        print(e)
    except requests.exceptions.ConnectionError as c:
        print(c)

print(len(urlArray2))

for a in urlArray2:
    try:
        r = requests.get('' + a)
        soups = BeautifulSoup(r.content, "lxml")
        for link in soups.find_all('a', class_='sub-nav-link', href=True):
            url = link['href']
            if url not in foundUrls:
                if(url[:4] == 'http'):
                    urlArray3.append(url)
                    foundUrls.append(url)
                else:
                   urlArray3.append("http://www.utexas.edu" + url)
                   foundUrls.append("http://www.utexas.edu" + url)
            else:
                if(url[:4] == 'http'):
                    ind = foundUrls.index(url)
#                else:
#                   ind = foundUrls.index("http://www.utexas.edu" + url)
    except requests.exceptions.SSLError as e:
        print(e)
    except requests.exceptions.ConnectionError as c:
        print(c)

print(len(urlArray3))

for a in urlArray3:
    try:
        r = requests.get('' + a)
        soups = BeautifulSoup(r.content, "lxml")
        for link in soups.find_all('a', class_='sub-nav-link', href=True):
            url = link['href']
            if url not in foundUrls:
                if(url[:4] == 'http'):
                    urlArray4.append(url)
                    foundUrls.append(url)
                else:
                   urlArray4.append("http://www.utexas.edu" + url)
                   foundUrls.append("http://www.utexas.edu" + url)
            else:
                if(url[:4] == 'http'):
                    ind = foundUrls.index(url)
 #               else:
 #                   ind = foundUrls.index("http://www.utexas.edu" + url)
    except requests.exceptions.SSLError as e:
        print(e)
    except requests.exceptions.ConnectionError as c:
        print(c)

print(len(urlArray4))

for a in urlArray4:
    print(len(urlArray5))
    try:
        r = requests.get('' + a)
        soups = BeautifulSoup(r.content, "lxml")
        for link in soups.find_all('a', class_='sub-nav-link', href=True):
            url = link['href']
            if url not in foundUrls:
                if(url[:4] == 'http'):
                    urlArray5.append(url)
                    foundUrls.append(url)
                else:
                   urlArray5.append("http://www.utexas.edu" + url)
                   foundUrls.append("http://www.utexas.edu" + url)
            else:
                if(url[:4] == 'http'):
                    ind = foundUrls.index(url)
 #               else:
 #                   ind = foundUrls.index("http://www.utexas.edu" + url)
    except requests.exceptions.SSLError as e:
        print(e)
    except requests.exceptions.ConnectionError as c:
        print(c)

#print(len(urlArray5))
# Yosvany Blanco
# CSCE 4430 (Quentin Mayo)
# Project question 3

# must install the "requests" module
# must also install "BeautifulSoup4" Module
# both can be found on Pip https://pip.pypa.io/en/stable/

# developed and tested on Python 3.5.2
import requests
import sys
from bs4 import BeautifulSoup

url = "http://www.technewsworld.com/"
r = requests.get(url)
# check that connection worked
if r.status_code != 200:
    print("Failed to connect to server error code: %d" %(r.status_code))
    print("You typed '%s' is this correct?" %(url))
    sys.exit(1)
soup = BeautifulSoup(r.content, "html.parser")

myTitles = soup.find_all("div", {"class": "title"})
myDates = soup.find_all("div", {"class": "date"})
print("Top 10 News Stories on Technewsworld.com")
for i in range(0,10):
    print("%d:" %(i+1))
    # handle titles with subtitles
    if len(myTitles[i].contents) > 1:
        print(myTitles[i].contents[2].text)
        print("www.technewsworld.com%s" %myTitles[i].contents[2].get('href'))
    else:
        print(myTitles[i].contents[0].text)
        print("www.technewsworld.com%s" %myTitles[i].contents[0].get('href'))
    # print out the dates for each title
    print(myDates[i].contents[0])
    print()
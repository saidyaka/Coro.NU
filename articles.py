import os.path
import requests
from bs4 import BeautifulSoup
import twet

def checkExistence():
    if os.path.exists("/home/pi/Soup/art.txt"):
        pass
    else:
        file = open("/home/pi/Soup/art.txt", 'w')
    
        file.close()

webp=  'https://www.northwestern.edu/coronavirus-covid-19-updates/developments/index.html'

page = requests.get(webp)
soup = BeautifulSoup(page.text,'html.parser')
graph = soup.find(class_='news')
date = graph.find('div')
canvas = graph.find('a')
date = date.contents[0]
title = canvas.contents[0]


link= "https://www.northwestern.edu/coronavirus-covid-19-updates/developments/"+str(canvas.get('href'))
checkExistence()
file = open('/home/pi/Soup/art.txt', 'r')
content =file.read()
file.close

if str(content) != title:
    twert = "Latest Update From @NorthwesternU:\n(Posted "+ date + ")\n\n"+ "'" + title + "'\n\n" + "Source: " + link
    print(twert)
    open('/home/pi/Soup/art.txt', 'w').close()
    file = open('/home/pi/Soup/art.txt', 'w')
    file.write(title)
    file.close()
    twet.tweetIt(twert)
    


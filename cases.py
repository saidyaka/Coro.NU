import os.path
import requests
from bs4 import BeautifulSoup
import twet

#Check Existence of the file written into
def checkExistence():
    if os.path.exists("/home/pi/Soup/last.txt"):
        pass
    else:
        file = open("/home/pi/Soup/last.txt", 'w')
    
        file.close()

#Copy into a file so we can compare with the new pulled data        
def copyInto(sta):
    open('/home/pi/Soup/last.txt', 'w').close()
    file = open('/home/pi/Soup/last.txt', 'w')
    file.write(sta)
    file.close()

#Takes the information and formats it for the tweet
def cleaner(twt):
    
    
    dat = twt.index(':')
    sent = twt
    wert = "COVID19 @NorthwesternU\n\n" + twt[0: dat] + ":\n\n"
    twt = twt[dat+2:len(twt)]
    dat = twt.index(',')
    wert+= "👩‍🏫 "+ twt[0:dat]+'\n'
    twt = twt[dat+2 : len(twt)]
    dat = twt.index(',')
    wert+= "👨‍🍳 " + twt[0:dat] + '\n'
    twt = twt[dat+2 : len(twt)]
    if twt.find("Build") > -1:
        dat = twt.index(',')
        sent = twt
        wert+= "🎓 " + twt[0: dat]+ '\n'
        twt = twt[dat+2: len(twt)]

    else:
        dat = len(twt)
        wert+= "🎓 " + twt[0: dat]+ '\n'
        twt = "Buildings: Not Provided"
    wert+= "🏢 " + twt
    wert+= '\n\nSource: http://bitly.ws/9p8U'
    print(wert)
    twet.tweetIt(wert)
   # print(len(wert))

    


webp=  'https://www.northwestern.edu/coronavirus-covid-19-updates/developments/confirmed-cases.html'

page = requests.get(webp)
soup = BeautifulSoup(page.text,'html.parser')
graph = soup.find(class_='content')
canvas = graph.find('canvas')
canvas =canvas.contents[0]
checkExistence()
file = open('/home/pi/Soup/last.txt', 'r')
cont = file.read()
file.close

if cont != canvas:
    canvaslen = len(canvas)
    lastoc = canvas.rindex('-')
    for i in range(lastoc-8,lastoc):
        if canvas[i] == " ":
         cleaner(canvas[i+1: canvaslen])
         copyInto(canvas)
         break



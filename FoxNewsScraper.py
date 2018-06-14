import requests
from bs4 import BeautifulSoup
import urllib

stories = []

def getTheGoodStuff(newsstories):
    global stories
    for data in newsstories:
        htmlatag = data.find("h2", class_="title").find("a")
        headline = htmlatag.getText()
        url = htmlatag.get("href")
        d = {"headline" : headline,
             "url" : url}
        stories.append(d)

def scrapeWebsites():
    global stories
    
    # Getting stories from Fox News.
    foxnews = "http://www.foxnews.com/"
    page = urllib.urlopen(foxnews)
    r  = requests.get(foxnews)
    data = r.text
    soup = BeautifulSoup(data,"lxml")
    for i in range(0, 15):
        foundstories = soup.find_all("article", class_="article story-" + str(i))
        getTheGoodStuff(foundstories)
    
def displayStories():
    global stories
    for i in range(0, len(stories)):
        print stories[i]["headline"]
        print stories[i]['url']
        print ""
    
scrapeWebsites()
displayStories()
        

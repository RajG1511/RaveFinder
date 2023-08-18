import requests
from datetime import date
import EventCreator
from dotenv import load_dotenv
import os

load_dotenv
lastfmkey = os.environ.get("lastfmkey")
edmkey = os.environ.get("edmtrainkey")
raveList = []

def getListeners(name) -> int:
    global lastfmkey
    response = requests.get(
        f'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={name}' + '&api_key=' + f'{lastfmkey}' + '&format=json')
    temp = response.json()
    try:
        return int(temp['artist']['stats']['listeners'])
    except KeyError:
        return -1

def loadRaves(city) -> list:
    global raveList
    raveList.clear()
    if city == "":
        return []
    edmTrainResponse = requests.get('https://edmtrain.com/api/events?locations?state=Nevada&city=Laggs%20Vegas&client=' + edmkey)
    dict = edmTrainResponse.json()
    eventList = dict['data']
    id = 0
    for event in eventList:
        if city in event['venue']['location']:
            artists = []
            for artist in event['artistList']:
                artists.append(artist['name'])
            dateParts = event['date'].split('-')
            eventDate = date(int(dateParts[0]), int(dateParts[1]), int(dateParts[2]))
            listeners = []
            for artist in artists:
                listeners.append(getListeners(artist))
            if len(listeners) == 0:
                continue

            temp = max(listeners)
            if temp <= 70000:
                continue
            raveList.append({'artists': artists, 'date': eventDate, 'listeners': temp, 'dateString': eventDate.strftime('%A %dth %B %Y'), 'id': id})
            id += 1
    return raveList

def createEvent(index):
    EventCreator.createEvent(raveList[index])

def addAllRaves():
    EventCreator.addAllRaves(raveList)




#calendarTest.createEvent(houstonDict)
import datetime as dt
from dotenv import load_dotenv
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/calendar']


def addAllRaves(eventList):
    creds = None
    if os.path.exists("token.json"):
        print("path exists")
        creds = Credentials.from_authorized_user_file("token.json")
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        for eventDict in eventList:
            event = {
            "summary": eventDict['artists'],
            "location": "",
            "description": "Some more details on this awesome event",
            "colorId": 6,
            "start": {
                "dateTime": str(eventDict['date']) + "T21:00:00-05:00",
                "timeZone": "America/Chicago"
            },
            "end": {
                "dateTime": str(eventDict['date']) + "T23:59:59-05:00",
                "timeZone": "America/Chicago"
            }
            }
            event = service.events().insert(calendarId="primary", body=event).execute()
        
    except HttpError as error:
        print("An error occurred", error)

def createEvent(eventDict):
    creds = None
    if os.path.exists("token.json"):
        print("path exists")
        creds = Credentials.from_authorized_user_file("token.json")
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        event = {
            "summary": eventDict['artists'],
            "location": "",
            "description": "Some more details on this awesome event",
            "colorId": 6,
            "start": {
                "dateTime": str(eventDict['date']) + "T21:00:00-05:00",
                "timeZone": "America/Chicago"
            },
            "end": {
                "dateTime": str(eventDict['date']) + "T23:59:59-05:00",
                "timeZone": "America/Chicago"
            }
        }
        event = service.events().insert(calendarId="primary", body=event).execute()
    except HttpError as error:
        print("An error occurred", error)
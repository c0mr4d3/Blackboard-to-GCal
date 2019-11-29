# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 02:29:43 2019

@author : Siddharth
"""

import csv

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def addEvents():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    with open("test.csv","r") as file:
        reader = csv.reader(file,delimiter=",")
        events_list = list(reader)
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)


    for x in range(len(events_list)):
        if x%2==0:
                event = {
                    'summary':events_list[x][0],
                    'description':events_list[x][3],
                    'start':{'date':events_list[x][1][:10]},
                    'end':{'date':events_list[x][2][:10]}
                    }
                event = service.events().insert(calendarId='primary', body=event).execute()
                print ('Event created: %s' % (event.get('htmlLink')))

        

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 03:04:27 2019

@author : Siddharth
"""

from icalendar import Calendar
import csv


class Conv():
    def __init__(self):
        self.csvdata = []
        self.calendar = None
        
    def read_calendar(self,location_calendar):
        with open(location_calendar,'r') as cal_file:
            cal_data = cal_file.read()
        #loading to an object that segregates the data acc to type
        self.calendar = Calendar.from_ical(cal_data)
        return self.calendar
    
    def conv_to_csv(self):
        
        for event in self.calendar.subcomponents:
            if event.name != 'VEVENT':
                continue
            data_row = [
                event.get('SUMMARY'),
                event.get('DTSTART').dt,
                event.get('DTEND').dt,
                event.get('DESCRIPTION') 
                ]
#            print("Read event ",event.get('SUMMARY'))
            data_row = [str(x) for x in data_row]
            self.csvdata.append(data_row)        
            
            
    def write_csv(self,location_csv):
        with open(location_csv,'w+') as csv_file:
            csvwriter = csv.writer(csv_file)
            for data_row in self.csvdata:
                csvwriter.writerow([rowdata.strip() for rowdata in data_row])
            

def makecsv():
    conv = Conv()
    conv.ical = 'learn.ics'
    conv.csv = 'test.csv'
    conv.read_calendar(conv.ical)
    conv.conv_to_csv()
    conv.write_csv(conv.csv)

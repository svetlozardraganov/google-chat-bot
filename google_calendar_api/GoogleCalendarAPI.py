from __future__ import print_function
##import datetime
from datetime import datetime, timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pathlib
current_folder_path = pathlib.Path(__file__).parent.resolve()
parrent_folder_path = current_folder_path.parents[0]

#To import HangoutsBot properly it's folder needs to be added to Path
import sys
sys.path.insert(1, parrent_folder_path.as_posix())
import HangoutsBot


#Get system arguments if any
try:
    argument_cmd = sys.argv[1]

except:
    argument_cmd = None



class GoogleCalendar():
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


    def __init__(self):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    current_folder_path/'credentials.json', GoogleCalendar.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

        #get credentials from file
        file_path = parrent_folder_path / "credentials.txt"
        f = open(file_path, "r")

        lines = f.readlines()
        for line in lines:
            if 'releases_calendar_id' in line:
                self.releases_calendar_id = line.split()[1]
                print(self.releases_calendar_id)
            
            if 'support_3d_calendar_id ' in line:
                self.support_3d_calendar_id  = line.split()[1]
                print(self.support_3d_calendar_id )


    def get_this_week_releases(self):
        # Get this week product releases
        #Get start/end days of current week

        output = ""

        today = datetime.now().date()
        #calculate week start/end date
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        #convert week start/end date to datetime object with time set to min/max
        #https://stackoverflow.com/questions/1937622/convert-date-to-datetime-in-python
        week_start = datetime.combine(week_start, datetime.min.time())
        week_end = datetime.combine(week_end, datetime.max.time())
        
        #convert week start date-tme to isoformat + Z time zone (UTC time)
        week_start = week_start.isoformat() + 'Z'
        week_end = week_end.isoformat() + 'Z'
        
 
##        print("Today: " + str(today))
##        print("Start: " + str(week_start))
##        print("End: " + str(week_end))
##        
##        now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
##        print("now=",now)
##        
        self.releases_calendar_id 
        

        print('Getting this week events')
        events_result = self.service.events().list(calendarId=self.releases_calendar_id,
                                            timeMin=week_start, timeMax=week_end,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            output = None
            
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
##            print(start, event['summary'])
            output = output + start[:10] + " " + event['summary'] + "\n"
            
        print(output)
        return output



    def get_whos_on_the_phone_this_week(self):
        # Get this week phone responsibles

        output = ""

        today = datetime.now().date()

        #convert week start/end date to datetime object with time set to min/max
        #https://stackoverflow.com/questions/1937622/convert-date-to-datetime-in-python
        today_start = datetime.combine(today, datetime.min.time())
        today_end = datetime.combine(today, datetime.max.time())

        #adding 8 hours offset to today start/end variables since it captures event from the next day
        today_start = today_start + timedelta(hours=8)
        today_end = today_end - timedelta(hours=8)
        
        #convert week start date-tme to isoformat + Z time zone (UTC time)
        today_start = today_start.isoformat() + 'Z'
        today_end = today_end.isoformat() + 'Z'

        
        print('Getting todays Phone responsibilities events in Support 3D Team calendar ')
        events_result = self.service.events().list(calendarId=self.support_3d_calendar_id ,
                                            timeMin=today_start, timeMax=today_end,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            output = None
            
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            
            if "Phone" in event['summary']:
                output = output + start[:10] + " " + event['summary'] + "\n"
            
        print(output)
        return output

    

    def get_calendars(self):
        
        #https://developers.google.com/calendar/v3/reference/calendarList/list
        page_token = None
        while True:
          calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
          for calendar_list_entry in calendar_list['items']:
            print("name = ",calendar_list_entry['summary'])
            print("|-> id = ",calendar_list_entry['id'])
          page_token = calendar_list.get('nextPageToken')
          if not page_token:
            break



##if __name__ == '__main__':
##    instance = GoogleCalendar()
##    instance.get_upcomming_releases()

##    instance.get_calendars()


gcalendar = GoogleCalendar()

#get credentials from file
file_path = parrent_folder_path / "credentials.txt"
f = open(file_path, "r")

lines = f.readlines()
for line in lines:
    if 'calendar_releases ' in line:
        calendar_releases  = line.split()[1]
        print(calendar_releases)
    if 'team_calendar':
        team_calendar = line.split()[1]
        print(team_calendar)

def get_releases():
    
    events = gcalendar.get_this_week_releases()

    #Only send notification to HangoutsBot if events exits
    #@all tagging help:
    #https://developers.google.com/hangouts/chat/reference/message-formats/basic#messages_that_mention_specific_users
    if events != None:
        msg = "<users/all> *THIS WEEK RELEASES REMINDER*\n" + events + calendar_releases 
        HangoutsBot.instance.send_message("PythonToHangouts",msg)
        # HangoutsBot.instance.send_message("3D-Support-Room",msg)

def whos_on_the_phone():

    tagged_users = ''
    
    whos_on_the_phone = gcalendar.get_whos_on_the_phone_this_week()
    print(whos_on_the_phone)

    
    if "Ники" in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['nikolay.kusht'] + "\n"
        tagged_users += 'nikolay.kusht' + "\n"

    
    if "Диди" in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['diana.milenova'] + "\n"
        tagged_users += 'diana.milenova' + "\n"

    

    if "Ташко" in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['tashko.zashev'] + "\n"
        tagged_users += 'tashko.zashev' + "\n"

    

    if "Марти" in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['martin.minev'] + "\n"
        tagged_users += 'martin.minev' + "\n"

    

    if "Здравко" in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['zdravko.keremidchiev'] + "\n"
        tagged_users += 'zdravko.keremidchiev' + "\n"

    
    
    if "Виктор" in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['viktor.angelov'] + "\n"
        tagged_users += 'viktor.angelov' + "\n"

        

    if "Цвети" in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['tsvetomira.girginova'] + "\n"
        tagged_users += 'tsvetomira.girginova' + "\n"

    if "Влади" in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['vladimir.krastev'] + "\n"
        tagged_users += 'vladimir.krastev' + "\n"
    
    
    if "Алекс К." in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['aleksandar.kasabov'] + "\n"
        tagged_users += 'aleksandar.kasabov' + "\n"

    if "Алекс И." in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['aleksandar.ivanov'] + "\n"
        tagged_users += 'aleksandar.ivanov' + "\n"

    if "Захари" in whos_on_the_phone:
        # tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['zahari.ivanov'] + "\n"
        tagged_users += 'zahari.ivanov' + "\n"


    print(tagged_users)

    msg = "*WHOS ON THE PHONE THIS WEEK*\n" + tagged_users + team_calendar 
    HangoutsBot.instance.send_message("PythonToHangouts",msg)
    # HangoutsBot.instance.send_message("3D-Support-Room",msg)

    
# get_releases()
whos_on_the_phone()

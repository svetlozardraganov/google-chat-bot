import requests
from datetime import datetime
import xml.etree.ElementTree as ET

import HangoutsBot

import pathlib
parrent_folder_path = pathlib.Path(__file__).parent.resolve()

#tutorial
#https://documentation.bamboohr.com/reference#login-3

class BambooHR():

    def __init__(self):
        #get credentials from file
        file_path = parrent_folder_path / "credentials.txt"
        f = open(file_path, "r")

        lines = f.readlines()
        for line in lines:
            if 'bamboo_base_url' in line:
                 self.base_url = line.split()[1]
                 print(self.base_url)
            if 'bamboo_api_key' in line:
                self.api_key = line.split()[1]
                print(self.api_key)

        self.timeout = 60
        self.today = datetime.today().strftime('%Y-%m-%d')


    def get_time_off_types(self):
        #https://documentation.bamboohr.com/reference#get-time-off-types
        url = self.base_url + 'meta/time_off/types/'
        response = requests.get(url, timeout=self.timeout, auth=(self.api_key, ''))
        response.raise_for_status()
        print(response.text)


    def get_time_off_policies(self):
        #https://documentation.bamboohr.com/reference#get-time-off-policies
        url = self.base_url + 'meta/time_off/policies/'
        response = requests.get(url, timeout=self.timeout, auth=(self.api_key, ''))
        response.raise_for_status()
        print(response.text)


    def get_time_off_requests(self,time_off_type_arg , start='', end=''):
        output = ""
        
        #https://documentation.bamboohr.com/reference#time-off-get-time-off-requests-1
        url = self.base_url + 'time_off/requests/'
        if start == '':
            start = self.today
        if end == '':
            end = self.today
        querystring = {"start":start, "end":end}
        response = requests.get(url, timeout=self.timeout, auth=(self.api_key, ''), params=querystring)
        response.raise_for_status()
        
        xml_data = ET.fromstring(response.content)
        
        for request in xml_data.findall('request'):
            employee = request.find('employee')
            # print(employee.text)
            name = employee.text
            for time_off_type_item in request.findall('type'):
                # print(' |-->', time_off_type_item.text)
                time_off_type =  time_off_type_item.text

            if time_off_type_arg == "Work From Home":
                if time_off_type == "Work From Home":
                    output = output + name + "\n"
            else:
                if time_off_type != "Work From Home":
                    output = output + name + " | " + time_off_type + "\n"

        #print(response.text)

        return output


    def get_time_off_policies_for_employee(self, employee_id):
        #https://documentation.bamboohr.com/reference#time-off-list-time-off-policies-for-employee
        url = self.base_url + 'employees/{0}/time_off/policies'.format(employee_id)
        response = requests.get(url, timeout=self.timeout, auth=(self.api_key, ''))
        response.raise_for_status()
        print(response.text)


    def get_future_time_off_balances(self, employee_id):
        #https://documentation.bamboohr.com/reference#estimate-future-time-off-balances
        url = self.base_url + 'employees/{0}/time_off/calculator'.format(employee_id)
        response = requests.get(url, timeout=self.timeout, auth=(self.api_key, ''))
        response.raise_for_status()
        print(response.text)


    def get_whos_out(self):
        #https://documentation.bamboohr.com/reference#get-a-list-of-whos-out-1
        url = self.base_url + 'time_off/whos_out'
        response = requests.get(url, timeout=self.timeout, auth=(self.api_key, ''))
        response.raise_for_status()
        print(response.text)


bamboo = BambooHR()

whosOut_WorkFromHome = bamboo.get_time_off_requests("Work From Home")
whosOut_NonWorkFromHome = bamboo.get_time_off_requests("Other")


if whosOut_WorkFromHome or whosOut_NonWorkFromHome:

    calendar_url = "<https://chaosgroup.bamboohr.com/calendar|_bamboo-calendar_>"
    msg = "<users/all> "
    
    if whosOut_NonWorkFromHome:
        msg += "*WHO'S OUT TODAY*\n" + whosOut_NonWorkFromHome
    if whosOut_WorkFromHome:
        msg += "*WHO'S WORKING FROM HOME TODAY*\n" + whosOut_WorkFromHome
        
    msg += calendar_url
    HangoutsBot.instance.send_message("PythonToHangouts",msg)
    # HangoutsBot.instance.send_message("3D-Support-Room",msg)
else:
    msg = "<users/all> *UNBELIEVABLE - THE WHOLE TEAM IS IN THE OFFICE TODAY*"
    HangoutsBot.instance.send_message("PythonToHangouts",msg)
    # HangoutsBot.instance.send_message("3D-Support-Room",msg)



##bamboo.get_time_off_types()

#Forbidden URL
##bamboo.get_time_off_policies()

#Forbidden URL
##bamboo.get_time_off_policies_for_employee(70)

##bamboo.get_future_time_off_balances(70)
##bamboo.get_whos_out()


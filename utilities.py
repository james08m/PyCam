__author__ = 'J08M'
import datetime

def getTimeToMinutes():
    current_time = datetime.datetime.now().time()
    time_str = str(current_time.hour) + ":"
    if current_time.minute < 10:
        time_str += "0"
    time_str += str(current_time.minute)
    return time_str

def getTimeToSecondes():
    current_time = datetime.datetime.now().time()
    time_str = str(current_time.hour) + "h"
    if current_time.minute < 10:
        time_str += "0"
    time_str += str(current_time.minute) + "m"
    if current_time.second < 10:
        time_str += "0"
    time_str += str(current_time.second)
    return time_str




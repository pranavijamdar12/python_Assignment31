import os 
import schedule
import time
from datetime import datetime

path = input("Enter directory path:")

def ScanDirectory():
    files = 0
    folder = 0
    for item in os.listdir(path):
        fullpath = os.path.join(path,item)

        if os.path.isfile(fullpath):
            files += 1
        elif os.path.isdir(fullpath):
            folder += 1

    print("Directory:",path)
    print("File:",files)
    print("Subdirecttores:",folder)
    print("sacn time:",datetime.now())

schedule.every(1).minutes.do(ScanDirectory)

while True:
    schedule.run_pending()
    time.sleep(1)

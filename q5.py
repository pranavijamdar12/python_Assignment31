import os
import schedule
import time
from datetime import datetime

path = input("Enter directory path: ")

def CountFiles():
    count = 0

    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            count += 1

    f = open("DirectoryCountLog.txt", "a")
    f.write("Directory : " + path + "\n")
    f.write("Files : " + str(count) + "\n")
    f.write("Time : " + str(datetime.now()) + "\n")
    f.write("----------------------\n")
    f.close()

    print("Updated Successfully")

schedule.every(5).minutes.do(CountFiles)

while True:
    schedule.run_pending()
    time.sleep(1)



import schedule
import time

message = input("Enter your msg:")

def DisplayMessage(message):
    print(message)

schedule.every(5).seconds.do(DisplayMessage,message)

while True:
    schedule.run_pending()
    time.sleep(1)

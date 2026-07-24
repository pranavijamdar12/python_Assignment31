import schedule
import time

def Display():
    print("Jay Ganesh....")

interval = int(input("Enter interval in seconds: "))

schedule.every(interval).seconds.do(Display)

while True:
    schedule.run_pending()
    time.sleep(1)

import schedule
import time

def MondayMsg():
    print("Start your weekly goals")

def WednesdayMsg():
    print("Review your weekly progress")

def FridayMsg():
    print("Weekly work completed")

schedule.every().monday.at("09:00").do(MondayMsg)
schedule.every().wednesday.at("17:00").do(WednesdayMsg)
schedule.every().friday.at("18:00").do(FridayMsg)

while True:
    schedule.run_pending()
    time.sleep(1)

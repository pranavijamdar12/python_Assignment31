import schedule
import time 
from datetime import datetime

def CreateLog():
    name = datetime.now().strftime("MarvellousLog_%d_%m_%Y_%M_%S.txt")

    f = open(name,"w")
    f.write("Log File created suncessfullly.\n")
    f.write("Creation time:" + str(datetime.now()))
    f.close()

    print(name,"Created")

schedule.every(10).minutes.do(CreateLog)

while True:
        schedule.run_pending()
        time.sleep(1)

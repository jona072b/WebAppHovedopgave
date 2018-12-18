import datetime

class Absense:
    dateTime = ""
    State = ""
    


    def __init__(self, dateTime, State):
        self.dateTime = dateTime
        self.State = State
        self.fixFormat()

    def fixFormat(self):
        # 2018-10-01 | 10:00:00.000
        #print("Before Fix format = " + self.dateTime)
        dateTimeList = self.dateTime.split(" ")
        date = dateTimeList[0].split("-")
        #print ("Absense FixFormat: " + str(date))
        self.dateTime = datetime.datetime(int(date[0]),int(date[1]), int(date[2]))
        self.dateTime =  self.dateTime.strftime('%Y-%m-%d')
        
        

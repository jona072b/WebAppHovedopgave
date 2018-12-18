import datetime
class Weather:
    dateTime = ""
    temperature = ""
    description = ""
    
    def __init__(
        self,
        dateTime,
        temperature,
        description
    ):
        self.dateTime = dateTime
        self.temperature = temperature
        self.description = description
        self.fixFormat()

    def fixFormat(self):
        self.description = self.description.replace("\"","")
        self.dateTime = self.dateTime.replace("\"","")
        self.dateTime = self.dateTime.replace(".","-")
        dateTimeList = self.dateTime.split(" ")
        date = dateTimeList[0].split("-")
        self.dateTime = datetime.datetime(int(date[2]),int(date[1]), int(date[0]), int(dateTimeList[1].split(":")[0]),int(dateTimeList[1].split(":")[1]))
        self.dateTime =  self.dateTime.strftime('%Y-%m-%d %H:%M:%S')
        
        #YYYY-MM-DD hh:mm:ss
    

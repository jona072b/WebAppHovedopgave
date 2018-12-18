from Absense import Absense
from Weather import Weather
import csv, pyodbc,time
from azure.storage.blob import BlockBlobService, PublicAccess
import os
import SendToBlob

#print("hello")


def connectToDB():
    #Cannot connect to our DB due to not providing connection string for DB in public GIT
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};Server=tcp:SOMESERVER,SOMEPORT;Database=SOMEDB;Uid=USERNAME@SOMEDB;Pwd=PASSWORD;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    return cnxn


def sendAbsenseToDB(absenseDataList):
    cnxn = connectToDB()
    cursor = cnxn.cursor()
    

    count = 0
    for record in absenseDataList:
        if count != 0:
            absenseRecordList = record.split(";")
            absense = Absense(absenseRecordList[2],absenseRecordList[3])
            #Sending the row to the db
            cursor.execute('insert into dbo.AbsenseData(Date,State) values (?,?)', (absense.dateTime , int(absense.State)))
            cnxn.commit()
            count += 1
        else:
            count +=1
    
    cnxn.close()

def sendWeatherToDB(weatherDataList):
    cnxn = connectToDB()
    cursor = cnxn.cursor()

    count = 0
    for record in weatherDataList:
        weatherRecordList = record.split(";")
        if count > 7:
            if "06:50" in weatherRecordList[0]:
                weather = Weather(weatherRecordList[0],int(weatherRecordList[1].split(".")[0].replace("\"","")),weatherRecordList[8])
                cursor.execute('insert into dbo.WeatherData(DateTime,Temperature,Description) values (?,?,?)',(weather.dateTime,int(weather.temperature),weather.description))
                cnxn.commit()
            count += 1
        else:
            count += 1
    cnxn.close()

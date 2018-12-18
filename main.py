from flask import Flask, request
from flask_cors import CORS
import MainFromFiles
import json

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/newAbsense', methods=['POST'])
def newAbsense():
    #print("Absense data recieved")
    posted_file = request.get_json()
    #for updates in posted_file:
    update_list = posted_file['updates']
    data = update_list[0]["value"].split("\n")
    #print("absenseData = " + str(data))
    MainFromFiles.sendAbsenseToDB(data)
    #print("Value: " + data[0])
    #value = json.dumps(posted_file)
    #print("File from Angular: " + value)
    return '{"Response" : "File Tranfered"}' 

@app.route('/newWeather', methods=['POST'])
def newWeather():
    #print("Weather data recieved")
    posted_file = request.get_json()
    #for updates in posted_file:
    update_list = posted_file['updates']
    data = update_list[0]["value"].split("\n")
    #print("weatherData = " + str(data))
    MainFromFiles.sendWeatherToDB(data)
    #print("Value: " + data[0])
    #value = json.dumps(posted_file)
    #print("File from Angular: " + value)
    return '{"Response" : "File Tranfered"}' 

@app.route('/test', methods=['GET'])
def test():
    return '{"TEST" : "TEST Complete"}'

app.run()
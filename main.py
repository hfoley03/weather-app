from flask import Flask
from flask import request
import requests
import geopy 
from geopy.geocoders import Nominatim

app = Flask(__name__) #creat instance of Flask 

@app.route("/")      #python decorator wraps code below to url endpoint
def index():
    location = request.args.get("location", "") #fetch location inputted by user 
    if location:                                #if location has been inputtted
        coordinates = get_geocode(location)     #calls function to convert location name to coordinates 
        try:
            weather_results = None
            weather_results = get_data(coordinates) #calls function to get weather data for coordinates
            #extracting individual results from dict weather_results
            if weather_results:
                date = weather_results[0]['startTime'][0:10]
                cloudy = str(weather_results[0]['values']['cloudCover'])
                temp = str(round(weather_results[0]['values']['temperature']))
                wind = str(weather_results[0]['values']['windSpeed'])
                rain = str(weather_results[0]['values']['precipitationIntensity'])
            else:
                coordinates = "Location was not found"
                date = "0"
                cloudy = "0"
                temp = "0"
                wind = "0"
                rain = "0"
        except TypeError as error:
            print(error)
            pass
        return(
            """<h1>Weather Web Service</h1>
            <body style="background-color:pink;">
            """
            +"""<form action="" method="get">
                    Location : <input type="text" name="location">
                    <input type="submit" value="Find Weather">
                     </form>                    
                     """
            + "Coordinates: "
            + coordinates
            +"""<br>"""
            + "Date: " 
            + date
            +"""<br>"""
            + "Cloud Coverage(%): "
            + cloudy
            +"""<br>"""
            + "Temperature(C): "
            + temp
            +"""<br>"""
            + "Wind(km/h): "
            + wind
            +"""<br>"""
            +"Rain Intensity:   "
            + rain    
        )
        
    else:
        #no location entered
        return(
            """<h1>Weather Web Service</h1>
            <body style="background-color:pink;">"""
            +"""<form action="" method="get">
                    Location : <input type="text" name="location">
                    <input type="submit" value="Find Weather">
                     </form>"""   
        )
        


def get_geocode(location):
    #function returns geocode/coordinates for a location entered using Nominatim API
    try:
        locator = Nominatim(user_agent="myGeocoder")
        geocode_ = locator.geocode(location)  #gets gecode of location
        #formatting output 
        latititude_ = str(round(geocode_.latitude, 5))
        longititude_ = str(round(geocode_.longitude, 5))
        coordinates = latititude_ + ", " +longititude_
        return str(coordinates)
    except AttributeError as error:
        print(error)
        pass
    
        
def get_data(coordinates):
    #function returns a dict of the current weather at the coordinates inputted, 
    #using tommorrow.io timelines API
    try:
        url = "https://api.tomorrow.io/v4/timelines"
        querystring = {
        "location":coordinates,
        "fields":["temperature", "cloudCover","windSpeed","precipitationIntensity"],
        "units":"metric",
        "timesteps":"current",
        "apikey":"NpUxfI0QDMTdiIzhW9GxUIzXfUZhcd74"}
        response = requests.request("GET", url, params=querystring)    
        results = response.json()['data']['timelines'][0]['intervals'] #formats json into dict
        return results         
    except KeyError as error:
        print(error)
        pass

#Starts use of Flask's local development server, allows script to be tested locally 
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


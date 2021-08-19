# weather-app
Weather Conditions Web Service 
A web service that returns the current weather conditions for a user inputted location. 
The web service can be accessed online through this [link](https://weather-app-323116.appspot.com/ "Weather App").
The web service was written in python and is hosted on google cloud platform. 
Alternatively the web service can be hosted locally using venv and running main.py from the terminal.

The file test.py contains unit testing for main.py and the file
test_api.py contains the testing for the exposed http endoints of https://weather-app-323116.appspot.com

The web service uses Nominatim for translation of locations to geocodes and the tomorrow.io timelines api for returning weather data.

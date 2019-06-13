# Map International Space Station current position

import folium
import requests
import time
import webbrowser

# Defining the folder where the HTML file will be saved  
filefolder = '/home/marcos/Programación/Python/'

# Locating JSON file
ISS = 'http://api.open-notify.org/iss-now.json'


while True:
    
    # Requesting the file
    r = requests.get(ISS)
    
    # Having the file as a JSON object
    r = r.json()
    
    # Locating Latitude and Longitudeand printing on screen
    lat = r['iss_position']['latitude']
    long = r['iss_position']['longitude']
    print(r['iss_position'])
    
    # Creating a map
    folium_map = folium.Map(center=[lat, long], zoom_start = 15)
    
    # Creating a circle on the map
    folium.Circle(
        radius=10000,
        location=[lat, long],
        popup='International Space Station',
        color='crimson',
        fill=True,
    ).add_to(folium_map)
    
    # Saving the map to a HTML file to be read by a web browser
    folium_map.save('iss.html')
    webbrowser.open('file://'+filefolder+'iss.html', new = -1)

    # Using a delay of 5 seconds
    time.sleep(5)
import requests
import os
# from tkinter import *
from os.path import join, dirname
from tkinter import *
from dotenv import load_dotenv
# Replace with your OpenWeatherMap API key
API_KEY = os.getenv("API_KEY")

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEYS") 
def get_weather():
    city = entry.get()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Extracting required information
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    coord = data['coord']
    wind_speed = data['wind']['speed']
 

    # Updating the labels to display the information
    min_temp_label.config(text=f'Min Temp: {min_temp} K ❄️',bg="magenta")
    max_temp_label.config(text=f'Max Temp: {max_temp} K ☀',bg="orange")
    coord_label.config(text=f'Coordinates: {coord["lat"]}, {coord["lon"]} 🌐',bg="light blue")
    wind_speed_label.config(text=f'Wind Speed: {wind_speed} m/s 💨',bg="light blue")



root = Tk()
root.title("MyEasy Weather")
root.geometry("360x500")

entry_widget_text = "Enter City Name"

entry = StringVar()
City_name = Entry(root, width=30, textvariable=entry, justify="center")
City_name.insert(0, entry_widget_text)
City_name.pack()
City_name.place(x=20, y=130)

search_button = Button(root, width=10, text="Search", bg="yellow", command=get_weather)
search_button.place(x=20, y=160)

# Labels to display information
min_temp_label = Label(root, text="Min Temp: ")
min_temp_label.place(x=12, y=220)

max_temp_label = Label(root, text="Max Temp: ")
max_temp_label.place(x=150, y=200)

coord_label = Label(root, text="Coordinates: ")
coord_label.place(x=150, y=260)

wind_speed_label = Label(root, text="Wind Speed: ")
wind_speed_label.place(x=12, y=290)


root.mainloop()



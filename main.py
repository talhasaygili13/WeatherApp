import requests
import tkinter
from tkinter import *
from tkinter import messagebox
window = tkinter.Tk()
window.title('Weather App')
window.geometry('380x670')
bg = PhotoImage(file = "bg.png" )
canvas_bg = Canvas(window, width=650, height=700)
canvas_bg.pack(fill='both', expand=True)
canvas_bg.create_image(0, 0, image=bg, anchor='nw')
FONT = ('Haveltica', 18)

base_url = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = open('api_key.txt', 'r').read()

def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius

def get_weather(city):
    result = requests.get(base_url + 'appid=' + api_key + '&q=' + city)
    if result:
        json = result.json()
        temp_kelvin = json['main']['temp']
        temp_celcius = kelvin_to_celcius(temp_kelvin)
        feels_like = json['main']['feels_like']
        feels_like_celcius = kelvin_to_celcius(feels_like)
        humidty = json['main']['humidity']
        weatherMain = json['weather'][0]['main']
        weatherDesc = json['weather'][0]['description']
        tempC = f'{temp_celcius:.2f}'
        feelsLikeC = f'{feels_like_celcius:.2f}'
        canvas_bg.create_text(270, 80, text=tempC, font=FONT, tags=("weather",))
        canvas_bg.create_text(270, 120, text=feelsLikeC, font=FONT, tags=("weather",))
        canvas_bg.create_text(270, 160, text=humidty, font=FONT, tags=("weather",))
        canvas_bg.create_text(270, 200, text=weatherMain, font=FONT, tags=("weather",))
        canvas_bg.create_text(180, 300, text=weatherDesc, font=FONT, tags=("weather",))
    else:
        messagebox.showerror(title='Error', message='Cannot find city {}'.format(city))


def search():
    canvas_bg.delete('weather')
    city = city_text.get()
    weather = get_weather(city)



city_text = StringVar()
city_input = Entry(canvas_bg, textvariable=city_text)

canvas_bg.create_window(200, 450, window=city_input)
canvas_bg.create_text(100, 80, text='Temperature:', font=FONT)
canvas_bg.create_text(117, 120, text='Feels Like:', font=FONT)
canvas_bg.create_text(130, 160, text='Humidty:', font=FONT)
canvas_bg.create_text(130, 200, text='Weather:', font=FONT)
canvas_bg.create_text(180, 260, text='Weather Detail:', font=FONT)

submit = Button(text='Submit', font=FONT, command=search)
canvas_bg.create_window(200, 500, window=submit)

tkinter.mainloop()

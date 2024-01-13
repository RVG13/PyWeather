from tkinter import ttk
from tkinter import *
import tkinter.messagebox as mb
import requests as re


def get_weather():
    city = entry.get()
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+('&units=metric&lang=ru&appid'
                                                                    '=3a1f96ccacf94a95f92fd68982f63be7')
    response = re.get(url)
    weather_data = response.json()
    mb.showinfo('Погода в ' + city, weather_data['main']['temp'])


root = Tk()
root.title('Погода PyWeather')
root.iconbitmap(default="cloud.ico")
root.geometry('400x100+700+400')
root.minsize(500, 200)
root.maxsize(500, 500)

label = Label(root, text='Узнать погоду в своём городе', font=("Arial", 16), background="#FFCDD2", foreground="#B71C1C")
label.pack()
label = Label(root, text='Введите название города:', font=("Arial", 10), background="#FFCDD2", foreground="#B71C1C")
label.pack()

entry = ttk.Entry(root)
entry.pack(padx=12, pady=2)

button = Button(root, text='Получить погоду', background="#FFCDD2", foreground="#B71C1C", command=get_weather)
button.pack()

root.mainloop()

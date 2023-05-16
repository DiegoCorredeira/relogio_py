import tkinter as tk
from tkinter import ttk
import datetime
import requests
import json
def get_temperature(city):
    api_key = "ecd5fbb0fa903393a75e997e06e2e184"
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)
    data = json.loads(response.text)
    if "current" in data and "temperature" in data["current"]:
        temperature = data["current"]["temperature"]
        return (temperature)
    else:
        return None

def show_temperature():
    city = city_entry.get().capitalize()
    temperature = get_temperature(city)
    if temperature is not None:
        info_label.configure(text=f'Temperatura em {city}: {temperature}°C')
    else:
        info_label.configure(text=f"Temperatura em {city} não encontrada")



def update_clock():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.configure(text=current_time)
    clock_label.after(1000, update_clock)

def show_day_of_week():
    # pegar todos os dias da semana
    days_of_week = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]
    # pegar o dia da semana atual
    current_day = datetime.datetime.now().weekday()
    days_of_week = days_of_week[current_day]
    info_label.config(text=f"Dia da semana: {days_of_week}")

def show_date():
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")
    info_label.config(text=f"Data: {current_date}")


window = tk.Tk()
window.title = ("Relogio Digital")
window.configure(bg="black")


bg_color = "black"
fg_color = "white"

clock_style = ttk.Style()
clock_style.configure("clock.TLabel", font=("Arial", 72, "bold"), background=bg_color, foreground=fg_color)

clock_label = ttk.Label(window, style="clock.TLabel")
clock_label.configure(anchor=tk.CENTER)
clock_label.pack(padx=20, pady=20)

city_entry = ttk.Entry(window, font="Helvetica 16 bold")
city_entry.pack(padx=20, pady=20)
city_entry.insert(0, "Informe a cidade")
city_entry.bind("<FocusIn>", lambda args: city_entry.delete('0', 'end'))



temperature_button = ttk.Button(window, text="Temperatura", command=show_temperature)
temperature_button.pack(padx=20, pady=20)


info_label = ttk.Label(window, font="Helvetica 20 bold", background=bg_color, foreground=fg_color)
info_label.pack(padx=20, pady=10)


menu_bar = tk.Menu(window)
window.configure(menu=menu_bar)

options_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Opções", menu=options_menu)
options_menu.add_command(label="Data", command=show_date)
options_menu.add_command(label="Dia da Semana", command=show_day_of_week)


update_clock()

window.mainloop()
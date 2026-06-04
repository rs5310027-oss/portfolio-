import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your API key
API_KEY = "YOUR_API_KEY"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter city name")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        messagebox.showerror("Error", "City not found")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    result_label.config(
        text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nCondition: {condition}"
    )

# GUI Window
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x300")

title = tk.Label(root, text="Weather Forecast App", font=("Arial", 16))
title.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Search", command=get_weather)
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
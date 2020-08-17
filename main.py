import tkinter as tk
from tkinter import font
import requests

degree_sign = u"\N{DEGREE SIGN}"

def format_response(weather):
    try:
        name, code = weather["name"], weather["sys"]["country"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        final_str = f"City: {name}, {code}\nConditions: {desc}\nTemperature ({degree_sign}C): {temp}  "
    except:
        final_str = "There was a problem\nretrieving that information"

    return final_str
def get_weather(city):
    weather_key = "536e97816398ceb705c3fef5a5e262fd"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    weather = response.json()

    results["text"] = format_response((weather))


HEIGHT = 500
WIDTH = 600

# every tkinter has a root window
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# upper frame smaller one on top
frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Courier", 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=("Courier", 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# lower frame

lower_frame = tk.Frame(root, bg="#80c1ff", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

results = tk.Label(lower_frame, font=("Courier", 14), anchor="nw", justify="left", bd=4)
results.place(relwidth=1, relheight=1)

# every application goes in between the root.mainloop() and root = tl.Tk()
root.mainloop()

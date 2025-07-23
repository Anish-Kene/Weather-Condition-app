from tkinter import *
from tkinter import ttk
import requests

def Data_get():
    city = city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06b5805a4462eb2310ac9426b3a4908a").json()
    W_label1.config(text= data["weather"][0]["main"])
    Wb_label1.config(text= data["weather"][0]["description"])
    temp_label1.config(text= str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text= data["main"]["pressure"])




win = Tk()
win.title("Weather Condition")
win.config(bg = "dark grey")
win.geometry("500x550")

name_label= Label(win, text=" Weather Condition",
                  font=("Time New Roman", 30, "bold"))

name_label.place(x=25, y=50, height=50, width=450)


city_name = StringVar()
list_name= [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
com = ttk.Combobox(win, text="Weather Condition app", values= list_name,
                   font=("Rime New Roman",20,"bold"), textvariable=city_name  )

com.place(x=25, y=120, height=50, width=450)


#1
W_label= Label(win, text=" Weather Climate",
                  font=("Time New Roman", 17))

W_label.place(x=25, y=290, height=50, width=210)

W_label1= Label(win, text="  ",
                  font=("Time New Roman", 17))

W_label1.place(x=250, y=290, height=50, width=220)

#2
Wb_label= Label(win, text=" Weather Discription",
                  font=("Time New Roman", 17))

Wb_label.place(x=25, y=350, height=50, width=210)

Wb_label1= Label(win, text=" ",
                  font=("Time New Roman", 17))

Wb_label1.place(x=250, y=350, height=50, width=220)

#3
temp_label= Label(win, text="Temperature",
                  font=("Time New Roman", 17))

temp_label.place(x=25, y=410, height=50, width=210)

temp_label1= Label(win, text="",
                  font=("Time New Roman", 17))

temp_label1.place(x=250, y=410, height=50, width=220)

#4
per_label= Label(win, text="Pressure",
                  font=("Time New Roman", 17))

per_label.place(x=25, y=470, height=50, width=210)

per_label1= Label(win, text="",
                  font=("Time New Roman", 17))

per_label1.place(x=250, y=470, height=50, width=220)

#Button
done_button= Button(win, text="Done", 
                   font=("Rime New Roman",20,"bold"),command=Data_get  )

done_button.place(y= 190, height=50, width= 100, x= 200)


win.mainloop()
from PIL import ImageTk 
import PIL.Image
from tkinter import *
import tkinter as tk
import requests
import webbrowser
import io
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime, time, os
import requests,bs4
from urllib.request import urlopen

windo = Tk()
windo.configure(background='white')
windo.title("Covid Visualizer")

windo.geometry('1120x520')
windo.iconbitmap('')
windo.resizable(0, 0)

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-minimized')  # maximized
wd = webdriver.Chrome(r'C:\Users\Karthik Y\Downloads\chromedriver_win32\chromedriver.exe', options=CO)

def search():
    try:
        global im5, un
        un = str(txt2.get())
        wd.get("https://www.worldometers.info/coronavirus/country/"+un)
        wd.implicitly_wait(wait_imp)
        

        ## Fetch image in system
      
        img_url = str("https://www.sic-info.org/wp-content/uploads/2014/01/"+un[0:2]+".png")
        u = urlopen(img_url)
        raw_data = u.read()
        im5 = PIL.Image.open(io.BytesIO(raw_data))
        im5 = im5.resize((30, 30), PIL.Image.ANTIALIAS)


        ## Fetch Info
        c2 = wd.find_elements_by_class_name("maincounter-number")
        total = c2[0].text
        Death = c2[1].text
        Recovered = c2[2].text
        total1 = str(total)+" Total cases"
        Death1 = str(Death)+" Deaths"
        Recovered1 = str(Recovered)+" Recovered"
        total_label.config(text=total1)
        recovered_label.config(text=Recovered1)
        deaths_label.config(text=Death1)

        ## Show image
        image = ImageTk.PhotoImage(im5)
        panel5 = Button(windo,image = image, command = check_link,borderwidth=0)
        panel5.image = image
        panel5.pack()
        panel5.place(x=300, y=30)



    except Exception as e:
        print(e)
        lab1 = tk.Label(windo, text="Country namenot found!", width=20, height=1, fg="white", bg="firebrick1",
                        font=('times', 14, ' bold '))
        lab1.place(x=400, y=250)
        windo.after(4000, destroy_widget, lab1)

def check_link():
    link = 'https://www.worldometers.info/coronavirus/country/' + un
    webbrowser.open_new_tab(link)

def clear():
    txt2.delete(first=0,last=100)


#def download_dp():
    #im5.save(un+'.jpg')
    #lab1 = tk.Label(windo, text="Picture Downloaded!", width=20, height=1, fg="black", bg="gold",
                    #font=('times', 14, ' bold '))
   #lab1.place(x=400, y=250)
   # windo.after(4000, destroy_widget,lab1 )

def destroy_widget(widget):
    widget.destroy()

im = PIL.Image.open('./meta/Coronavirus.png')
im = im.resize((200, 200), PIL.Image.ANTIALIAS)
wp_img = ImageTk.PhotoImage(im)
panel4 = Label(windo, image=wp_img, bg='white')
panel4.pack()
panel4.place(x=50, y=70)

im1 = PIL.Image.open('./meta/angry1.jpg')
im1 = im1.resize((200, 200), PIL.Image.ANTIALIAS)
wp_img1 = ImageTk.PhotoImage(im1)
panel4 = Label(windo, image=wp_img1, bg='white')
panel4.pack()
panel4.place(x=885, y=90)

im1 = PIL.Image.open('./meta/search.png')
im1 = im1.resize((40, 40), PIL.Image.ANTIALIAS)
sp_img = ImageTk.PhotoImage(im1)
panel5 = Button(windo, borderwidth=0, image=sp_img,command=search, bg='white')
panel5.pack()
panel5.place(x=750, y=175)

im2 = PIL.Image.open('./meta/eraser.png')
im2 = im2.resize((40, 40), PIL.Image.ANTIALIAS)
assert isinstance(im2, object)
sp_img1 = ImageTk.PhotoImage(im2)
panel6 = Button(windo, borderwidth=0,command=clear, image=sp_img1, bg='white')
panel6.pack()
panel6.place(x=810, y=175)


pred = tk.Label(windo, text="Covid19 Visualiser", width=30, height=2, fg="white", bg="maroon2",
                font=('times', 25, ' bold '))
pred.place(x=274, y=10)

lab = tk.Label(windo, text="Enter Country name", width=18, height=1, fg="white", bg="blue2",
               font=('times', 16, ' bold '))
lab.place(x=394, y=120)

txt2 = tk.Entry(windo, borderwidth=7, width=26, bg="white", fg="black", font=('times', 25, ' bold '))
txt2.place(x=280, y=170)

total_label = tk.Label(windo, text='Total cases', width=17, height=2, fg="white", bg="maroon2",
                           font=('times', 18, ' bold '))
total_label.place(x=200, y=300)

recovered_label = tk.Label(windo, text="Recovered", width=17, height=2, fg="black", bg="spring green",
                           font=('times', 18, ' bold '))
recovered_label.place(x=470, y=300)

deaths_label = tk.Label(windo, text="Deaths", width=17, height=2, fg="white", bg="red",
                       font=('times', 18, ' bold '))
deaths_label.place(x=740, y=300)


windo.mainloop()

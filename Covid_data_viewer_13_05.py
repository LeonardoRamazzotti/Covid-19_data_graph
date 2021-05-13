#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:27:13 2021

@author: leonardo
"""
from PIL import ImageTk,Image
from datetime import datetime
import tkinter as  tk
import numpy as np
import pandas as pd

root= tk.Tk()
root.title('Covid-19 Data Analisys')
root.geometry('1920x1080')
root.configure(bg='#2A363B')

time=str(datetime.now())
time = time.replace('-','')
time = time.split(' ')

def regioni_graphic():
    
    my_img3 =Image.open('ricoverati_var'+time[0]+'.png')
    my_img3.show()
  
def province_graphic():
    
    my_img2 =Image.open('province_casi'+time[0]+'.png')
    my_img2.show()


frame_regioni= tk.Frame(root,bg ='#FF947C')
frame_regioni.place(height = 350, width = 600 , x=0, y=0)
frame_province= tk.Frame(root,bg ='#99B898')
frame_province.place(height = 205, width = 428 , x=615, y=0)


df = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv')
datiregioni = df[['denominazione_regione','ricoverati_con_sintomi','variazione_totale_positivi']].sort_values(by='ricoverati_con_sintomi', ascending = False)
ax = datiregioni.plot(kind="bar", x='denominazione_regione', figsize=(8,10))

fig1 = ax.get_figure()
fig1.savefig('ricoverati_var'+time[0]+'.png')

df_provincia = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province-latest.csv')
df_provincia= df_provincia.iloc[123:131]
datiprovince = df_provincia[['denominazione_provincia','totale_casi']]
bx=datiprovince.plot(kind="bar", x='denominazione_provincia', figsize=(8,8))

title_regioni = tk.Label(frame_regioni,text='REGIONI',fg ='#FF947C',bg='#2A363B',font=('Calibri',18) )
title_regioni.place(height = 48, width = 595 , x=0, y=0)
title_province = tk.Label(frame_province,text='PROVINCE TOSCANA',fg ='#99B898',bg='#2A363B',font=('Calibri',18) )
title_province.place(height = 50, width = 423 , x=0, y=0)

labelregioni = tk.Label(frame_regioni, text= datiregioni, fg='#FF947C',bg='#2A363B', font=('Calibri',10))
labelregioni.place(height = 305, width = 615 , x=-20, y=40)
labelprovince = tk.Label(frame_province, text= datiprovince, fg='#99B898',bg='#2A363B', font=('Calibri',12))
labelprovince.place(height = 150,width =423, x=0, y=50)

buttonregioni = tk.Button(frame_regioni,text ='Grafico',bg='#FF947C',fg ='#2A363B',width=100,height=50, command=regioni_graphic )
buttonregioni.place(height =30,width =60, x=20, y=10)
buttonprovince = tk.Button(frame_province,text ='Grafico',bg='#99B898',fg ='#2A363B',width=100,height=50 , command= province_graphic)
buttonprovince.place(height =30,width =60, x=20, y=10)


fig1 = ax.get_figure()
fig1.savefig('ricoverati_var'+time[0]+'.png')

fig2 = bx.get_figure()
fig2.savefig('province_casi'+time[0]+'.png')


root.mainloop()
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import csv
from keras.models import Sequential
from keras.layers import Dense
import bs4 as bs
import lxml
import urllib.request
import os

wlinks=['https://karki23.github.io/Weather-Data/Albury.html','https://karki23.github.io/Weather-Data/BadgerysCreek.html','https://karki23.github.io/Weather-Data/Cobar.html','https://karki23.github.io/Weather-Data/CoffsHarbour.html','https://karki23.github.io/Weather-Data/Moree.html','https://karki23.github.io/Weather-Data/Newcastle.html','https://karki23.github.io/Weather-Data/NorahHead.html','https://karki23.github.io/Weather-Data/NorfolkIsland.html','https://karki23.github.io/Weather-Data/Penrith.html','https://karki23.github.io/Weather-Data/Richmond.html','https://karki23.github.io/Weather-Data/Sydney.html','https://karki23.github.io/Weather-Data/SydneyAirport.html','https://karki23.github.io/Weather-Data/WaggaWagga.html','https://karki23.github.io/Weather-Data/Williamtown.html','https://karki23.github.io/Weather-Data/Wollongong.html','https://karki23.github.io/Weather-Data/Canberra.html','https://karki23.github.io/Weather-Data/Tuggeranong.html','https://karki23.github.io/Weather-Data/MountGinini.html','https://karki23.github.io/Weather-Data/Ballarat.html','https://karki23.github.io/Weather-Data/Bendigo.html','https://karki23.github.io/Weather-Data/Sale.html','https://karki23.github.io/Weather-Data/MelbourneAirport.html','https://karki23.github.io/Weather-Data/Melbourne.html','https://karki23.github.io/Weather-Data/Mildura.html','https://karki23.github.io/Weather-Data/Nhil.html','https://karki23.github.io/Weather-Data/Portland.html','https://karki23.github.io/Weather-Data/Watsonia.html','https://karki23.github.io/Weather-Data/Dartmoor.html','https://karki23.github.io/Weather-Data/Brisbane.html','https://karki23.github.io/Weather-Data/Cairns.html','https://karki23.github.io/Weather-Data/GoldCoast.html','https://karki23.github.io/Weather-Data/Townsville.html','https://karki23.github.io/Weather-Data/Adelaide.html','https://karki23.github.io/Weather-Data/MountGambier.html','https://karki23.github.io/Weather-Data/Nuriootpa.html','https://karki23.github.io/Weather-Data/Woomera.html','https://karki23.github.io/Weather-Data/Albany.html','https://karki23.github.io/Weather-Data/Witchcliffe.html','https://karki23.github.io/Weather-Data/PearceRAAF.html','https://karki23.github.io/Weather-Data/PerthAirport.html','https://karki23.github.io/Weather-Data/Perth.html','https://karki23.github.io/Weather-Data/SalmonGums.html','https://karki23.github.io/Weather-Data/Walpole.html','https://karki23.github.io/Weather-Data/Hobart.html','https://karki23.github.io/Weather-Data/Launceston.html','https://karki23.github.io/Weather-Data/AliceSprings.html','https://karki23.github.io/Weather-Data/Darwin.html','https://karki23.github.io/Weather-Data/Katherine.html','https://karki23.github.io/Weather-Data/Uluru.html']
wfiles=['albury','badgerys','cobar','coffs','moree','newcastle','norah','norfolk','penrith','richmond','sydney','sydair','wagga','william','wollongong','canberra','tuggeranong','ginini','ballarat','bendigo','sale','melair','melbourne','mildura','nhil','portland','watsonia','dartmoor','brisbane','cairns','goldcoast','townsville','adelaide','gambier','nuriootpa','woomera','albany','witchcliffe','pearceraaf','perthair','perth','salmon','walpole','hobart','launceston','alice','darwin','kath','uluru']

new_file=open('datasets\\complete_dataset.csv','w',newline='')
df=pd.read_csv('datasets\\albury.csv')
writer=csv.writer(new_file)
writer.writerow(list(df.keys()))
    
p=0
while p<=48:
    sauce=urllib.request.urlopen(wlinks[p]).read()
    srccode=bs.BeautifulSoup(sauce,'lxml')
    writer=csv.writer(new_file)
    tr=srccode.find_all('tr')
    tr.pop(0)
    for k in tr[1:]:
        td=k.find_all('td')
        row_data=[j.text for j in td]
        writer.writerow(row_data)
    p=p+1
new_file.close()

data=pd.read_csv("datasets\\complete_dataset.csv")
data=data.drop(columns=['Date', 'Location', 'RISK_MM'])

data['WindGustDir'] = pd.Categorical(data['WindGustDir'])
data['WindGustDir'] = data.WindGustDir.cat.codes
data['WindDir9am'] = pd.Categorical(data['WindDir9am'])
data['WindDir9am'] = data.WindDir9am.cat.codes
data['WindDir3pm'] = pd.Categorical(data['WindDir3pm'])                 
data['WindDir3pm'] = data.WindDir3pm.cat.codes
data['RainToday'] = pd.Categorical(data['RainToday'])
data['RainToday'] = data.RainToday.cat.codes
data['RainTomorrow'] = pd.Categorical(data['RainTomorrow'])
data['RainTomorrow'] = data.RainTomorrow.cat.codes

data[['WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow', 'Evaporation', 'Sunshine']] = data[['WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow', 'Evaporation', 'Sunshine']].astype(float)

for i in data.keys():
    data[i].fillna(data[i].mean(), inplace=True)
    
x_data=data.drop(columns=["RainTomorrow"])

y_data=data["RainTomorrow"]

x_train=x_data[1:int(0.8*len(x_data))]

y_train=y_data[1:int(0.8*len(y_data))]

x_test=x_data[int(0.8*len(x_data)):]

y_test=y_data[int(0.8*len(y_data)):]



x_train.shape[1]

model=Sequential()

n_cols = x_train.shape[1]

model.add(Dense(21, activation='sigmoid', input_shape=(n_cols,)))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)

test_loss, test_acc = model.evaluate(x_test, y_test)
print("\nTHE TEST ACCURACY IS : ", test_acc)




'''data[['WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow', 'Evaporation', 'Sunshine']] = data[['WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow', 'Evaporation', 'Sunshine']].astype(float)

for i in data.keys():
    data[i].fillna(data[i].mean(), inplace=True)


x_data=data.drop(columns=["RainTomorrow"])
y_data=data["RainTomorrow"]


x_train=x_data[1:int(0.8*len(x_data))]
y_train=y_data[1:int(0.8*len(y_data))]
x_test=x_data[int(0.8*len(x_data)):]
y_test=y_data[int(0.8*len(y_data)):]

n_cols = x_train.shape[1]

model=Sequential()
model.add(Dense(21, activation='sigmoid', input_shape=(n_cols,)))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x_train, y_train, epochs=30)

test_loss, test_acc = model.evaluate(x_test, y_test)
print("\nTHE TEST ACCURACY IS : ", test_acc)'''


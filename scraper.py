# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:01:13 2019

@author: swanuja
"""

import bs4 as bs
import lxml
import urllib.request
import csv
import os

os.mkdir("datasets")
wlinks=['https://karki23.github.io/Weather-Data/Albury.html','https://karki23.github.io/Weather-Data/BadgerysCreek.html','https://karki23.github.io/Weather-Data/Cobar.html','https://karki23.github.io/Weather-Data/CoffsHarbour.html','https://karki23.github.io/Weather-Data/Moree.html','https://karki23.github.io/Weather-Data/Newcastle.html','https://karki23.github.io/Weather-Data/NorahHead.html','https://karki23.github.io/Weather-Data/NorfolkIsland.html','https://karki23.github.io/Weather-Data/Penrith.html','https://karki23.github.io/Weather-Data/Richmond.html','https://karki23.github.io/Weather-Data/Sydney.html','https://karki23.github.io/Weather-Data/SydneyAirport.html','https://karki23.github.io/Weather-Data/WaggaWagga.html','https://karki23.github.io/Weather-Data/Williamtown.html','https://karki23.github.io/Weather-Data/Wollongong.html','https://karki23.github.io/Weather-Data/Canberra.html','https://karki23.github.io/Weather-Data/Tuggeranong.html','https://karki23.github.io/Weather-Data/MountGinini.html','https://karki23.github.io/Weather-Data/Ballarat.html','https://karki23.github.io/Weather-Data/Bendigo.html','https://karki23.github.io/Weather-Data/Sale.html','https://karki23.github.io/Weather-Data/MelbourneAirport.html','https://karki23.github.io/Weather-Data/Melbourne.html','https://karki23.github.io/Weather-Data/Mildura.html','https://karki23.github.io/Weather-Data/Nhil.html','https://karki23.github.io/Weather-Data/Portland.html','https://karki23.github.io/Weather-Data/Watsonia.html','https://karki23.github.io/Weather-Data/Dartmoor.html','https://karki23.github.io/Weather-Data/Brisbane.html','https://karki23.github.io/Weather-Data/Cairns.html','https://karki23.github.io/Weather-Data/GoldCoast.html','https://karki23.github.io/Weather-Data/Townsville.html','https://karki23.github.io/Weather-Data/Adelaide.html','https://karki23.github.io/Weather-Data/MountGambier.html','https://karki23.github.io/Weather-Data/Nuriootpa.html','https://karki23.github.io/Weather-Data/Woomera.html','https://karki23.github.io/Weather-Data/Albany.html','https://karki23.github.io/Weather-Data/Witchcliffe.html','https://karki23.github.io/Weather-Data/PearceRAAF.html','https://karki23.github.io/Weather-Data/PerthAirport.html','https://karki23.github.io/Weather-Data/Perth.html','https://karki23.github.io/Weather-Data/SalmonGums.html','https://karki23.github.io/Weather-Data/Walpole.html','https://karki23.github.io/Weather-Data/Hobart.html','https://karki23.github.io/Weather-Data/Launceston.html','https://karki23.github.io/Weather-Data/AliceSprings.html','https://karki23.github.io/Weather-Data/Darwin.html','https://karki23.github.io/Weather-Data/Katherine.html','https://karki23.github.io/Weather-Data/Uluru.html']
wfiles=['albury','badgerys','cobar','coffs','moree','newcastle','norah','norfolk','penrith','richmond','sydney','sydair','wagga','william','wollongong','canberra','tuggeranong','ginini','ballarat','bendigo','sale','melair','melbourne','mildura','nhil','portland','watsonia','dartmoor','brisbane','cairns','goldcoast','townsville','adelaide','gambier','nuriootpa','woomera','albany','witchcliffe','pearceraaf','perthair','perth','salmon','walpole','hobart','launceston','alice','darwin','kath','uluru']
  
p=0
for i in wfiles:
    i=open('datasets\\'+i+'.csv','w',newline='')
    sauce=urllib.request.urlopen(wlinks[p]).read()
    srccode=bs.BeautifulSoup(sauce,'lxml')
    writer=csv.writer(i)
    tr=srccode.find_all('tr')
    tr.pop(0)
    headings=srccode.find_all('th')
    headings_new=[i.text for i in headings]
    writer=csv.writer(i)
    writer.writerow(headings_new)
    for k in tr:
        td=k.find_all('td')
        row_data=[j.text for j in td]
        writer.writerow(row_data)
    i.close()
    p=p+1
        
        
    


import os		
import sys
import pandas as pd
import sqlite3
import numpy as np

cnx = sqlite3.connect('triggered.db')

heasarc = pd.read_sql_query("SELECT * FROM heasarc_data", cnx)
heasarc["trigger_time"]= pd.to_numeric( heasarc["trigger_time"],errors='ignore')
heasarc=heasarc.sort_values(by='trigger_time')
heasarc=heasarc.reset_index(drop=True)
heasarc.insert(0, 'mode1', 0)
heasarc.insert(0, 'mode2', 0)
heasarc.insert(0, 'mode3', 0)
heasarc.insert(0, 'mode4', 0)
hea_trig= heasarc["trigger_time"]


### MODE 1

mode1= pd.read_sql_query("SELECT * FROM Mode1", cnx)
mode1["time_met"]=pd.to_numeric(mode1["time_met"],errors='ignore')
mode1=mode1.sort_values(by='time_met')
mode1=mode1.reset_index(drop = True)
mode1.insert(0, 'mode1', 1)
mode1_trig=mode1["time_met"]


#initializing for mode 1
for i in range(len(hea_trig)):
    if hea_trig.at[i]>(mode1_trig.at[0]) and  hea_trig.at[i]<(mode1_trig.at[len(mode1_trig)-1]) :
        heasarc.at[i,'mode1']=1

##searching algo.
a=0
i=0
j=0
while i<len(hea_trig)-1 and j<len(mode1_trig)-1 :
    if hea_trig.at[i]>=(mode1_trig.at[j]-0.5):
        if hea_trig.at[i]<=(mode1_trig.at[j]+0.5):
            heasarc.at[i,'mode1']=2
            explored.at[j,'mode1']=2
            j+=1
            if i>0:
                i-=1
        else:
            j+=1
            if i>0:
                i-=1
    else:
        i+=1

print("MODE1: "+str(a))


### MODE 2

mode2= pd.read_sql_query("SELECT * FROM Mode2", cnx)
mode2["time_met"]=pd.to_numeric(mode2["time_met"],errors='ignore')
mode2=mode2.sort_values(by='time_met')
mode2=mode2.reset_index(drop = True)
mode2.insert(0, 'mode2', 1)
mode2_trig=mode2["time_met"]


#initializing for mode2
for i in range(len(hea_trig)):
    if hea_trig.at[i]>(mode2_trig.at[0]) and  hea_trig.at[i]<(mode2_trig.at[len(mode2_trig)-1]) :
        heasarc.at[i,'mode2']=1

##searching algo.
a=0
i=0
j=0
while i<len(hea_trig)-1 and j<len(mode2_trig)-1 :
    if hea_trig.at[i]>=(mode2_trig.at[j]-0.5):
        if hea_trig.at[i]<=(mode2_trig.at[j]+0.5):
            heasarc.at[i,'mode2']=2
            explored.at[j,'mode2']=2
            j+=1
            if i>0:
                i-=1
        else:
            j+=1
            if i>0:
                i-=1
    else:
        i+=1
print("MODE2: "+str(a))


### MODE 3

mode3= pd.read_sql_query("SELECT * FROM Mode3", cnx)
mode3["time_met"]=pd.to_numeric(mode3["time_met"],errors='ignore')
mode3=mode3.sort_values(by='time_met')
mode3=mode3.reset_index(drop = True)
mode3.insert(0, 'mode3', 1)
mode3_trig=mode3["time_met"]


#initializing for mode3
for i in range(len(hea_trig)):
    if hea_trig.at[i]>(mode3_trig.at[0]) and  hea_trig.at[i]<(mode3_trig.at[len(mode3_trig)-1]) :
        heasarc.at[i,'mode3']=1

##searching algo.
a=0
i=0
j=0
while i<len(hea_trig)-1 and j<len(mode3_trig)-1 :
    if hea_trig.at[i]>=(mode3_trig.at[j]-0.5):
        if hea_trig.at[i]<=(mode3_trig.at[j]+0.5):
            heasarc.at[i,'mode3']=2
            explored.at[j,'mode3']=2
            j+=1
            if i>0:
                i-=1
        else:
            j+=1
            if i>0:
                i-=1
    else:
        i+=1
print("MODE3: "+str(a))
### MODE 4

mode4= pd.read_sql_query("SELECT * FROM Mode4", cnx)
mode4["time_met"]=pd.to_numeric(mode4["time_met"],errors='ignore')
mode4=mode4.sort_values(by='time_met')
mode4=mode4.reset_index(drop = True)
mode4.insert(0, 'mode4', 1)
mode4_trig=mode4["time_met"]


#initializing for mode4
for i in range(len(hea_trig)):
    if hea_trig.at[i]>(mode4_trig.at[0]) and  hea_trig.at[i]<(mode4_trig.at[len(mode4_trig)-1]) :
        heasarc.at[i,'mode4']=1

##searching algo.
a=0
i=0
j=0
while i<len(hea_trig)-1 and j<len(mode4_trig)-1 :
    if hea_trig.at[i]>=(mode4_trig.at[j]-0.5):
        if hea_trig.at[i]<=(mode4_trig.at[j]+0.5):
            heasarc.at[i,'mode4']=2
            explored.at[j,'mode4']=2
            a+=1
            j+=1
            if i>0:
                i-=1
        else:
            j+=1
            if i>0:
                i-=1
    else:
        i+=1

print("MODE4: "+str(a))





heasarc.to_sql('heasarc_data', cnx, if_exists='replace', index = False)
explored.to_sql('explored_data', cnx, if_exists='replace', index = False)







#f.close()
cnx.commit()
cnx.close()

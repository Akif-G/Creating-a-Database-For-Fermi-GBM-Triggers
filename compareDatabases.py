import os		
import sys
import pandas as pd
import sqlite3
import numpy as np

cnx = sqlite3.connect('triggered.db')

heasarc = pd.read_sql_query("SELECT * FROM heasarc_data", cnx)
heasarc["trigger_time"]= pd.to_numeric( heasarc["trigger_time"],errors='ignore')

try:
    heasarc.insert(0, 'mode1', 0)
    heasarc.insert(0, 'mode2', 0)
    heasarc.insert(0, 'mode3', 0)
    heasarc.insert(0, 'mode4', 0)
except:
    heasarc.drop(['mode1','mode2','mode3','mode4',],axis=1,inplace=True)
    
    heasarc.insert(0, 'mode1', 0)
    heasarc.insert(0, 'mode2', 0)
    heasarc.insert(0, 'mode3', 0)
    heasarc.insert(0, 'mode4', 0)
    
heasarc=heasarc.sort_values(by='trigger_time')
heasarc=heasarc.reset_index(drop=True)
hea_trig= heasarc["trigger_time"]


### MODE 1

mode1= pd.read_sql_query("SELECT * FROM Mode1", cnx)
mode1["time_met"]=pd.to_numeric(mode1["time_met"],errors='ignore')

try:
    mode1.insert(0, 'nearest', 0)
    mode1.insert(0, 'nearest_name', "")    
    mode1.insert(0, 'mode1', 1)
except:
    mode1.drop(['nearest','nearest_name','mode1'],axis=1,inplace=True)
    mode1.insert(0, 'nearest', "")
    mode1.insert(0, 'mode1', 1)

mode1=mode1.sort_values(by='time_met')
mode1=mode1.reset_index(drop = True)
mode1_trig=mode1["time_met"]

#initializing for mode 1
if len(mode1_trig)!=0:
    for i in range(len(hea_trig)):
        if hea_trig.at[i]>(mode1_trig.at[0]) and  hea_trig.at[i]<(mode1_trig.at[len(mode1_trig)-1]) :
            heasarc.at[i,'mode1']=1

    ##searching algo.
    a=0
    i=0
    j=0
    while i<len(hea_trig)-1 and j<len(mode1_trig)-1 :
        if hea_trig.at[i]>=(mode1_trig.at[j]-0.5):
            if  i>0:
                if abs(hea_trig.at[i]-mode1_trig.at[j]) < abs(hea_trig.at[i-1]-mode1_trig.at[j]):
                    mode1.at[j,'nearest']=abs(hea_trig.at[i]-mode1_trig.at[j])
                    mode1.at[j,'nearest_name']=str(heasarc.at[i,'trigger_name'])
                else:
                    mode1.at[j,'nearest']=abs(hea_trig.at[i-1]-mode1_trig.at[j])
                    mode1.at[j,'nearest_name']=str(heasarc.at[i-1,'trigger_name'])
            if hea_trig.at[i]<=(mode1_trig.at[j]+0.5):
                heasarc.at[i,'mode1']=2
                mode1.at[j,'mode1']=2
                j+=1
                a+=1
                if i>0:
                    i-=1
            else:
                j+=1
                if i>0:
                    i-=1
        else:
            i+=1

    print("MODE1: "+str(a))
else:
    print("MODE1: not exist.")

### MODE 2

mode2= pd.read_sql_query("SELECT * FROM Mode2", cnx)
mode2["time_met"]=pd.to_numeric(mode2["time_met"],errors='ignore')

try:
    mode2.insert(0, 'nearest', 0)
    mode2.insert(0, 'nearest_name', "")    
    mode2.insert(0, 'mode2', 1)
except:
    mode2.drop(['nearest','nearest_name','mode2'],axis=1,inplace=True)
    mode2.insert(0, 'nearest', "")
    mode2.insert(0, 'mode2', 1)

mode2=mode2.sort_values(by='time_met')
mode2=mode2.reset_index(drop = True)
mode2_trig=mode2["time_met"]

#initializing for mode2
if len(mode2_trig)!=0:
    for i in range(len(hea_trig)):
        if hea_trig.at[i]>(mode2_trig.at[0]) and  hea_trig.at[i]<(mode2_trig.at[len(mode2_trig)-1]) :
            heasarc.at[i,'mode2']=1

    ##searching algo.
    a=0
    i=0
    j=0
    while i<len(hea_trig)-1 and j<len(mode2_trig)-1 :
        if hea_trig.at[i]>=(mode2_trig.at[j]-0.5):
            if  i>0:
                if abs(hea_trig.at[i]-mode2_trig.at[j]) < abs(hea_trig.at[i-1]-mode2_trig.at[j]):
                    mode2.at[j,'nearest']=abs(hea_trig.at[i]-mode2_trig.at[j])
                    mode2.at[j,'nearest_name']=str(heasarc.at[i,'trigger_name'])
                else:
                    mode2.at[j,'nearest']=abs(hea_trig.at[i-1]-mode2_trig.at[j])
                    mode2.at[j,'nearest_name']=str(heasarc.at[i-1,'trigger_name'])
                    
            if hea_trig.at[i]<=(mode2_trig.at[j]+0.5):
                heasarc.at[i,'mode2']=2
                mode2.at[j,'mode2']=2
                j+=1
                a+=1
                if i>0:
                    i-=1
            else:
                j+=1
                if i>0:
                    i-=1
        else:
            i+=1
    print("MODE2: "+str(a))
else:
    print("MODE2: not exist.")

### MODE 3

mode3= pd.read_sql_query("SELECT * FROM Mode3", cnx)
mode3["time_met"]=pd.to_numeric(mode3["time_met"],errors='ignore')

try:
    mode3.insert(0, 'nearest', 0)
    mode3.insert(0, 'nearest_name', "")
    mode3.insert(0, 'mode3', 1)
except:
    mode3.drop(['nearest','nearest_name','mode3'],axis=1,inplace=True)
    mode3.insert(0, 'nearest', "")
    mode3.insert(0, 'mode3', 1)

mode3=mode3.sort_values(by='time_met')
mode3=mode3.reset_index(drop = True)
mode3_trig=mode3["time_met"]

#initializing for mode3
if len(mode3_trig)!=0:
    for i in range(len(hea_trig)):
        if hea_trig.at[i]>(mode3_trig.at[0]) and  hea_trig.at[i]<(mode3_trig.at[len(mode3_trig)-1]) :
            heasarc.at[i,'mode3']=1

    ##searching algo.
    a=0
    i=0
    j=0
    while i<len(hea_trig)-1 and j<len(mode3_trig)-1 :
        if hea_trig.at[i]>=(mode3_trig.at[j]-0.5):
            if  i>0:
                if abs(hea_trig.at[i]-mode3_trig.at[j]) < abs(hea_trig.at[i-1]-mode3_trig.at[j]):
                    mode3.at[j,'nearest']=abs(hea_trig.at[i]-mode3_trig.at[j])
                    mode3.at[j,'nearest_name']=str(heasarc.at[i,'trigger_name'])
                else:
                    mode3.at[j,'nearest']=abs(hea_trig.at[i-1]-mode3_trig.at[j])
                    mode3.at[j,'nearest_name']=str(heasarc.at[i-1,'trigger_name'])
                    
            if hea_trig.at[i]<=(mode3_trig.at[j]+0.5):
                heasarc.at[i,'mode3']=2
                mode3.at[j,'mode3']=2
                j+=1
                a=+1
                if i>0:
                    i-=1
            else:
                j+=1
                if i>0:
                    i-=1
        else:
            i+=1
    print("MODE3: "+str(a))
else:
    print("MODE3: not exist.")

### MODE 4

mode4= pd.read_sql_query("SELECT * FROM Mode4", cnx)
mode4["time_met"]=pd.to_numeric(mode4["time_met"],errors='ignore')

try:
    mode4.insert(0, 'nearest', 0)
    mode4.insert(0, 'nearest_name', "")
    mode4.insert(0, 'mode4', 1)
except:
    mode4.drop(['nearest','nearest_name','mode4'],axis=1,inplace=True)
    mode4.insert(0, 'nearest', "")
    mode4.insert(0, 'mode4', 1)
    
mode4=mode4.sort_values(by='time_met')
mode4=mode4.reset_index(drop = True)
mode4_trig=mode4["time_met"]

#initializing for mode4
if len(mode4_trig)!=0:
    for i in range(len(hea_trig)):
        if hea_trig.at[i]>(mode4_trig.at[0]) and  hea_trig.at[i]<(mode4_trig.at[len(mode4_trig)-1]) :
            heasarc.at[i,'mode4']=1

    ##searching algo.
    a=0
    i=0
    j=0
    while i<len(hea_trig)-1 and j<len(mode4_trig)-1 :
        if hea_trig.at[i]>=(mode4_trig.at[j]-0.5):
            if  i>0:
                if abs(hea_trig.at[i]-mode4_trig.at[j]) < abs(hea_trig.at[i-1]-mode4_trig.at[j]):
                    mode4.at[j,'nearest']=abs(hea_trig.at[i]-mode4_trig.at[j])
                    mode4.at[j,'nearest_name']=str(heasarc.at[i,'trigger_name'])
                else:
                    mode4.at[j,'nearest']=abs(hea_trig.at[i-1]-mode4_trig.at[j])
                    mode4.at[j,'nearest_name']=str(heasarc.at[i-1,'trigger_name'])
                    
            if hea_trig.at[i]<=(mode4_trig.at[j]+0.5):
                heasarc.at[i,'mode4']=2
                mode4.at[j,'mode4']=2
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
else:
    print("MODE4: not exist.")


##FINAL COMPARISON THROUGH THE 4 COLUMN WE CREATED TO SEE IF ALL OF THEM ARE INCLUDED IN ONE OF ANY
#  
try:
    heasarc.insert(0, 'existence', 0)
except:
    heasarc.drop('existence',axis=1,inplace=True)
    heasarc.insert(0, 'existence', 0)

for i in range(len(hea_trig)):
    if ( heasarc.at[i,'mode1']==1 or heasarc.at[i,'mode2']==1 or heasarc.at[i,'mode3']==1 or heasarc.at[i,'mode4']==1 ):
        heasarc.at[i, 'existence']=1
    if heasarc.at[i,'mode4']==2:
        heasarc.at[i, 'existence']=2    
    elif heasarc.at[i,'mode2']==2:
        heasarc.at[i, 'existence']=2  
    elif heasarc.at[i,'mode3']==2:
        heasarc.at[i, 'existence']=2  
    elif heasarc.at[i,'mode1']==2:
        heasarc.at[i, 'existence']=2  

print("data is completely investigated")

heasarc.to_sql('heasarc_data', cnx, if_exists='replace', index = False)
mode1.to_sql('Mode1', cnx, if_exists='replace', index = False)
mode2.to_sql('Mode2', cnx, if_exists='replace', index = False)
mode3.to_sql('Mode3', cnx, if_exists='replace', index = False)
mode4.to_sql('Mode4', cnx, if_exists='replace', index = False)


cnx.commit()
cnx.close()

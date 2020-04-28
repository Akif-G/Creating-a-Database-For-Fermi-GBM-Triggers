import os		
import sys
import pandas as pd
import sqlite3
import numpy as np

cnx = sqlite3.connect('triggered.db')
test=sqlite3.connect('test.db')

heasarc = pd.read_sql_query("SELECT * FROM heasarc_data", cnx)
hea_trig=heasarc["trigger_time"]

mode1=pd.read_sql_query("SELECT * FROM mode1", cnx)
mode2=pd.read_sql_query("SELECT * FROM mode2", cnx)
mode3=pd.read_sql_query("SELECT * FROM mode3", cnx)
mode4=pd.read_sql_query("SELECT * FROM mode4", cnx)

cnx.close()

mode1_trig=mode1["time_met"]
mode2_trig=mode2["time_met"]
mode3_trig=mode3["time_met"]
mode4_trig=mode4["time_met"]

heasarc["mode1"].values[:] = 0
mode1["mode1"].values[:] = 0
mode2["mode2"].values[:] = 0
mode3["mode3"].values[:] = 0
mode4["mode4"].values[:] = 0
print("remaining iterations count:")
print(str(len(hea_trig)*(len(mode1_trig)+len(mode2_trig)+len(mode3_trig)+len(mode4_trig))-len(hea_trig)*(0)-87466068))
for i in range(len(hea_trig)):
    for j in range(len(mode1)):
        if hea_trig[i]<=(mode1_trig.values[j]+0.5) and hea_trig[i]>=(mode1_trig.values[j]-0.5):
            heasarc["mode1"][i]=2
            mode1["mode1"][j]=2
    for k in range(len(mode2)):
        if hea_trig[i]<=(mode2_trig.values[k]+0.5) and hea_trig[i]>=(mode2_trig.values[k]-0.5):
            heasarc["mode2"][i]=2
            mode2["mode2"][k]=2
    for m in range(len(mode3)):
        if hea_trig[i]<=(mode3_trig.values[m]+0.5) and hea_trig[i]>=(mode3_trig.values[m]-0.5):
            heasarc["mode3"][i]=2
            mode3["mode3"][m]=2
    for n in range(len(mode4)):
        if hea_trig[i]<=(mode4_trig.values[n]+0.5) and hea_trig[i]>=(mode4_trig.values[n]-0.5):
            heasarc["mode4"][i]=2
            mode4["mode4"][n]=2
    #printing countdown
    print(str(len(hea_trig)*(len(mode1_trig)+len(mode2_trig)+len(mode3_trig)+len(mode4_trig))-len(hea_trig)*(i+1)-87466068))

heasarc.to_sql('heasarc_data', test, if_exists='replace', index = False)
mode1.to_sql('Mode1', test, if_exists='replace', index = False)
mode2.to_sql('Mode2', test, if_exists='replace', index = False)
mode3.to_sql('Mode3', test, if_exists='replace', index = False)
mode4.to_sql('Mode4', test, if_exists='replace', index = False)


test.commit()
test.close()

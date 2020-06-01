import os		
import sys
import pandas as pd
import sqlite3
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

"""
very slow cross-validation test algorithm:
-> checks every input regardless of their time value unlike the comperasion algorithm.
-> checking from (HEASARC) to (MODE)
-> a lot of iteraitons...
-> more secure (literally compares everything...
"""
#OPEN
cnx = sqlite3.connect('triggered.db')
#output:
test=sqlite3.connect('test.db')

heasarc = pd.read_sql_query("SELECT * FROM heasarc_data", cnx)
hea_trig=heasarc["trigger_time"]

#SELECT FOR THE COMPERASION
mode1=pd.read_sql_query("SELECT * FROM mode1", cnx)
mode2=pd.read_sql_query("SELECT * FROM mode2", cnx)
mode3=pd.read_sql_query("SELECT * FROM mode3", cnx)
mode4=pd.read_sql_query("SELECT * FROM mode4", cnx)

#CLOSE THE ORIGINAL W/O CHANGING ANYTHING
cnx.close()

#seperated: will use for comperasion
mode1_trig=mode1["time_met"]
mode2_trig=mode2["time_met"]
mode3_trig=mode3["time_met"]
mode4_trig=mode4["time_met"]

#values converted to 0 again
heasarc["mode1"].values[:] = 0
heasarc["mode2"].values[:] = 0
heasarc["mode3"].values[:] = 0
heasarc["mode4"].values[:] = 0
mode1["heasarc"].values[:] = 0
mode2["heasarc"].values[:] = 0
mode3["heasarc"].values[:] = 0
mode4["heasarc"].values[:] = 0

#value changed 2 if any overlapping (+-0.5 second) happened.
print("remaining iterations count:")
print(str((len(hea_trig)*(len(mode1_trig)+len(mode2_trig)+len(mode3_trig)+len(mode4_trig)))/pow(10,4)))
for i in range(len(hea_trig)):
    for j in range(len(mode1)):
        if hea_trig[i]<=(mode1_trig.values[j]+0.5) and hea_trig[i]>=(mode1_trig.values[j]-0.5):
            heasarc["mode1"][i]=2
            mode1["heasarc"][j]=2
    for k in range(len(mode2)):
        if hea_trig[i]<=(mode2_trig.values[k]+0.5) and hea_trig[i]>=(mode2_trig.values[k]-0.5):
            heasarc["mode2"][i]=2
            mode2["heasarc"][k]=2
    for m in range(len(mode3)):
        if hea_trig[i]<=(mode3_trig.values[m]+0.5) and hea_trig[i]>=(mode3_trig.values[m]-0.5):
            heasarc["mode3"][i]=2
            mode3["heasarc"][m]=2
    for n in range(len(mode4)):
        if hea_trig[i]<=(mode4_trig.values[n]+0.5) and hea_trig[i]>=(mode4_trig.values[n]-0.5):
            heasarc["mode4"][i]=2
            mode4["heasarc"][n]=2
    #printing countdown
    print(str((len(hea_trig)*(len(mode1_trig)+len(mode2_trig)+len(mode3_trig)+len(mode4_trig))-(i*(len(mode1_trig)+len(mode2_trig)+len(mode3_trig)+len(mode4_trig))))/pow(10,4)))

#commit changes to uotput database: test.db
heasarc.to_sql('heasarc_data', test, if_exists='replace', index = False)
mode1.to_sql('Mode1', test, if_exists='replace', index = False)
mode2.to_sql('Mode2', test, if_exists='replace', index = False)
mode3.to_sql('Mode3', test, if_exists='replace', index = False)
mode4.to_sql('Mode4', test, if_exists='replace', index = False)


test.commit()
test.close()

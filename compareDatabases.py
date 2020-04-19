import os		
import sys
import pandas as pd
import sqlite3
import numpy as np

cnx = sqlite3.connect('triggered.db')


heasarc = pd.read_sql_query("SELECT * FROM heasarc_data", cnx)

explored= pd.read_sql_query("SELECT * FROM explored_data", cnx)


heasarc["trigger_time"]= heasarc["trigger_time"].astype(float)

explored["time_met"]=explored["time_met"].astype(float)

heasarc.sort_index(inplace=True)
explored.sort_index(inplace=True)



hea_trig= heasarc["trigger_time"].astype(float)

exp_trig=explored["time_met"].astype(float)



heasarc.insert(0, 'EXIST', 0)
explored.insert(0, 'EXIST', 0)
print(type(hea_trig))
for i in range(len(hea_trig)):
    for j in range(len(exp_trig)):
        if hea_trig.at[i]<(exp_trig.at[j]+0.5) and hea_trig.at[i]>(exp_trig.at[j]-0.5):
            heasarc["EXIST"][i]=1
            explored["EXIST"][j]=1
            print(1)


heasarc.to_sql('heasarc_data', cnx, if_exists='replace', index = False)
explored.to_sql('explored_data', cnx, if_exists='replace', index = False)

cnx.commit()
cnx.close()
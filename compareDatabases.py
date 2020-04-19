import os		
import sys
import pandas as pd
import sqlite3
import numpy as np

cnx = sqlite3.connect('triggered.db')


heasarc = pd.read_sql_query("SELECT * FROM heasarc_data", cnx)
explored= pd.read_sql_query("SELECT * FROM explored_data", cnx)


heasarc["trigger_time"]= pd.to_numeric( heasarc["trigger_time"], downcast="float")
explored["time_met"]=pd.to_numeric(explored["time_met"],  downcast="float")
print(type(heasarc.iat[1,3]))

heasarc=heasarc.sort_values(by='trigger_time')
explored=explored.sort_values(by='time_met')

heasarc=heasarc.reset_index(drop=True)
explored=explored.reset_index(drop = True)


heasarc.insert(0, 'EXISTENCE', 0)
explored.insert(0, 'EXISTENCE', 1)


hea_trig= heasarc["trigger_time"]
exp_trig=explored["time_met"]



##searching algo.
#initializing
i=0
j=0
count=0

while i<len(hea_trig)-1 and j<len(exp_trig)-1 :   
    if hea_trig.at[i]>=(exp_trig.at[j]-0.5):
        if hea_trig.at[i]<=(exp_trig.at[j]+0.5):
            heasarc.at[i,'EXISTENCE']=2
            explored.at[j,'EXISTENCE']=2
            j+=1
            if i>0:
                i-=1
        else:
            if hea_trig.at[i]>(exp_trig.at[0]) and  hea_trig.at[i]<(exp_trig.at[len(exp_trig)-1]) :
                heasarc.at[i,'EXISTENCE']=1
            j+=1
            if i>0:
                i-=1
    else:
        i+=1

heasarc.to_sql('heasarc_data', cnx, if_exists='replace', index = False)
explored.to_sql('explored_data', cnx, if_exists='replace', index = False)

cnx.commit()
cnx.close()

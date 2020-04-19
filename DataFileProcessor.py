
import fromWebToDataFile as website
import fermiTrigger as trig
import os
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print("\n\n")
heasarc=website.website(dataFileName="heasarc",url="https://heasarc.gsfc.nasa.gov/FTP/fermi/data/tdat/heasarc_fermigtrig.tdat")
heasarc.updateContent()

allTriggers=[]

f=open(heasarc.dataFileName,"r")
line=""
while line!="<DATA>\n":
    try:    
        line=f.readline()
    except:
        print("no DATA found : try updating")
lines=f.readlines()


print("Reading data...")

count=1
for line in lines:
    if line!="<END>\n":
        newTrigger=trig.trigger(line)
        allTriggers.append(newTrigger)
        sys.stdout.write(str(count))
        for _ in range(len(str(count))):
            sys.stdout.write("\r")
        count=count+1
sys.stdout.write("\r"+str(count))

print("\nReading data is over.")
print("Creating database...")

# We created our data-structure, now it is time to create our database from it

import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('triggered.db')
c = conn.cursor()
#create database: if exist delete and create again
try:
    c.execute('''CREATE TABLE heasarc_data
                (version,trigger_name,name,ra,dec,lii,bii,error_radius,time,end_time,trigger_time,time_mjd,end_time_mjd,trigger_time_mjd,trigger_type,reliability,
                trigger_timescale,trigger_algorithm,channel_low,channel_high,adc_low,adc_high,detector_mask,geo_long,geo_lat,
                ra_scx,dec_scx,ra_scz,dec_scz,theta,phi,localization_source)''')

except Error:
    c.execute('''DROP TABLE heasarc_data ''')
    c.execute('''CREATE TABLE heasarc_data
                (version,trigger_name,name,ra,
                dec,lii,bii,error_radius,
                time,end_time,trigger_time,time_mjd,
                end_time_mjd,trigger_time_mjd,trigger_type,reliability,
                trigger_timescale,trigger_algorithm,channel_low,channel_high,
                adc_low,adc_high,detector_mask,geo_long,
                geo_lat,ra_scx,dec_scx,ra_scz,
                dec_scz,theta,phi,localization_source)''')


count=1
sys.stdout.write("\r: ")
for i in allTriggers:
    c.execute('INSERT INTO heasarc_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(i.dictionary.get('version'),i.dictionary.get('trigger_name'),i.dictionary.get('name'),i.dictionary.get('ra'),
                                                                                                                     i.dictionary.get('dec'),i.dictionary.get('lii'),i.dictionary.get('bii'),i.dictionary.get('error_radius'),
                                                                                                                     i.dictionary.get('time'),i.dictionary.get('end_time'),i.dictionary.get('trigger_time'),i.dictionary.get('time(mjd)'),
                                                                                                                     i.dictionary.get('end_time(mjd)'),i.dictionary.get('trigger_time(mjd)'),i.dictionary.get('trigger_type'),i.dictionary.get('reliability'),
                                                                                                                     i.dictionary.get('trigger_timescale'),i.dictionary.get('trigger_algorithm'),i.dictionary.get('channel_low'),i.dictionary.get('channel_high'),
                                                                                                                     i.dictionary.get('adc_low'),i.dictionary.get('adc_high'),i.dictionary.get('detector_mask'),i.dictionary.get('geo_long'),
                                                                                                                     i.dictionary.get('geo_lat'),i.dictionary.get('ra_scx'),i.dictionary.get('dec_scx'),i.dictionary.get('ra_scz'),
                                                                                                                     i.dictionary.get('dec_scz'),i.dictionary.get('theta'),i.dictionary.get('phi'),i.dictionary.get('localization_source'),))
    sys.stdout.write(str(count))
    if count!=len(allTriggers):
        for _ in range(len(str(count))):
            sys.stdout.write("\r")
    count=count+1
print("\nTable created.")


conn.commit()
conn.close()

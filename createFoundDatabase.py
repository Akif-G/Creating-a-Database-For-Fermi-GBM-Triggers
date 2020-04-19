import os		
from scipy.io import readsav
import sys
#adress = "search_transients/results/Poisson/"
#downloaded on computer:
adress="./"
modes = ["Mode_2"]  #, "Mode_2", "Mode_3", "Mode_4"]

allTimes=[]

for mode in modes:
    print("\n\n" + mode + " started.\n\n")
    dates = os.listdir(adress + mode)
    list_ = "list_" + mode
    #dates.remove(list_)
    for date in dates:
        print(mode + " " + date + " started.")
        savs = os.listdir(adress + mode + "/" + date)
        arr = []
        for sav in savs:
            if ".csav" in sav:
                arr.append(sav)	
            if ".sav" in sav:
                s = sav[:sav.rfind(".")] + ".csav"
                if s not in arr:
                    arr.append(sav)
        print(".csavs are taken.")
        for i in arr:
            sav_name = adress + mode + "/" + date + "/" + i
            fromIDL = readsav(sav_name, idict=None, python_dict=True, uncompressed_file_name=None, verbose=False)
            for key, value in fromIDL.items():
                if key == 'burst_data':
                    #allTimes.append(repr(value))
                    allTimes.append(value)
            
        print(mode + " " + date + " ended.\n")
    print(mode + " ended.")
print('READING END\n->Starting to create the database...')


import sqlite3
from sqlite3 import Error
import trigdate as td

conn = sqlite3.connect('triggered.db')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE explored_data (json_raw,time_mjd, time_met,time_iso)''')

except Error:
    c.execute('''DROP TABLE explored_data''')
    c.execute('''CREATE TABLE explored_data (time_mjd, time_met,time_iso,json_raw)''')

asTrigtimes=[]

for i in allTimes:
    asTrigtimes.append(td.trigDate(i[0][0],"met"))


count=1
sys.stdout.write("\r: ")
for i in range(len(allTimes)):
    c.execute('INSERT INTO explored_data VALUES (?,?,?,?)',(asTrigtimes[i].mjd,asTrigtimes[i].met,asTrigtimes[i].date,allTimes[i]))
    sys.stdout.write(str(count))
    if count!=len(asTrigtimes):
        for _ in range(len(str(count))):
            sys.stdout.write("\r")
    count=count+1


conn.commit()
conn.close()

import os		
from scipy.io import readsav
import sys
adress = "/vdata1/shared/search_transients/results/Poisson/"
#when downloaded on computer:
#adress="./"
modes = ["Mode_4"]  #, "Mode_2", "Mode_3", "Mode_4"]

allTimes=[]

for mode in modes:
    print("\n\n" + mode + " started.\n\n")
    dates = os.listdir(adress + mode)
    list_ = "list_" + mode
    #dates.remove(list_)
    count=0
    for date in dates:
        print(mode + " " + date + " started.")
        try:
          savs = os.listdir(adress + mode + "/" + date)
          arr = []
          count+=1
          for sav in savs:
              if ".csav" in sav:
                  arr.append(sav)	
          print(".csavs are taken\n"+str(len(dates)-count))
          for i in arr:
              sav_name = adress + mode + "/" + date + "/" + i
              fromIDL = readsav(sav_name, idict=None, python_dict=True, uncompressed_file_name=None, verbose=False)
              for key, value in fromIDL.items():
                  if key == 'burst_data':
                      #allTimes.append(repr(value))
                      allTimes.append(value)
              
          print(mode + " " + date + " ended.\n")
        except:
          print("problem occured or end of files")
        
    print(mode + " ended.")
print('READING END\n->Starting to create the database...')


import sqlite3
from sqlite3 import Error
import trigdate as td
os.chdir(os.path.dirname(os.path.realpath(__file__)))

conn = sqlite3.connect('triggered.db')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE Mode4 (time_mjd,time_iso, time_met)''')

except Error:
    c.execute('''DROP TABLE Mode4''')
    c.execute('''CREATE TABLE Mode4 (time_mjd,time_iso, time_met)''')

asTrigtimes=[]

for i in allTimes:
    for j in i:
        asTrigtimes.append(td.trigDate(time=float(j[0]),Format="met"))


count=1
sys.stdout.write("\r: ")
for i in range(len(asTrigtimes)):
    c.execute('INSERT INTO Mode4 VALUES (?,?,?)',(asTrigtimes[i].mjd,asTrigtimes[i].date,asTrigtimes[i].met))
    sys.stdout.write(str(count))
    if count!=len(asTrigtimes):
        for _ in range(len(str(count))):
            sys.stdout.write("\r")
    count=count+1


conn.commit()
conn.close()

import os		
from scipy.io import readsav
import sys
adress = "/vdata1/shared/search_transients/results/Poisson/"
#when downloaded on computer:
#adress="./"
modes = ["Mode_3"]  #, "Mode_1", "Mode_2", "Mode_4"]

allTimes=[]
allSavs = []

for mode in modes:
    print("\n\n" + mode + " started.\n\n")
    dates = os.listdir(adress + mode)
    list_ = "list_" + mode
    #dates.remove(list_)
    count = 0
    for date in dates:
        print(mode + " " + date + " started.")
        try:
            isCsav=False    #indicates if a date includes csav files
            savs = os.listdir(adress + mode + "/" + date)
            arr = []
            count += 1
            for sav in savs:
                if ".csav" in sav or ".sav" in sav:
                    arr.append(sav)
                    isCsav = True
            if isCsav==False:
                for sav in savs:
                    if ".sav" in sav:
                        arr.append(sav)
                print(".sav s are taken.\n"+str(len(dates)-count))
            else:
                print(".csav s are here! and taken.\n"+str(len(dates)-count))

            for i in arr:
                sav_name = adress + mode + "/" + date + "/" + i
                fromIDL = readsav(sav_name, idict=None, python_dict=True,
                                    uncompressed_file_name=None, verbose=False)
                for key, value in fromIDL.items():
                    if key == 'burst_data':
                        #allTimes.append(repr(value))
                        allTimes.append(value)
                        allSavs.append(sav_name[:-4])

            print(mode + " " + date + " ended.\n")
        except:
            print("problem occured or (EOF)")

    print(mode + " ended.")
print('READING END\n->Starting to create the database...')



import sqlite3
from sqlite3 import Error
import trigdate as td
os.chdir(os.path.dirname(os.path.realpath(__file__)))

conn = sqlite3.connect('triggered.db')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE Mode3 (time_mjd,time_iso, time_met,detectors)''')

except Error:
    c.execute('''DROP TABLE Mode3''')
    c.execute('''CREATE TABLE Mode3 (time_mjd,time_iso, time_met,detectors)''')

trigTimesAndDetectors=[]

countTime = 0
for i in allTimes:
    count = 0
    for j in i:
        count += 1
        newTrigger = []
        newTrigger.append(td.trigDate(time=float(j[0]), Format="met"))
        newTrigger.append("".join(map(str, j[2])))
        newTrigger.append(allSavs[countTime]+"_12det_"+str(count)+".ps")
        trigTimesAndDetectors.append(newTrigger)
    countTime += 1

count=1
sys.stdout.write("\r: ")
for i in range(len(trigTimesAndDetectors)):
    c.execute('INSERT INTO Mode3 VALUES (?,?,?,?,?)',
              (trigTimesAndDetectors[i][0].mjd, trigTimesAndDetectors[i][0].date, trigTimesAndDetectors[i][0].met, trigTimesAndDetectors[i][1], newTrigger[i][2]))
    sys.stdout.write(str(count))
    if count!=len(trigTimesAndDetectors):
        for _ in range(len(str(count))):
            sys.stdout.write("\r")
    count=count+1


conn.commit()
conn.close()

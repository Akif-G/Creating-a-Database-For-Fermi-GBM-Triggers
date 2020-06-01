import datetime as dt
from astropy.time import Time

print("if any issue is appeared PLEASE NOTIFY DEVELOPER.")

# global leap Second file searcher for given location:
leapSecs=[]
try:
    with open('/vdata1/shared/search_transients/codes/misc/leap_sec.txt', "r") as f:
        for line in f:
            try:
                leapSecs.append(float(line))
            except EOFError:
                break
            except:
                pass
    print("file found in:: /vdata1/shared/search_transients/codes/misc/leap_sec.txt")
    #if global file is not found look for local file
except:
    try:
        print("no Leap Second file found in:"+str(leapPath))
        print("looking locally...")
        line=""
        with open('leap_sec.txt', "r+") as f:
            for line in f:
                try:
                    leapSecs.append(float(line))
                except EOFError:
                    break
                except:
                    pass
        #if local file is also not found use the values below.
    except:
        if len(leapSecs)<3:
            print("no Leap Second file found")
            print("using predefined time values with starting point: 51910.00000000")
            leapSecs.append(53735.99998843)
            leapSecs.append(54831.99998843)
            leapSecs.append(56108.99998843)
            leapSecs.append(57203.99998843)
            leapSecs.append(57753.99998843)

print("leap seconds:")       
for i in range(len(leapSecs)):
    print(i,":",leapSecs[i])

def is_float(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False

class trigDate:
    def __init__(self,time,Format="mjd"):
        #you can use met,mjd,jd,iso
        #self class provides very complex comparisons
        #for triggers date and gave you simple progress about
        if(Format=="mjd"):
            self.mjd=float(time)
            self.jd=float(self.mjd)+2400000.5
            self.met=self.MJDtoMET(self.mjd)
            self.date=Time(float(self.jd),format='jd').iso

        elif(Format=="met"):
            self.met=float(time)
            self.mjd=self.METtoMJD(self.met)
            self.jd=self.mjd+2400000.5
            self.date=Time(float(self.jd),format='jd').iso

        elif(Format=="jd"):
            self.jd=float(time)
            self.mjd=self.jd-2400000.5
            self.met=self.MJDtoMET(self.mjd)
            self.date=Time(float(self.jd),format='jd').iso

        elif(Format=="iso"):
            date=Time(str(time),format='iso')
            self.date=date.iso
            self.mjd=date.jd-2400000.5
            self.jd=date.jd
            self.met=self.MJDtoMET(self.mjd)

        else:
            raise Exception


    def MJDtoMET(self,mjd):
        #converts mjd to met.
        #51910 : mission start date.
        #returns float
        
        met=(mjd-51910.00000000)*60*60*24
        for leap in leapSecs:
            if leap>=51910.00000000:
                if mjd>leap:
                    met=met+1

        return float(met)
        

    def METtoMJD(self,met):
        mjdTrial=(met/(60*60*24))+51910
        
        for leap in leapSecs:
            if leap>=51910.00000000:
                if mjdTrial>leap:
                    met-=1

        mjd=(met/(60*60*24))+51910
        return float(mjd)
    

        
"""tests
mete=trigDate(time=57755,Format="mjd")
print(mete.jd)
print(mete.mjd)
print(mete.met)
print(mete.date)

meteson=trigDate(time=mete.met,Format="met")
print(meteson.jd)
print(meteson.mjd)
print(meteson.met)
print(meteson.date)


mete=trigDate(time=meteson.date,Format="iso")
print(mete.jd)
print(mete.mjd)
print(mete.met)
print(mete.date)


meteson=trigDate(time=mete.met,Format="met")
print(meteson.jd)
print(meteson.mjd)
print(meteson.met)
print(meteson.date)
"""

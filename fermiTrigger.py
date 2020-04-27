import trigdate as trigdate

def find_nth(haystack, needle, n):
    if n==0:
        return -1
    else:
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start



class trigger:
    def __init__(self,line=""):
        self.keys=["version","trigger_name","name","ra","dec","lii","bii","error_radius","time","end_time","trigger_time","time(mjd)","end_time(mjd)","trigger_time(mjd)","trigger_type","reliability",
        "trigger_timescale","trigger_algorithm","channel_low","channel_high","adc_low","adc_high","detector_mask","geo_long","geo_lat",
        "ra_scx","dec_scx","ra_scz","dec_scz","theta","phi","localization_source"]
        self.dictionary={"version":'',"trigger_name":'',"name":'',"ra":'',"dec":'',"lii":'',"bii":'',"error_radius":'',"time":'',"end_time":'',"trigger_time":'',"time(mjd)":'',"end_time(mjd)":'',"trigger_time(mjd)":'',"trigger_type":'',"reliability":'',
        "trigger_timescale":'',"trigger_algorithm":'',"channel_low":'',"channel_high":'',"adc_low":'',"adc_high":'',"detector_mask":'',"geo_long":'',"geo_lat":'',
        "ra_scx":'',"dec_scx":'',"ra_scz":'',"dec_scz":'',"theta":'',"phi":'',"localization_source":''}
        
        a=0
        for i in range(32):
            if (i==8 or i==9 or i==10 ) and (a<3):
                value=trigdate.trigDate(float(line[find_nth(line,"|",i)+1:find_nth(line,"|",i+1)]), Format="mjd")
                obj={self.keys[i]:value.met}
                a=a+1
            else:
                if (i>10):
                    i=i-3
                    obj={self.keys[i+3]:line[find_nth(line,"|",i)+1:find_nth(line,"|",i+1)]}
                else:
                    obj={self.keys[i]:line[find_nth(line,"|",i)+1:find_nth(line,"|",i+1)]}

            self.dictionary.update(obj)

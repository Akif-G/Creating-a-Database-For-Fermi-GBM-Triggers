
import urllib2
import os

class website:
    """To be able to use a website creates a website html from data file's first line.
    If there is no data file creates one. you can change data file's name by writing it while creating, fo futher use.
    It can be constucted by userinput."""
    
    heasarc_url="https://heasarc.gsfc.nasa.gov/FTP/fermi/data/tdat/heasarc_fermigtrig.tdat"
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def __init__(self,dataFileName="data",url=heasarc_url):
        self.dataFileName=dataFileName
        try:
            f=open(dataFileName,"r")
            print("file found: "+str(dataFileName))

        except IOError:
            print("NO Datafile FOUND with name:"+str(dataFileName))
            f=open(dataFileName,"w+")
            f.write(str(url))
            print("created DATA FILE for you, as: \""+ str(dataFileName)+ "\" in: "+ str(os.path.dirname(os.path.realpath(__file__))))
        f.close()

        f=open(dataFileName,"r+")
        f.seek(0)

        self.dataFile=f
        self.url=self.dataFile.readline()     

        if len(self.url)==0:
            print("NO DATA & URL in file! Assign URL with method: website.change_url()")
            print("url assigned as: "+str(url))
            self.url=url
            print("change URL or use method: updateContent to get data.")
            f.seek(0)
            f.writelines(url)
        else:
            print("URL found: "+self.url)
        
    def change_url(self,givenUrl):
        """after changing url you need to use method: updateContent"""
        self.url=givenUrl
        self.dataFile.seek(0)
        urlLine=self.dataFile.readline()

        #changing url in file 
        with open(self.dataFileName, "r") as f:
            lines = f.readlines()
        with open(self.dataFileName, "w") as f:
            for line in lines:
                if line.strip("\n") != urlLine:
                    f.write(line)
                else:
                    f.write(givenUrl)
        print("Url changed: " +str(self.url)+"\nUse method: updateContent to update DATA.")

    def change_dataFileName(self,dataFileName):
        self.dataFileName=dataFileName   
 
    def updateContent(self):
        try:
            self.dataFile.close()
            self.dataFile=open(self.dataFileName,"wb")
            response = urllib2.urlopen(self.url)
            webContent = response.read()
            self.dataFile.write(str(self.url+"\n").encode())
            self.dataFile.write(webContent)
            self.dataFile.close()
            self.dataFile= open(self.dataFileName,"r+")
            print("UPDATED DATA FROM: "+str(self.url))
        except:
            print("UPDATE IS FAILED !!!")


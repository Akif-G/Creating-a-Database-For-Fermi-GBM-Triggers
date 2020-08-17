
# Creating a Database of Astrophysical Sources
 
  ---
## Contributing

first of all:
- create a github account
- be sure you have Git installed in your system

### Download code:

branch_name can be: / empty for cloning: will clon on master (not preffered) /  preffered: github / or literally anything you want. 
```console
git clone -b <branch_name> https://github.com/Akif-G/Creating-a-Database-For-Fermi-GBM-Triggers 
```

### Make Your changes on your favorite ide

### save them to your local git repository:

```console
git add .

git commit -m "<AN EXPLANATION HERE>"
```


### push your changes to the github repository on origin (github.com) When You are completely done.

- do not create Pull request after every commit you done,
- can not create a Pull request if origin repository has changed...
```console
git push -u origin <branch_name>
```
 ---

### Contributing Again:
you can continue contributing if your previous commits merged in origin repository (github)

```console
git pull  -u origin master
```

### Make Your changes on your favorite ide

### save them to your local git repository:

```console
git add .

git commit -m "<AN EXPLANATION HERE>"
```
### push your changes to the github repository on origin (github.com) When You are completely done.
```console
git push -u origin <branch_name>
```
---
## Abstract

The Fermi Gamma-ray Space Telescope, formerly known as the Gamma-ray Large Area Space Telescope (GLAST), the Gamma-ray Burst Monitor (GBM) was designed by the National Aeronautics and Space Administration (NASA) to capture and monitor gamma-rays from a distant cosmos. GBM contains 12 detectors that are used by astrophysicists to obtain and analyze information.

Our research focuses on identifying and analyzing short-lived, “transient”, astrophysical events, observed with NASA’s Fermi Gamma-ray Space Telescope. In this project, our aim is to gather data from known astrophysical gamma-ray transient sources of all types and to form a database using them and to compare different searching algorithms to identify the matching events and finally to create a web-based interface for accessing that database so that the events can be identified accurately and easily.

  

# Introduction

Gamma-ray transient events or Gamma-ray bursts (GRBs) are bursts of gamma-ray light. Gamma-ray lights are the most energetic forms of light occurring in galaxies and that happen in a few milliseconds to several minutes. When a burst takes place in-universe it is the brightest source of gamma-ray photons in a brief time that it occurs (NASA, n.d.). In 2008, June 11 Fermi Gamma-Ray Space Telescope launched by NASA to explore gamma-rays (Howell, 2018.). For this purpose, it has mounted an instrument called Gamma-Ray Burst Monitor (GBM) which is designed to search the gamma-ray bursts by detecting the sudden change in flux of photons with several detectors when bursts occur. Moreover, GBM measures spectra and light curves of bursts in the energy range 8 keV to 30 MeV with a high time resolution of 0.256 s normal and 0.064 s during bursts. GBM not only observes the burst triggers but also detects the locations as a result of high resolution. When the detected energy level of photons is above a certain threshold, the detector becomes triggered meaning that a gamma-ray burst has happened. Later this information is sent to an international network of observing sites. (MPA, n.d.) (NASA, n.d.). However, the data could include untriggered gamma-ray transient events as well due to lack of flux or shorter amount of time than needed to identify the observation as triggered.

Previously we developed a searching and filtering algorithm to analyze the large database of GBM and detect the untriggered gamma-ray transient events by eliminating the missing time intervals and the missing data to make the analyzing process more accurate. In this step of our project we created five databases, one for Heasarc, NASA’s archive that has triggered data detected by NASA and four for the detections done by our supervisors’ search algorithm. What we are doing in this project is comparing the times of the triggered events in both algorithms and finding the matching events.

  

## Developing the Database

We use a large observational database of an instrument (GBM) onboard Fermi, to search for such “transient” events, and each event found in the search must be categorized and identified.  Such a database is crucial for correct identification of the transient events found in our search.

  

### Code Flow And Database Implementations

There is a Heasarc database which is on the official NASA website. There exists triggered data that was detected by NASA. In addition to that, there is a detection algorithm developed by our supervisors. So, there are two sources for our database creating algorithm; one taken from heasarc.com and the other one is created by our supervisors on the vega server, which is the official super-computer of Sabanci University. Our aim was to check the number of matching triggered data.![](https://lh3.googleusercontent.com/Eu9fqVMuw1g0lx0T9AJpcYTCBH7YWrNgvzYwF-INy-UWnK5srWYgjuct9CdqPEuGiZVPPQE7bkwCl8LYRoxHSDDScHYkvt7dzDBRJOx6b9ewduZGSPEFlhCioc2jSc8z5PBVrI4M)

  

### Helper Class Implementations

There are two helper classes for the implementations of triggers, which is used in the stage of storing the databases in SQL.

There is also a helper class implemented for storing the Heasarc webpage as a structural information, with methods.

Finally, there are two helper classes .There are 3 types of time; mjd, mit, iso. Mjd in terms of day and mit in terms of the second. There is a reference date depending on the beginning day of the project and it is the thing that decides the reference date. Met is referred to the day after the mission began. On the other hand it refers to the second that passed after the beginning of the mission. We needed to implement an algorithm that does time conversion between this methods with the information of leap-seconds .

  
### Creating a Database for Heasarc webpage

There are two main functional algorithms in this module. One is implemented to be able to scrape and store or update the webpage as offline. The other one is converting the webpage into a SQLite3 database.

#### Storing the Webpage Offline

Here, we implemented a helper algorithm, a python class for web page, which includes all the data, indicators and much more. The algorithm is implemented in a way that is allowed to be used separated from the other functions.

#### Converting the webpage into a SQL database

In this step there is also two helper implementations that is created: creating every trigger in webpage, converting the time between mission elapsed time (MET)  and Modified Julian Date (MJD) .

![](https://lh3.googleusercontent.com/szhKQeevsFvjqvmwBJy0ET813p6I84-FIQ98sDrcDjUgiOuCY3Cs1i2HrhlsbPJ2TwnDYnsLVFV85trKUqewul7BComcD10-yAV1DRuh_6G-_1i2_027JngWmob1TZaUkR8rvhbA)

  

### Create Databases for Filtered Results

There are 4 modes in the vega server, and two types of data, .csav and .sav. Initially all of them were .sav but they were checked manually and checked ones called .csav. So, we have taken the data from .csav, if it exists, if not we used .sav ones. So, there is basically the same data in both of them but there is a manually taken note in the .csav files.

In this stage, there are four main algorithms implemented in separated modules. Every one of them is handling the different filtering results. There is also one helper implementation which is used for time conversion.

  

### Comparison of the Databases

After creating the databases we implemented a comparison algorithm which uses cross comparison with sorted results. With this additional sorted feature the comparison algorithm got very fast. It is important to be fast for us, because we have very huge datasets in any aspect.

Cross-comparison of the sorted values, decides the overlapping triggers of heasarc databases with the range of 0.5 seconds.

  

### Testing

Testing algorithm is implemented to be used for cross-check validation. Cross-check validation can be used to check comparison algorithms’ correctness. What we are doing here is, taking the state before comparison and subtracting the ‘sorted’ feature. Then, checking every value and creating the comparison table again. If there is any difference with fast comparison algorithms, the values will be different. After that it is not easy to have a mistake and not realize.

This algorithm is very slow since it is not using the decreased comparisons of sorted values. So it should be run when final filtering is done.

We have also checked our results to be sure we would not face any bugs afterwards.

  

### Improvements

First of all, we wanted to have a version controlling feature in our implementations. So, we used git for this purpose. We also shared our code as open-source implementation via Github.

Secondly and most importantly, our implementations are placed in separate modules and handled with the error-handling feature of python. So, we are able to use these modules again and it is more likely to be bug-free .

The future works of the project is simply, creating a website as a front-end aspect for our database.

  

## Discussion and Conclusion

We have focused on creating a database for a dataset that exists in the vega server, for the FERMI satellite. Firstly, we have created a database for Heasarc which is the detected time by NASA. Trigger times are defined by NASA and they refer to the events that pass the threshold of the satellite’s detectors. There are twelve detectors on the FERMI. The events that could not pass the threshold are not in the heart, however, there is lots of other data in the set. Also, there is a whole data package with triggered and untriggered data. We created two databases for both of them and compared them to each other to check if there is a missing trigger in the heasarc. This means: if the threshold is not passed, the event is not considered as a “trigger”, however, it is open to discussion that there might be loose events. So, there is a more tolerated searching algorithm developed by our supervisors, and triggered events depend on that algorithm in the vega server. With creating the database we became able to check the possible other triggered data that do not exist in the heart database. There are 4 types of modes 1,2,3 and 4, the newly developed searching algorithm does not search all of the satellite histories, it is focused on special dates that the number of triggers is not high. There are 7.000 triggered data in the heart and a total of more than 20.000 data in the vega server. There is a special column to show the newly detected data that’s not detected in heasarc, but detected with another algorithm.

  
  

References

-   HEASARC Data Archive - HEASARC: NASA's Archive of Data on ... (n.d.). Retrieved May 17, 2020, from https://heasarc.gsfc.nasa.gov/docs/archive.html
    
-   Andrew.novick@nist.gov. (2020, February 11). Leap Seconds FAQs. Retrieved May 17, 2020, from https://www.nist.gov/pml/time-and-frequency-division/leap-seconds-faqs
    
-   Leap second. (2020, May 10). Retrieved May 17, 2020, from https://en.wikipedia.org/wiki/Leap_second
    
-   FSSC: Fermi Data " Data Analysis " Online Documentation " Fermitools: Cicerone - Data. (n.d.). Retrieved May 17, 2020, from https://fermi.gsfc.nasa.gov/ssc/data/analysis/documentation/Cicerone/Cicerone_Data/Time_in_ScienceTools.html

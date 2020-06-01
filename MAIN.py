import os		
import sys

"""
execute python scripts in an order.

-> create Heasarc Database
-> Create Databases for each Mode
-> Compare everything. (fast)
-> Optional cross comperation validation test (slow)
"""

try:
    execfile('./createHeasarcDatabase.py')
except NameError:
    exec(open('./createHeasarcDatabase.py').read())

print("heasarc database created:")


try:
    execfile('./Mode1_createDB.py')
    print("DATABASE CREATED FOR MODE1 created:")
except NameError:
    try:
        exec(open('./Mode1_createDB.py').read())
        print("DATABASE CREATED FOR MODE1 created:")
    except:
        print("file path problem occured while reading mode 1")

try:
    execfile('./Mode2_createDB.py')
    print("DATABASE CREATED FOR MODE2 created:")

except NameError:
    try:
        exec(open('./Mode2_createDB.py').read())
        print("DATABASE CREATED FOR MODE2 created:")
    except:
        print("file path problem occured while reading mode 2")

try:
    execfile('./Mode3_createDB.py')
    print("DATABASE CREATED FOR MODE3 created:")
except NameError:
    try:
        exec(open('./Mode3_createDB.py').read())
        print("DATABASE CREATED FOR MODE3 created:")
    except:
        print("file path problem occured while reading mode 3")

try:
    execfile('./Mode4_createDB.py')
    print("DATABASE CREATED FOR MODE4 created:")
except NameError:
    try:
        exec(open('./Mode4_createDB.py').read())
        print("DATABASE CREATED FOR MODE4 created:")
    except:
        print("file path problem occured while reading mode 4")

try:
    execfile('./compareDatabases.py')
except NameError:
    exec(open('./compareDatabases.py').read())

willTest=raw_input("WOULD YOU LIKE TO TEST THE RESULTS? IT IS VERY SLOW but accurate...\nY=YES\nN=NO")
if(willTest=="Y"):
    try:
        execfile('./slowTester.py')
    except NameError:
        exec(open('./slowTester.py').read())

    
print("\n\n---------------------------------------END---------------------------------------")

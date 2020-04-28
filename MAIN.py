import os		
import sys

try:
    execfile('./createHeasarcDatabase.py')
except NameError:
    exec(open('./createHeasarcDatabase.py').read())

print("heasarc database created:")
os.chdir(os.path.dirname(os.path.realpath(__file__)))


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



os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    execfile('./compareDatabases.py')
except NameError:
    exec(open('./compareDatabases.py').read())

print("\n\n---------------------------------------END---------------------------------------")

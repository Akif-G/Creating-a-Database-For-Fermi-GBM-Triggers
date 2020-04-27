import os		
import sys

execfile('./createHeasarcDatabase.py')
print("heasarc database created:")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

execfile('./Mode1_createDB.py')
print("DATABASE CREATED FOR MODE1 created:")

execfile('./Mode2_createDB.py')
print("DATABASE CREATED FOR MODE2 created:")

execfile('./Mode3_createDB.py')
print("DATABASE CREATED FOR MODE3 created:")

execfile('./Mode4_createDB.py')
print("DATABASE CREATED FOR MODE4 created:")


os.chdir(os.path.dirname(os.path.realpath(__file__)))
execfile('./compareDatabases.py')

print("\n\n---------------------------------------END---------------------------------------")

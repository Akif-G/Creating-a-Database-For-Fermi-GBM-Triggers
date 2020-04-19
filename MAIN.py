import os		
import sys

execfile('./createHeasarcDatabase.py')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

execfile('./createFoundDatabase.py')
os.chdir(os.path.dirname(os.path.realpath(__file__)))
execfile('./compareDatabases.py')

print("\n\n---------------------------------------END---------------------------------------")

import os		
import sys

execfile('./DataBaseProcessors/createHeasarcDatabase.py')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

execfile('./DataBaseProcessors/createFoundDatabase.py')
os.chdir(os.path.dirname(os.path.realpath(__file__)))
execfile('./DataBaseProcessors/compareDatabases.py')

print("\n\n---------------------------------------END---------------------------------------")

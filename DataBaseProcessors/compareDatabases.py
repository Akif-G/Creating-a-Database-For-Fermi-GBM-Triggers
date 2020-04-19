import os		
import sys

conn = sqlite3.connect('triggered.db')
c = conn.cursor()




conn.commit()
conn.close()

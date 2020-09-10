#!/usr/bin/env python3

import sqlite3
import sys
import argparse
from datetime import datetime

def parse(argv):
   parser = argparse.ArgumentParser(description='Updates brew and opens homepages of random formulae and casks so you can explore some amazing software')
   parser.add_argument('n_formulae', metavar='F', help='number of formulae', type=int, nargs='?', default=3)
   parser.add_argument('n_casks', metavar='C', help='number of casks', type=int, nargs='?', default=3)
   return parser.parse_args(argv)

args = parse(sys.argv[1:]) # first element is script itself
print(args)
exit(1)
# Connect to db
conn = sqlite3.connect('db.sqlite3') # Use ':memory:' for temporary db in RAM
db = conn.cursor()

# Get time
time = datetime.now()
time_s = time.strftime('%Y-%M-%D %H:%M:%S')

# Remember formulae shown
db.execute("INSERT INTO formulae VALUES (?, ?)", (time_s, formulae))
# Remember casks shown./
db.execute("INSERT INTO casks VALUES (?, ?)", (time_s, casks))

# Grab all stock transactions of the given symbol and print one
symbol = ('RHAT',)
db.execute('SELECT * FROM stocks WHERE symbol=?', symbol)
print(db.fetchone())

# Insert many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),]
db.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# Get all buy transactions and print them all
trans = ('BUY',)
db.execute('SELECT * FROM stocks WHERE trans=?', trans)
print(db.fetchall())

# Save (commit) the changes
conn.commit()

# Close connection (doesn't auto-save)
conn.close()

def get_formulae():
   return None
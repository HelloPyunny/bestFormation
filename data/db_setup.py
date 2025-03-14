import sqlite3
import pandas as pd

# load data from csv
df = pd.read_csv('data_updated.csv')

# connect to sqlite3
conn = sqlite3.connect('players.db')
cursor = conn.cursor


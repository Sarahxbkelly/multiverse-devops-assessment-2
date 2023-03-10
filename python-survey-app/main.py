import pandas as pd

from csv_processor import read_csv
import csv

file_path = './results.csv'# Read the fileprint(read_csv(file_path))

results = (read_csv(file_path))

duplicates = set()

cleanresults = []

for rec in results:
    id = rec[0]
    if id not in duplicates:
        duplicates.add(id)
        cleanresults.append(rec)

print(cleanresults)




#print(results)





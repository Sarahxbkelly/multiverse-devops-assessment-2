from csv_processor import read_csv
import csv
from remove_duplicate import remove_duplicates
from remove_empty_record import remove_empty_records

file_path = './results.csv'# Read the fileprint(read_csv(file_path))

results = (read_csv(file_path))

#print(results)

#ticket 2 & 3

cleanresults = remove_empty_records(results)

print(cleanresults)

#ticket 4














from csv_processor import read_csv # ticket 7
import csv

file_path = './clean_results.csv'# Read the fileprint(read_csv(file_path))

clean_results = (read_csv(file_path))

for row in clean_results:
    print (row)



#print(clean_results)

  


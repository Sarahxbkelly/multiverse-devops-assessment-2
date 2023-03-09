from csv_processor import read_csv
import csv
def write_csv(row, file_path):
    with open(file_path, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(row)
def append_csv(row, file_path):
    with open(file_path, 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(row)

file_path = './results.csv'# Read the fileprint(read_csv(file_path))

print(read_csv(file_path))


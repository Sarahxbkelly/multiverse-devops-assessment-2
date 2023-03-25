import csv
from csv_processor  import read_csv # ticket 1
from remove_duplicate import remove_duplicates #ticket 2
from remove_empty_record import remove_empty_records #ticket 3
from capitalise import capitalise #ticket 4
from validate_field import validate_field #ticket 5



file_path = 'results.csv'
file_name = 'clean_results.csv'

results = (read_csv(file_path))

cleanresults = validate_field(remove_duplicates(remove_empty_records(capitalise(results))))


with open('clean_results.csv', mode='w', newline='') as clean_results:
    writer = csv.writer(clean_results, delimiter=',')
    writer.writerows(cleanresults) #ticket 6























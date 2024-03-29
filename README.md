# multiverse-devops-assessment-2

Python-Survey-App

The base application for the DevOps assignment 2: Report on the development and operationalisation of a data-based
application

The application covers all tickets listed below:

Ticket #1 Read a CSV file
Description In your input script, create a function that will read data from a CSV file.
Objectives
-The results.csv data file can be successfully processed into an array.
-Each line of the file is read into a new array item.
-The file read method must be in a sub-module.

Ticket #2 Remove duplicate entries
Description Add functionality to your input script to ignore or remove any duplicate entries
from the input data.
Duplicates are based on the User Id field.
Objectives
-A final array is created with duplicate entries removed.
-Where duplicates are found, the first entry is retained.

Ticket #3 Ignore empty lines
Description Update your input script to ignore any empty lines found when reading in the
input data file.
Objectives
-A final array is created with any empty lines omitted.

Ticket #4 Capitalise user name fields
Description Add functionality to your input script to automatically capitalise the first_name
and last_name fields found in the input data.
Objectives
-All names are capitalised in all data entries.

Ticket #5 Validate the responses to answer 3
Description Update your input script to validate the responses to the third answer field.
This answer must have a numeric value between 1 and 10.
Any rows with an invalid value are ignored.
Objectives
-A final array is created with the input data excluding any rows where
answer 3 is invalid.
-No answer 3 values will be outside the range of 1 to 10.

Ticket #6 Output the cleansed result data to a new file
Description Add functionality to your input script to output the cleansed data to a new CSV
file.
Objectives
-A new file is created called clean_results.csv.
-The file is recreated on each execution.
-No invalid or unformatted data is present in the new file.

Ticket #7 Create an output script
Description A new output script will be created which reads in the clean_results.csv CSV
file and outputs the results to the command line, row by row.
Objectives
-The script uses the existing sub-module to read the CSV file.
-The printed output will contain all row data and an appropriate header.
-Stretch: The printed output will be formatted with fixed length strings.

The application also runs unit tests for each ticket created. 

Terraform IAC

Code containing the infrastructure for this project

.github/workflows

Code containing all workflows for this project



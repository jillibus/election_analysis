# The Election Analysis Pseudocode
# Collect the data
# 1. Load the data from resources/election_results.csv
# 2. The total number of votes cast
# 2. A complete list of candidates to received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. Close the file resources/election_results.csv

# Import dependencies
import csv
import os
import datetime
import random
#import numpy

# Referencing File and opening it
# syntax: file_variable = open(file_name, mode) modes: (r)ead, (w)rite, 
#         e(x)clusive creation - it won't create one if not there, 
#         (a)ppend - will create the file if not there, otherwise it adds to the end,
#         (+) - open for read and write
#
# Create a way to connect to the election results data to process
file_to_load = os.path.join('election_analysis/resources','election_results.csv')

# Create a new file for program output in analysis folder
file_to_save = os.path.join('election_analysis/analysis','election_analysis.txt')

# (1) Open the election_results.csv file for read only
with open(file_to_load) as election_data:
    # Read data from election_results.csv
    file_reader = csv.reader(election_data)
    # Print header row
    headers = next(file_reader)
    print(headers)
    # Print contents of election_results.csv
    for row in file_reader:
        print(row)

# (2) Process the election results 



# (#) Open the election_analysis.txt file for writing
# (#) Write results to election_analysis.txt
with open(file_to_save, 'w') as election_results:
    # Write some data to our new file
    election_results.write('Counties in the Election\n')
    election_results.write('-------------------------\n')
    election_results.write('Arapahoe\n')
    election_results.write('Denver\n')
    election_results.write('Jefferson\n')



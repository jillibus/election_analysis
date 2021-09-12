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

# Variable to count all the votes
total_votes = 0
# Variables for the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Variables to extact from the CSV file
candidate_options = []
# Declare an empty dictionary
candidate_votes = {}

# (1) Open the election_results.csv file for read only
with open(file_to_load) as election_data:
    # Read data from election_results.csv
    file_reader = csv.reader(election_data)

    # Read the Header Row
    headers = next(file_reader)
    
    # Print each row of the CSV file
    for row in file_reader:
        # increment the total_vote count
        total_votes += 1

        # capture candidate_name from CSV file
        candidate_name = row[2]

        # add candidate_name to candidate_options
        if candidate_name not in candidate_options:
            # Add candidate_name to candidate list
            candidate_options.append(candidate_name)

            # Start tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# (#) Open the election_analysis.txt file for writing
# (#) Write results to election_analysis.txt
with open(file_to_save, 'w') as election_results:
    # Write some data to our new file
    election_results.write('Election Results\n')
    election_results.write('-----------------------------------\n')
    election_results.write(f'Total Votes: {total_votes:,}\n')
    election_results.write('-----------------------------------\n')

    # (2) Process the election results and determine winner
    for candidate_name in  candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        election_results.write(f'{candidate_name}:  {vote_percentage:.1f} ({votes:,})\n')
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    election_results.write('-----------------------------------\n')
    election_results.write(f'Winner: {winning_candidate}\n')
    election_results.write(f'Winning Vote Count: {winning_count:,}\n')
    election_results.write(f'Winning Percentage: {winning_percentage:.2f}\n') 
    election_results.write('-----------------------------------\n')


# Print to the terminal the results

#for candidate_name in  candidate_votes:
#    votes = candidate_votes[candidate_name]
#    vote_percentage = float(votes) / float(total_votes) * 100
 #   print(f'{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n')

#print(f'The winner of the election is {winning_candidate}\n')
#print(f'with {winning_count:,} votes making up {winning_percentage:.2f}% of the total votes')




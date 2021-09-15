counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = []
voting_data.append({'county':'Arapahoe','registered_voters':422829})
voting_data.append({'county':'Denver','registered_voters':463353})
voting_data.append({'county':'Jefferson','registered_voters':432438})

for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')   

#voting_data

# this prints a pretty version of the one below this
# i could have grabbed 'county' and 'registered_voters' from the voting_data
for county, voters in counties_dict.items():
    print(county," county has ",voters," registered voters.")    
# prints the entire line of each counties info in voting_data
for i in range(len(voting_data)):
    print(voting_data[i])
# another version of with the same result
for county_dict in voting_data:
    print(county_dict)
# How to get ther values from a list of dictionaries
for county_dict in voting_data:
    print(county_dict.values())
dict_values(['Arapahoe', 422829])
dict_values(['Denver', 463353])
dict_values(['Jefferson', 432438])
for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)
Arapahoe
422829
Denver
463353
Jefferson
432438

#Printing with variables
# all variables need to be converted to strings
# print('Your interest for the year is $ ' + str(interest))

# my_votes = int(input('How many votes did you get in the election? '))
# total_votes = int(input('What is the total votes in the election? '))
# precentage_votes = (my_votes / total_votes) * 100
# print('I received ' + str(percentage_votes)+ '% of the total votes')

# with Python3 you can use f-string
# my_votes = int(input('How many votes did you get in the election? '))
# total_votes = int(input('What is the total votes in the election? '))
# print(f'I received {my_votes / total_votes * 100}% of the total votes')

#for county, voters in counties_dict.items():
#    print(county + ' county has ' + str(voters) + ' registered voters.')
#    print(f'{county} county has {voters:,} registered voters.')

#candidate_votes = int(input('How many votes did the candidate get in the election? '))
#total_votes = int(input('What is the total votes in the election? '))
#message_to_candidate = (
#    f'You received {candidate_votes:,} number of votes.'
#    f'The total number of votes in the election was {total_votes:,}. '
#    f'You received {candidate_votes / total_votes * 100:.2f}% of the total votes.'
#)
#print(message_to_candidate)


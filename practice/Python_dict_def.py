# Definitions/examples of special lists - dictionaries

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for key, value in counties_dict.items():
    print(key,value)

# note the first variable is assigned to the keys
# the second variable is assigned to the values
for county, voters in counties_dict.items():
    print(county,voters)

>>> counties_dict = {}
>>> counties_dict['Arapahoe'] = 422829
>>> counties_dict
{'Arapahoe': 422829}
>>> counties_dict['Denver'] = 463353
>>> counties_dict['Jefferson'] = 432438
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> len(counties_dict)
3
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get('Denver')
463353
>>> counties_dict.get('Arapahoe')
422829
>>> print(counties_dict.get('Arapahoe'))
422829
>>> voting_data = []
>>> voting_data.append({'county':'Arapahoe','registered_voters':422829})
>>> voting_data.append({'county':'Denver','registered_voters':463353})
>>> voting_data.append({'county':'Jefferson','registered_voters':432438})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, 
{'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data[2] = ({'county':'El Paso','registered_voters':461149})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, 
{'county': 'El Paso', 'registered_voters': 461149}]
>>> voting_data.append({'county':'Denver','registered_voters':463353})
>>> voting_data[2]
{'county': 'Denver', 'registered_voters': 463353}
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, 
{'county': 'Denver', 'registered_voters': 463353}]
>>> voting_data.append({'county': 'Arapahoe', 'registered_voters': 422829})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438},
 {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]

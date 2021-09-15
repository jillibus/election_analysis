## lists - (arrays)  mutable (editable)
counties = ['Arapahoe','Denver','Jefferson']
if counties[3] != 'Jefferson':
    print(counties[2])

for i in range(len(counties)):
    print(counties[i])

# print counties
counties
counties[0]
'Arapahoe'
counties[1]
'Denver'
counties[2]
'Jefferson'
# print range based on position
counties[:2], counties[1:2], counties[:-1]
['Arapahoe','Denver']
counties[:3]
['Arapahoe','Denver','Jefferson']
counties[1:], counties[1:3]
['Denver','Jefferson']
counties[1:2]
['Denver']
# add to list
counties.append('El Paso')
counties.insert(2,'El Paso')  ## this actually overwrites what is in currently in position 2
# remove from list
counties.remove('El Paso')
counties.pop(3)
counties.pop(-1)
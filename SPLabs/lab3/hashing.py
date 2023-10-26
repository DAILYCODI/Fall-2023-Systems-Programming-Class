
newdict = dict()

newdict = {'key': 'some value', 1: 100, 'list_key': [1, 2, 3]}

res = newdict[1]
print(res)

newdict[2] = 99
print(newdict)
# cannot have duplicate keys

# get the value for the key 'list_key'
#x = newdict['list_key']
#print(x)

# update the value for 'list_key'
#newdict['list_key'] = 1

# get the value for the key 'list_key'
#y = newdict['list_key']
#print(y)

# # get the value for the key 'list_key'
#x = newdict['list_key']
#print(x)

# alternate way to get value

# update the value for 'list_key'
x = newdict.get('list_key')
print(x)

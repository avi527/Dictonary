my_dict={'name':'Avinash singh','age':90,'salary':'9lak'}
print(my_dict.get('name'))

# not match keys then what we output
print(my_dict.get('names')) #here come out is none but i want change output
print(my_dict.get('names','sorry not found !!'))


#if more than one key is same that what is output

my_dict1={'name':'Avinash singh','age':90,'salary':'9lak','age':92}
print(my_dict1)

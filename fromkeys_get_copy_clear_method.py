my_dict={'name':'Avinash singh','age':90,'salary':'9lak'}

#fromkeys method : here to write same value in allkey this condition
#to use fromkeys method

d=dict.fromkeys(['name','address'],'same')
print(d)

#get method:get method use for access the dict
print(d.get('name'))

print(my_dict.get('name'))
print(my_dict.get('salary'))

#copy method : copy method is used for dict in another dict as it is
dict_copy=my_dict.copy()
print(dict_copy)

#clear method : this method used for clear the dict
dict_clear=my_dict.clear()
print(dict_clear)

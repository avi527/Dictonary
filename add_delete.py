user_info={
    'name':'avinash',
    'age':23,
    'fav_player':'dhoni'
}
#print(type(user_info))
#print(user_info)
#add key and value in above dict
user_info['address']='noida'
print(user_info)

#delete fav_player from dict
retun_value=user_info.pop('fav_player')
print(retun_value)
print(user_info)

#popitem is work randmly delete any key
rendmly_delete=user_info.popitem()
print(rendmly_delete)
print(user_info)

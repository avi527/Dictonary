user_info={}
name=input("Enter name")
age=input("Enter age")
salary=input("Enter salary")
fav_movie=input("Enter Fav Movie seprate by comma").split(",")
fav_song=input("Enter fav song seprate by comma").split(",")
fav_actor=input("Enter fav actor seprate by comma").split(",")
user_info['name']=name
user_info['age']=age
user_info['salary']=salary
user_info['fav_movie']=fav_movie
user_info['fav_song']=fav_song
user_info['fav_actor']=fav_actor
for key,value in user_info.items():
    print(f"{key}:{value}")

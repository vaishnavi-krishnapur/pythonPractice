#Create some_dict = {'a': [1, 1, 2, 3]} create another_dict which is same as some_dict.
# Then modify some_dict without affecting another_dict and vice versa

main_dict ={'a': [1, 1, 2, 3]}
copied_dict=dict(main_dict)
print("main_dict : ", main_dict)
main_dict['b']=1
print("main_dict after main_dict modification:", main_dict)
print("copied_dict after main dict modification",copied_dict)
print("\n")
copied_dict['c'] =3
print("main_dict after both modifications:", main_dict)
print("copied dict after copied dict modification",copied_dict)


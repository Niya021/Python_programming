print("Name: Niya Joshy")
print("Admission No:A24MCA049")
print("Experiment No:5")

dict1={'apple':1,'cherry':2,'banana':3}
dict_asce=dict(sorted(dict1.items()))
print("Dictionary in ascending order ",dict_asce)
dict_desc=dict(sorted(dict1.items(),reverse=True))
print("Dictionary in descending order ",dict_desc)
dict2={'melon':4,'grapes':5}
dict1.update(dict2)
print("Merged dictionary ",dict1)

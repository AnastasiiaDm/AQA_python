"""
You have a group of people with non-unique names. Generate a list of non-duplicate names (you cannot use set for this
task. If there are 2 johns in the list, you need to take only one of them.
"John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")
"""
non_unique_names = ['Geralt of Rivia', 'Lutic Pankratz', 'Geralt of Rivia', 'Lutic Pankratz']
non_duplicate_names = {}.fromkeys(non_unique_names)
print(list(non_duplicate_names.keys()))

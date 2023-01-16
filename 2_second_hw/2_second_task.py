"""
You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba. Show it in code.
Keep in mind that people with the same name can be in both companies
"""
eleks = ['Geralt', 'Triss', 'Lutic']
toshiba = ['Yennefer', 'Ciri', 'Vesemir', 'Geralt']
toshiba.extend(eleks)
print(toshiba)

"""
You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist. Names of people in the format 
"John Dow" first and second name. Find those who are on all blacklists.
"""
casino_blacklist = {'Yennefer of Vangerberg', 'Lutic Pankratz', 'Triss Merigold'}
poker_blacklist = {'Triss Merigold', 'Lutic Pankratz', 'Geralt of Rivia'}
alcohol_blacklist = {'Geralt of Rivia', 'Lutic Pankratz', 'Triss Merigold'}
print(casino_blacklist.intersection(poker_blacklist, alcohol_blacklist))

"""
You have two groups of people. One group consists of omnivores, the other only vegetarians. An omnivore is a vegetarian 
but a vegetarian is not an omnivore. Display a list of guests who can eat vegetables and herbs.
"""
omnivores = {'Geralt of Rivia', 'Lutic Pankratz', 'Triss Merigold'}
vegetarians = {'Yennefer of Vangerberg', 'Triss Merigold'}

vegetables_and_herbs_guests = vegetarians.union(omnivores)
print(vegetables_and_herbs_guests)

"""
You have a group of guests for the VIP box. The seats in the VIP box are all occupied by these guests. There is a group 
of guests in the common room and there are still places in it. Display 2 groups of guests in code.
"""
vip_box = {
    1: 'Geralt of Rivia',
    2: 'Yennefer of Vangerberg',
    3: 'Triss Merigold'
}
common_room = {
    1: 'Lutic Pankratz',
    2: None,
    3: None
}

"""
You have a group of people with non-unique names. Generate a list of non-duplicate names (you cannot use set for this 
task. If there are 2 johns in the list, you need to take only one of them. 
"John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")
"""
non_unique_names = ['Geralt of Rivia', 'Lutic Pankratz', 'Geralt of Rivia', 'Lutic Pankratz']
non_duplicate_names = {}.fromkeys(non_unique_names)
print(list(non_duplicate_names.keys()))


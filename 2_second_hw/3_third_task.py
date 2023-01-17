"""
You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist. Names of people in the format
"John Dow" first and second name. Find those who are on all blacklists.
"""
casino_blacklist = {'Yennefer of Vangerberg', 'Lutic Pankratz', 'Triss Merigold'}
poker_blacklist = {'Triss Merigold', 'Lutic Pankratz', 'Geralt of Rivia'}
alcohol_blacklist = {'Geralt of Rivia', 'Lutic Pankratz', 'Triss Merigold'}
print(casino_blacklist.intersection(poker_blacklist, alcohol_blacklist))

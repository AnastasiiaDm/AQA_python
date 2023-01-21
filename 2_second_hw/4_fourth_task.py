"""
You have two groups of people. One group consists of omnivores, the other only vegetarians. An omnivore is a vegetarian
but a vegetarian is not an omnivore. Display a list of guests who can eat vegetables and herbs.
"""
omnivores = {'Geralt of Rivia', 'Lutic Pankratz', 'Triss Merigold'}
vegetarians = {'Yennefer of Vangerberg', 'Triss Merigold'}

vegetables_and_herbs_guests = vegetarians.union(omnivores)
print(vegetables_and_herbs_guests)

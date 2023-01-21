"""
You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba. Show it in code.
Keep in mind that people with the same name can be in both companies
"""
eleks = ['Geralt', 'Triss', 'Lutic']
toshiba = ['Yennefer', 'Ciri', 'Vesemir', 'Geralt']
toshiba.extend(eleks)
eleks.clear()
print(toshiba)
print(eleks)

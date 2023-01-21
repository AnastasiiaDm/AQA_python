"""
1. Create variables john_salary and marta_salary of some type (floating point). Assign the created variables the values
 you want. Print the values of both variables to the console using the print method.
"""
john_salary = 1000.00
geralt_salary = 1500.00
lutic_salary = 3000.00
marta_salary = 2000.00
ciri_salary = 500.00
yennefer_salary = 4000.00

print(john_salary)
print(marta_salary)

"""
2. Create variables john_age and marta_age of integer type. Assign the created variables the values you want. 
Print the values of both variables to the console using the print method.
"""
john_age = 20
geralt_age = 99
lutic_age = 43
marta_age = 30
ciri_age = 16
yennefer_age = 95

print(john_age)
print(marta_age)

"""
3. Create string type variables john_name and marta_name. Assign the created variables the values you want. 
Print the values of both variables to the console using the print method.
"""

john_name = 'John'
geralt_name = 'Geralt'
lutic_name = 'Lutic'
marta_name = 'Marta'
ciri_name = 'Ciri'
yennefer_name = 'Yennefer'

print(john_name)
print(marta_name)

"""
4. Create boolean variables john_gender and marta_gender. Let john be false and Marta be true. Print the values of both 
variables to the console using the print method.
"""
john_gender = False
geralt_gender = False
lutic_gender = False
marta_gender = True
ciri_gender = True
yennefer_gender = True

print(john_gender)
print(marta_gender)

"""
5. Create variables john_friends and marta_friends. Assign lists to variables. Each list must contain the names of 
friends. John has his list of friends and Martha has hers. Friends (friend's name) can be the usual strings "James", 
"Peter", etc.
"""

john_friends = ['Geralt', 'Triss', 'Lutic']
geralt_friends = ['Zoltan', 'Lutic']
lutic_friends = ['Geralt']
marta_friends = ['Yennefer', 'Ciri', 'Vesemir']
ciri_friends = ['Dara', 'Triss']
yennefer_friends = ['no friends']

"""
6. Create a list with people's names, some names should be repeated in it. Turn a list of duplicate names into a list 
of unique names using sets.
"""
repeated_name_list = ['Geralt', 'Triss', 'Lutic', 'Geralt']
name_set = set(repeated_name_list)

"""
7. Create 2 tuple variables. The tuple must consist of 2 floating point numbers. The first value of the tuple is the 
latitude where you live, and the second value is the longitude where you live.
"""
my_live_latitude = (46.4902944)
my_live_longitude = (30.7117686)
geralt_coordinates = (76.7676858, 85.7575858)
lutic_coordinates = (58.77497464, 47.758574)
ciri_coordinates = geralt_coordinates
yennefer_coordinates = (74.848484, 94.7478494)

"""
8. Create 2 variables john, marta. Variables must be dictionaries with keys: full_name, age, salary, gender, friends, 
coordinates.
"""
# john_coordinates = (10.775885854, 78.95959969)
john = {
    'full_name': john_name,
    'age': john_age,
    'salary': john_salary,
    'gender': john_gender,
    'friends': john_friends,
    'coordinates': (10.775885854, 78.97695759)
}

for key in john:
    print(key + ' => ' + str(john[key]))

marta = {
    'full_name': marta_name,
    'age': marta_age,
    'salary': marta_salary,
    'gender': marta_gender,
    'friends': marta_friends,
    'coordinates': (49.76868694, 65.75894947)
}

for key in marta:
    print(key + ' => ' + str(marta[key]))

"""
Task from point 8. Instead of strings in the list of friends, there should be the same dictionaries as john and marta. 
Create 2 friends each for John and Martha. Print John and Martha's fields to the console.
"""
geralt = {
    'full_name': geralt_name,
    'age': geralt_age,
    'salary': geralt_salary,
    'gender': geralt_gender,
    'friends': geralt_friends,
    'coordinates': geralt_coordinates
}

lutic = {
    'full_name': lutic_name,
    'age': lutic_age,
    'salary': lutic_salary,
    'gender': lutic_gender,
    'friends': lutic_friends,
    'coordinates': lutic_coordinates
}

ciri = {
    'full_name': ciri_name,
    'age': ciri_age,
    'salary': ciri_salary,
    'gender': ciri_gender,
    'friends': ciri_friends,
    'coordinates': ciri_coordinates
}

yennefer = {
    'full_name': yennefer_name,
    'age': yennefer_age,
    'salary': yennefer_salary,
    'gender': yennefer_gender,
    'friends': yennefer_friends,
    'coordinates': yennefer_coordinates
}

john['friends'] = [geralt, lutic]
print(john)

marta['friends'] = [ciri, yennefer]
print(marta)

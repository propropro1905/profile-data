import random
def import_data_from_file(filename):
    text_file = open(filename, "r")
    temp = text_file.read().splitlines()
    text_file.close()
    return temp
# load name
female_names = import_data_from_file("./data/name/female.dat")
male_names = import_data_from_file("./data/name/male.dat")
lastnames = import_data_from_file("./data/name/lastname.dat")
cities = import_data_from_file("./data/location/city.dat")
occupations = import_data_from_file("./data/occupation.dat")
print(random.choice(lastnames) + " " + random.choice(female_names))

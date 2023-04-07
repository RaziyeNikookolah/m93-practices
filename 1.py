import re

def capital_space(string):
    return re.sub(r'\S([A-Z])','r \1',string)

print(capital_space("Maktab"))
print(capital_space("TheFirstProgrammingBootcamp"))
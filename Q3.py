def code(modulecode):
    switcher={
        "CSC1009":"Object Oriented Programming",
        "CSC1010":"Computer Networks",
        "CSC1008":"Data Structures and Algorithms",
        "CSC1007":"Operating Systems",
        "CSC1006":"Mathematics 2"
    }
    return switcher.get(modulecode, "Unknown Module")

print(code("CSC1009"))

for i in range(102, 66, -1):
    if(i % 2 == 1):
        print(i)
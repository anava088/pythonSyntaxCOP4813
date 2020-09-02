message = "Hello COP 4813"

print(message)

first_name = "Greg"

print("My name ", len(first_name), "letters.")

print(first_name.lower())
print(first_name.title())
print(first_name.upper())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

a = 2
b = 5

c = a + b
print(c)

c = b - a
print(c)

c = b * a
print(type(c))

c = b / a
print(type(c))

c = b // a
print(type(c))

print(10/2)

professors = ["greg", "leonardo", "giri"]
print(professors,len(professors),type(professors))

print(professors[0])

for i in professors:
    print(i.title())


print(professors[-3])
professors.append("Micheal")
print(professors)
print(professors[0:2]) # I am getting elements 0  and 1
print(professors[0:2]) # I am also accessing elements 0 and 1
print(professors[1:3]) # I am acessing elements 1 and 2
print(professors[2:]) #Acessing elements 2 and 3

for j,k in enumerate(professors):
    print(j,k)

#functions, for loops if statements, classes need the :
print(professors.index("greg"))

#print(professors.index("Cowboy")) # trying to acess an element that is not in the list

professors.sort()
print(professors)
professors.sort(reverse=True)
print(professors)

for m in range(1,10,2):  #10 = 0-9 2,10 = 2-9 1,10,2 = skip by 2
    print(m)

released_date = {
    "iphone":2007,
    "iphone4":2010,
    "iphone7":2016,
    "iphonex":2017,

}
print(released_date)
print(released_date["iphone7"])
for i in released_date.keys():
    print(i)
for k in released_date.values():
        print(k)
for key,element in released_date.items():
        print(key,element)
print(len(released_date))
capitals ={}
print(capitals)

capitals["USA"]="DC"
capitals["Lithuania"]="Wilnus"
capitals["Colombia"]="Bogota"
capitals["Brazil"]="Brasilia"
capitals["Peru"]="Lima"
capitals["Argentina"]="Buenos Aires"

countries = ["France","Lebanon","USA","Brazil","Colombia"]
print(type(capitals),type(countries))

for i in countries: #elements of the list
    if i in capitals: #trying to see if an element of the list is in the dictionary
        print("The capital of",i,"is",capitals[i])
    else:
        print("Unknown capital!")
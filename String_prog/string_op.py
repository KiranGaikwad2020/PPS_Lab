#This program demosntrates the string operations

city=input("\n Enter the name of city: ")
state=input("\n Enter the name of state: ")
print("\n Your city is {}".format(city))
print("\n Your state is {}".format(state))
citystate = city+state
print("\n The concatenation of city and state strings is: {}".format(citystate))
print("\n Length of concatenated string is: {}".format(len(citystate)))
print("\n Converted the citystate string to Upper Case as: {}".format(citystate.upper()))
print("\n Converted the citystate string to Lower Case as: {}".format(citystate.lower()))



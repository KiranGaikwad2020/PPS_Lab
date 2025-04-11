class Sample:
    def __init__(self):
        self.num1 = 10  # Instance variable with a default value

    def getdata(self):
        self.num1 = int(input("\n Enter the value: "))  # Store input in instance variable

    def printdata(self):
        print("\n Entered value is {}".format(self.num1))  # Use self.num1


# Create objects
obj1 = Sample()
obj2 = Sample()

# Call methods
obj1.getdata()
obj1.printdata()
obj2.printdata()  # obj2 still has the default value 10

	
	

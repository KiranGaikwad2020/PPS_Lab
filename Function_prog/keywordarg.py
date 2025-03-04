num1=int(input("\n Enter the first number"))
num2=int(input("\n Enter the second number"))
def add(num1,num2):
	return num1+num2

result=add(num1=45,num2=5)
result1=add(num1,num2)
print("\n Addition with keyword arguments is : {}".format(result))
print("\n Addition without keyword arguments is : {}".format(result1))



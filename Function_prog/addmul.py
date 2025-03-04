#This program demosntrates the function use
num1=int(input("\n Enter the first number"))
num2=int(input("\n Enter the second number"))
def addmul(a,b):
	return a+b,a*b
add,mul=addmul(num1,num2)
print("\n Addition of two numbers {} and {} is : {}".format(num1,num2,add))
print("\n Multiplication of two numbers {} and {} is : {}".format(num1,num2,mul))


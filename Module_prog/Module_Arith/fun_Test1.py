#This program demosntrates the Function with multiple return values

Pi=3.14

def add():
	num1=int(input("\n Enter the First number: "))
	num2=int(input("\n Enter the Second number: "))
	add=num1+num2
	print("\n Addition of {} and {} is {}".format(num1,num2,add))
	
	
def sub():
	num1=int(input("\n Enter the First number: "))
	num2=int(input("\n Enter the Second number: "))
	sub=num1-num2
	print("\n Subtraction of {} and {} is {}".format(num1,num2,sub))


def mul():
	num1=int(input("\n Enter the First number: "))
	num2=int(input("\n Enter the Second number: "))
	mul=num1*num2
	print("\n Subtraction of {} and {} is {}".format(num1,num2,mul))


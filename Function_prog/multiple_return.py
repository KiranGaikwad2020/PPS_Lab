#This program demosntrates the Function with multiple return values

def function1(a,b):
	return a+b,a*b
	
num1=int(input("\n Enter the First number: "))
num2=int(input("\n Enter the Second number: "))
add,mul=function1(num1,num2)
print("\n Addition of {} and {} is {}".format(num1,num2,add))
print("\n Multiplication of {} and {} is {}".format(num1,num2,mul))

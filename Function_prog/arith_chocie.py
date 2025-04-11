#This program demonstrates the use of arithemtical operations using function choice
num1=int(input("\n Enter the first number"))
num2=int(input("\n Enter the second number"))
def add(num1,num2):
	return (num1+num2)
	
def sub(num1,num2):
	return (num1-num2)
	
def mul(num1,num2):
	return (num1*num2)
	
def div(num1,num2):
	return (num1//num2)

print("\n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division")
choice=int(input("\n Enter your choice :"))
if (choice==1):
	result=add(num1,num2)
	print("\n Addition of {} and {} is {}".format(num1,num2,result))
elif (choice==2):
	result=sub(num1,num2)
	print("\n Substraction of {} and {} is {}".format(num1,num2,result))
elif (choice==3):
	result=mul(num1,num2)
	print("\n Multiplication of {} and {} is {}".format(num1,num2,result))
elif (choice==4):
	result=div(num1,num2)
	print("\n Division of {} and {} is {}".format(num1,num2,result))
else:
	print("\n Wrong choice")
	


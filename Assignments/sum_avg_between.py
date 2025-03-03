#This program demostrates the sum and average of numbers in between given two numbers
num1=int(input("\n Enter the start number: "))
num2=int(input("\n Enter the end number: "))
sum=0
for i in range(num1,num2):
	sum=sum+i
print("\n Sum of numbers in between {} and {} is : {}".format(num1,num2,sum))
avg=sum/len(range(num1,num2))
print("\n Average of numbers in between {} and {} is: {}".format(num1,num2,avg))

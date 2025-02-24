#This program demosntrates the sum of the digits of given number
number=int(input("\n Enter the input number"))
sum=0
orig_num=number
while number!=0:
	temp=number%10
	sum=sum+temp
	number=number/10

print("\n Sum of digits in given number {} is : {}".format(orig_num,int(sum)))

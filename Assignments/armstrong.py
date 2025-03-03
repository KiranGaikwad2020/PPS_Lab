#This program demonstrates the armstrong number validation

num=int(input("\n Enter the number: "))
orig_number=num
sum=0
digits=len(str(num))
print("\n Length of the entered number is ", + digits)
while num > 0:
	digit=num%10
	sum=sum+(digit**digits)
	num=num//10
if(sum==orig_number):
	print("\n Entered number {} is armstrong number".format(orig_number))
else:
	print("\n Entered number {} is not armstrong number".format(orig_number))

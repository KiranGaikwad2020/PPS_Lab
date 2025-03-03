#This program demonstrates the multiplication table"
number=int(input("\n Enter the number of which multiplication table to be generated"))
i=1
print("\n Multiplication table of {} is as follows:".format(number))
while i<=10:
#	table=i*number
	print("\n {} x {} = {}".format(number,i,(i*number)))
	i=i+1
	
	

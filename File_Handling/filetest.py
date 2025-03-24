#This program demosntrates the file handling operations

#1. Open()
def openfiletest():
	filept=open("/home/comp625/test.py","r")
	if(filept!=0):
		print("\n File is opened in read mode and original contents are \n")
		print("***********************************************************")
		print(filept.read())
		print("***********************************************************")
		filept.close()
	else:
		print("\n File is not opened in read mode")
	
	
#2. Close()
def closefiletest():
	fileopt=open("/home/comp625/vote2.py","r+")


#	fileinput=input("\n Enter the name of file alongwith file extesnion")
#	fileopt=open("fileinput","r+")
	if(fileopt!=0):
		print("\n File is opened in Read & Write Mode")
		print("\n Original Contenetns of the file are \n")
		print("*********************************************")
		print(fileopt.read())
		print("*********************************************")
		print("\n File is updating with writing single line: #This is added line")
		fileopt.write("#This is added line")
		fileopt.close()
	else:
		print("\n File is not opened for the operation")
	fileopt=open("/home/comp625/vote2.py","r")
	print("\n File is opened after write operation performed")
	print("*****************************************************************")
	print(fileopt.read())
	print("******************************************************************")
	fileopt.close()
	
#openfiletest()			
closefiletest()

#This program demosntrates the temprature conversion

temp_far=float(input("\n Enter the temperature in farheneit"))
print("\n Converting given farheneit temprature into celcius")
temp_celc=round((temp_far-32)*float(5/9),2)
print("\n Given Temperature in farheneit is {}.And it's conversion into celcious is {}".format(temp_far,temp_celc,".2f"))

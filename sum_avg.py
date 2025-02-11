#This program demonstrates the addition and average of first 10 numbers:
# Generating the first 10 natural numbers
numbers = list(range(1, 11))
print("\nGeenrated list using range function is of first 10 numbers as follows: \n")
print(numbers)
# Calculating the sum
total_sum = sum(numbers)
# Calculating the average
average = total_sum / len(numbers)
# Displaying the results
print("\nSum of first 10 numbers: ", total_sum)
print("\nAverage of first 10 numbers: ", average)

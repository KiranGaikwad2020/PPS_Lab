#This program demonstrate string operations in python

def string_operations():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string (for equality check & substring check): ")
    
    # i. Calculate length of string
    print(f"Length of the first string: {len(str1)}")
    
    # ii. String reversal
    reversed_str = str1[::-1]
    print(f"Reversed string: {reversed_str}")
    
    # iii. Equality check of two strings
    if str1 == str2:
        print("Both strings are equal.")
    else:
        print("Strings are not equal.")
    
    # iv. Check palindrome
    if str1 == reversed_str:
        print("The first string is a palindrome.")
    else:
        print("The first string is not a palindrome.")
    
    # v. Check substring
    if str2 in str1:
        print(f"'{str2}' is a substring of '{str1}'.")
    else:
        print(f"'{str2}' is not a substring of '{str1}'.")

# Run the function
string_operations()




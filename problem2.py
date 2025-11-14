#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
You may need to use the:
print( variable , end='') option to print on one line
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""

n = float(input("Enter a number:"))

print(n*1,n*2,n*3,n*4,n*5,n*6,n*7,n*8,n*9,n*10,n*11,n*12)
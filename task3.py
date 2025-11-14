#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

Number=""

even=False

while not even:
    Number = float(input("Enter number: "))
    if Number %2 == 0:
         even = True
    else:
        print("Not an even integer")
print("That number is an even integer")
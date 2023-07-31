"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab01 - Q2
"""

num1 = int( input( "Enter the first integer: " ) )
num2 = int( input( "Enter the second integer: " ) )
num3 = int( input( "Enter the third integer: "  ) )


# Solution 1
print( "The sorted nums are:" )

if num1 > num2:
    if num3 > num2:
        print( num2 )
        if num3 > num1:
            print( num1 )
            print( num3 )
        else:
            print( num3 )
            print( num1 )
    else: 
        print( num3 ) 
        print( num2 )
        print( num1 )
else:
    if num3 > num1:
        print(num1)
        if num2 > num3:
            print( num3 )
            print( num2 )
        else:
            print( num2 )
            print( num3 ) 
    else: 
        print( num3 )
        print( num1 )
        print( num2 )




# Solution 2
if num2 > num3:
    num2, num3 = num3, num2

if num1 > num2:
    num1, num2 = num2, num1

print( "The sorted nums are:", num1, num2, num3 )
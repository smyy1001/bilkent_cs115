"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab02 - Q2
"""

sumNumbers = 0
count = 0

lower = int( input( "Enter lower bound: " ) )
upper = int( input( "Enter upper bound: " ) )

if lower < upper:
    for i in range( lower, upper + 1 ):
        if i % 7 == 0 and i % 5 != 0:
            sumNumbers += i
            count += 1

    if count != 0:
        average = sumNumbers / count
        print( count, "values are divisible by 7 but not 5 between", lower, "and", upper, "inclusive" )
        print( "Average Value is ", average )

    else:
        print( "No values found!" )
else:
    print( "Invalid range!" )

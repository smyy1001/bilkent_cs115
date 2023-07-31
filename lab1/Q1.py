"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab01 - Q1
"""
import math

a = int( input( "Enter coefficient of x2: " ) )
b = int( input( "Enter coefficient of x : " ) )
c = int( input( "Enter constant term    : " ) )

d = b*b - 4 * a * c

if d > 0:
    r1 = ( -b - math.sqrt( d ) ) / ( 2 * a )
    r2 = ( -b + math.sqrt( d ) ) / ( 2 * a )
    print( "Roots are: {0:.2f} {1:.2f}".format( r1,r2 ) )
else:
    print( "No real roots found!" )

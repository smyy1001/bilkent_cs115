"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab02 - Q1
"""

s = input(" Enter a string: ")

mid_index = len(s)//2

if len(s) >= 4:   
    s1 = s[mid_index:] + s[0:mid_index]

else:
    s1 = s[mid_index:] + s[0:mid_index] 
    s1 += ("_" * (4-len(s)))

print( s1 )

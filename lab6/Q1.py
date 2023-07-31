"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab06
"""


def max_chars( t ):
    max_counts = []    
    
    for col in range( len( t[0] )  ):
        max_count = 0

        for row in range( len( t ) ):
            if len( t[row][col] ) > max_count:
                max_count = len( t[row][col] )

        max_counts.append( max_count )

    return max_counts


def read_words( rows, cols ):
    table = []

    for r in range( rows ):
        row = []

        for c in range( cols ):
            row.append( input( "Enter word into " + str(r+1) + "," + str(c+1) + ": " ) )

        table.append(row)

    return table




# Test
table = read_words( 3, 4 )
print( "Words:", table )
print( "Max Length of words in each column: ", max_chars( table ) )

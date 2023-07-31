"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab01 - Q3
"""

val = int( input("Enter a positive integer: " ) )
result = 0

if val > 0:
    units = input("Enter the unit of the value ( bit/byte/kilobyte ): " )
    
    if units == "bit":
        convert_to = input( "What unit do you want to convert the value ( bit/byte/kilobyte ): " )

        if convert_to == "byte":
            result = val / 8
            
        elif convert_to == "kilobyte":
            result = val / ( 8 * 1024 )
            
        elif convert_to == "bit":
            print( "No conversion necessary" )
            
        else:
            print( "Invalid conversion unit" )
            
    elif units == "byte":
        convert_to = input( "What unit do you want to convert the value ( bit/byte/kilobyte ): " )

        if convert_to == "bit":
            result = val * 8
            
        elif convert_to == "kilobyte":
            result = val / 1024
        
        elif convert_to == "byte":
            print( "No conversion necessary" )
            
        else:
            print( "Invalid conversion unit" )
            
    elif units == "kilobyte":
        convert_to = input( "What unit do you want ( bit/byte/kilobyte ): " )

        if convert_to == "bit":
            result = val * 1024 * 8
            
        elif convert_to == "byte":
            result = val * 1024
        
        elif convert_to == "kilobyte":
            print( "No conversion necessary" )
            
        else:
            print( "Invalid conversion unit" )
        
    else: # unit of the entered value is not bit, byte or kilobyte
        print( "Invalid Unit" )

else: # entered an non-positive integer
    print( "Units must be positive" )


if result != 0: # if the result is calculated
    print( val, units, "is equal to", result, convert_to )
    # ...  bit/byte/kilobyte  is equal to  ...  bit/byte/kilobyte
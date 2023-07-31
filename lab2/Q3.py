"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab02 - Q3
"""

TENNISBALL = 0.7
BASKETBALL = 0.75
SUPERBALL = 0.9
SOFTBALL = 0.3

ballType = input( "Enter Ball Type: " ).lower(  )

while ballType != 'exit':

    coefficient = 0

# determine coefficient
    if ballType == "tennis ball":
        coefficient = TENNISBALL

    elif ballType == "basket ball":
        coefficient = BASKETBALL

    elif ballType == "super ball":
        coefficient = SUPERBALL

    elif ballType == "soft ball":
        coefficient = SOFTBALL

    else:
        print( "Invalid Ball Type..." )



    if coefficient > 0:
        totalHeight = 0

        # input height
        initialH = float( input( "Enter initial height( m ): " ) )

        # convert height to cm
        height = initialH * 100
        totalHeight = height

        bounces = 1

        height = height * coefficient

        while height >= 10:
            bounces += 1
            totalHeight += height * 2
            height = height * coefficient

        print( "Number of bounces:", bounces )
        print( f"Meters traveled: {totalHeight/100.0:.2f}" )

    ballType = input( "Enter Ball Type: " )

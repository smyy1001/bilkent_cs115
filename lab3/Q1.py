"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab03
"""


def count_letter( c, word ):
    count = 0
    for ch in word:
        if ch == c:
            count += 1
    return count


def convert_word( word ):
    count = 0
    new_w = ""
    for ch in word:
        if not ch.isalpha():
            new_w += "*"
        else: 
            count = count_letter( ch.lower(), word.lower())
            if( count != 1 ):
                new_w += ")"
            else:
                new_w += "("
    return new_w
            

def same_birthday( d ):
    probab = 1
    for i in range(1, d + 1):
        probab = probab * ( ( 365 - i ) / 365 )
    probab = 1 - probab
    return probab


def display_menu():
    print( "1 - Convert Word" )
    print( "2 - Same Birthday" )
    print( "3 - Exit" )


def get_choice():
    display_menu()
    choice = int( input( "Input choice: " ) )
    return choice


# Test
choice = get_choice()
while choice != 3:

    if choice == 1:
        word = input( "Enter word to convert: " )
        converted = convert_word( word )
        print( f"\original: {word} converted: {converted}\n" )

    elif choice == 2:
        size = int( input( "Enter group size: " ) )
        if size > 0:
            prob = same_birthday( size )
            print( f"The probab of two people in a group of {size} having the same birthday: {prob*100:.1f}" )
        else:
            print( "The group size must be positive" )

    else:
        print("Invalid choice")

    # again
    choice = get_choice()

print("Goodbye...")

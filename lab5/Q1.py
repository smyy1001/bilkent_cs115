"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab05
"""


def read_restaurants( fileName ):
    restaurants = {}
    data = open( fileName,'r' )
    count = 5

    for i in range( count, 0, -1 ):
        r = data.readline().strip()
        rest_list = r.split(",")
        rating = i * "*"
        restaurants[rating] = rest_list
    data.close()

    return restaurants


def display_restaurants( restaurants ):
    for i in restaurants:
        print( f"{i.strip():8s}: ", end="" )

        for j in restaurants[i]:
            print( f"{j.strip()}", end=" " )
        print()




# Test
menu = "1) Find by Restaurant\n2) Find by Rating\n3) Add Rating"
menu+= "\n4) Display Restaurants \n5) EXIT\nChoice: "

choice = int( input( menu ) )

restaurants = read_restaurants( "restaurants.txt" )

while choice != 5:
    if choice == 1:
        rest_name = input( "Enter restaurant name: " )

        for rating in restaurants:
            for rest in restaurants[rating]:
                if rest == rest_name:
                    print( f"{rest_name} has {len(rating)} stars" )

    elif choice == 2:
        rating = input( "Enter rating to search: " )
        print( f"Restaurants with {len(rating)} stars:" )

        if rating in restaurants:
            rest_list = restaurants[rating]
            for rest in rest_list:
                print( rest, end=" " )
    
    elif choice == 3:
        rest_name = input( "Enter restaurant name: " )
        rating = input( "Enter restaurant rating: " )
        if rest_name not in restaurants[rating]:
            restaurants[rating].append(rest_name)

    elif choice == 4:
        display_restaurants(restaurants)

    else:
        print( "Invalid choice" )

    # again
    choice = int( input( menu ) )

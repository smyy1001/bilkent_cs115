"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab04
"""

import order

customer = input( "Enter customer name to search (exit to quit): " ).lower()

while customer != "exit":
    order_id = order.find_order( "customers.txt", customer )

    if order_id != -1:
        (items, total) = order.find_order_items( "orders.txt", order_id )
        
        if len(items) > 0:
            print( "Order Summary: " )
            print( items )
            print( "Total Order Price: ", total )
            outfile = open( str( order_id )+".txt", 'a' )
            outfile.write( customer + "\t" + str( total ) + "\n" )
            outfile.close()

        else:
            print( "Order Not Found!" )

    else:
        print( "Customer Not Found!" )

    customer = input( "Enter customer name to search (exit to quit): " )
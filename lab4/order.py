"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab04
"""

def find_order_items( o_file, order_id ):
    total = 0.0
    items = ""
    inFile = open(o_file, 'r')

    for line in inFile:
        if line[:len(order_id)] == order_id:
            price_index = line.rfind(';')
            total += float(line[price_index+1:])
            item_pos = line.find(';')
            items += line[item_pos+1:price_index] + '\n'

    return items,total


def find_order( c_file, cname ):
    inFile = open(c_file,'r')

    for line in inFile:
        id_pos = line.find(',')
        
        if line[id_pos+1:].strip().lower() == cname.strip().lower():
            return line[0:id_pos]
        
    return -1

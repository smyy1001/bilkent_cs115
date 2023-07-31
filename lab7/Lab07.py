# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:54:56 2019

@author: b
"""

import Vehicle as v

def read_vehicles( filename ):
    in_file = open(filename,'r')
    v_list = []
    
    for line in in_file:
        line = line.strip()
        data = line.split(',')
        if data[0] == 'B':
            vehicle = v.Bus(data[1],float(data[2]), int(data[3]),int(data[4]))
        elif data[0] == 'C':
            vehicle = v.Car(data[1],float(data[2]), int(data[3]),data[4], data[5])
    
        else:
            vehicle = v.Vehicle(data[1],float(data[2]), int(data[3]))
        
        v_list.append(vehicle)
    return v_list

v_list = read_vehicles('vehicles.txt')
print(v_list)

total = 0
c_code = input('Enter code of city to search: ')

for vehicle in v_list:
    city = vehicle.get_plate_no()[0:2]
    #if type(vehicle) == v.Car and city == c_code:
    if isinstance(vehicle, v.Car) and city == c_code:
        print(vehicle)
    total += vehicle.get_year()

avg_year = total // len(v_list)
print('Average year of all vehicles:',avg_year)
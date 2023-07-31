"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab06
"""

from Lab06Flight import  *


flightList = []

#create 4 flights and add the flights to the list
flightList.append( Flight( "TK1234", "Ankara",   "Antalya", 250 ) )
flightList.append( Flight( "LH8686", "Munich",   "Tokyo",   290 ) )
flightList.append( Flight( "TK9897", "Istanbul", "Paris",   195 ) )
flightList.append( Flight( "TK5432", "Antalya",  "Ankara",  250 ) )

print("Original List: ")
print(flightList)

#sort the list 
flightList.sort()

print("Sorted List: ")
print(flightList)

#total operating cost
totalCost = 0.0
for current in flightList:
	#get the operating cost of the flight add to the total
	totalCost += current.calculateOperatingCost()

#display the total cost
print( "Total Operating Cost: " + str( totalCost ) )

#Display the flight whose destination is Tokyo
for flight in flightList:
	if flight.getDestination() == "Tokyo":
		print("\n\n"+str(flight))
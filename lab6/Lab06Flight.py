"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab06
"""


class Flight:
    __flightOperatingCost = 150  
        
    def __init__( self, num,  dep,  dest,  cap):
        self.__flightNo = num
        self.__destination = dest
        self.__departure = dep
        self.__capacity = cap    
    

    def  setCapacity( self, cap):
        if(cap > 0):
            self.__capacity = cap

    def  getCapacity(self):
        return self.__capacity
    


    def  setFlightNo( self, num):
        self.__flightNo = num
    
    def  getFlightNo(self):
        return self.__flightNo
    


    def  setDeparture( self, dep):
        self.__departure = dep
    
    def  getDeparture(self):
        return self.__departure
     


    def  setDestination( self, dest):
        self.__destination = dest
    
    def  getDestination(self):
        return self.__destination
    


    def  calculateOperatingCost(self):
        return self.__capacity * Flight.__flightOperatingCost
    
    def  __repr__(self):
        flight = "\nFlight Number: " + self.__flightNo + "\nDeparting From: "
        flight += self.__departure+"\nArriving To: " + self.__destination
        flight += "\nSeats: " + str(self.__capacity) + "\n" 
        return flight
    
    def __lt__(self, other):
        return self.__flightNo < other.__flightNo

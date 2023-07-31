"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab07
"""

#parent
class Vehicle:   

    def __init__( self, plate_no, price, year ):
        self.__price = price
        self.__year = year
        self.__plate_no = plate_no


    def get_plate_no( self ):
        return self.__plate_no
    
    def set_plate_no( self, plate ):
        self.__plate_no = plate



    def get_price( self ):
        return self.__price
    
    def set_price( self, price ):
        self.__price = price
    


    def get_year( self ):
        return self.__year
    
    def set_year( self, year ):
        self.__year = year
    


    def __repr__( self ):
        return "\nVehicle " + self.__plate_no + "\n" + "Price: " + str( self.__price ) +  \
        " (" + str( self.__year ) + ")\n"
        


#sub class
class Car(Vehicle):   

    def __init__( self, plate_no, price, year, brand, model ):
        Vehicle.__init__( self, plate_no, price, year ) #super
        self.__brand = brand
        self.__model = model
    


    def get_brand( self ):
        return self.__brand
    
    def set_brand( self, brand ):
        self.__brand = brand


    
    def get_model( self ):
        return self.__model
    
    def set_model( self, model ):
        self.__model = model
    


    def __repr__( self ):
        return "\n" + Vehicle.__repr__(self) + self.__brand + "(" + self.__model + ")\n"



#sub class
class Bus( Vehicle ):

    def __init__( self, plate_no, price, year, seats ):
        Vehicle.__init__( self, plate_no, price, year ) #super
        self.__seats = seats
    

    def get_seats( self ):
        return self.__seats
    
    def set_seats( self, seats ):
        self.__seats = seats 
    

    def find_type( self ):

        if self.__seats >= 40:
            return "Full Size Bus"
        
        elif self.__seats >= 20:
            return "Midibus"
        
        else:
            return "Minibus"


    def __repr__( self ):
        return  "\n" + self.find_type() + " " + str( self.get_price() ) + "\n"
        
    
        
        
        

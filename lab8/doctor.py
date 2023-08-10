"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab08
"""


class Doctor:
    
    def __init__( self, dId, dName, dSpec, hosp ):
        self.__doctorId = dId
        self.__doctorName = dName
        self.__specialty = dSpec
        self.__hospital = hosp
    

    def getDoctorId( self ):
        return self.__doctorId
    

    def setDoctorId( self, dId ):
        self.__doctorId = dId
    

    def getDoctorName( self ):
        return self.__doctorName
    
    def setDoctorName( self, dName ):
        self.__doctorName = dName
    
 
    def getSpecialty( self ):
        return self.__specialty
    
    def setSpecialty( self, dSpec ):
        self.__specialty = dSpec
    

    def getHospital( self ):
        return self.__hospital

    def setHospital( self, hosp ):
        self.__hospital = hosp
    
    def __repr__( self ):
        return self.__doctorId + ' ' + self.__doctorName + ' ' + self.__specialty + ' ' + self.__hospital
    
    def __eq__( self, other ):
        return self.__doctorId == other.__doctorId

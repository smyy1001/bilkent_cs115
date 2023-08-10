"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab08
"""


from doctor import Doctor

def selectionSort( data ):
    suffixStart = 0
    while suffixStart != len(data):
        for i in range( suffixStart, len(data) ):
            if data[i].getSpecialty() < data[suffixStart].getSpecialty():
                data[suffixStart], data[i] = data[i], data[suffixStart]
            elif  data[i].getSpecialty() == data[suffixStart].getSpecialty():
                if data[i].getDoctorName() < data[suffixStart].getDoctorName():
                    data[suffixStart], data[i] = data[i], data[suffixStart]
        suffixStart += 1

def searchDoctors( data, hosp, endInd ):
    if( endInd == -1 ):
        return []
    elif data[endInd].getHospital() == hosp:
        searchRes = searchDoctors( data, hosp, endInd-1 )
        searchRes.append( data[endInd] )
        return searchRes
    else:
        return ( searchDoctors( data, hosp, endInd-1 ) )
    
    
def readDoctors( fileName, doctors ):
    dFile = open( fileName,'r' )
    for line in dFile:
        data = line.strip().split( ';' )
        dId = data[0]
        dName = data[1]
        dSpec = data[2]
        hosp = data[3]
        doctors.append( Doctor( dId, dName, dSpec, hosp ) )
    dFile.close()


# build a list of doctors
doctors = []
readDoctors( "doctors.txt", doctors )

# search for doctors in a specified hospital
hosp = input( "Enter hospital to search: " )
matches = searchDoctors(doctors, hosp, len(doctors)-1)
if len( matches ) != 0:
    print( "List of Doctors at", hosp )
    for doc in matches:
        print( doc )
else:
    print( "No doctors in that hospital" )


# sorted the doctors list according to their specialty and name
selectionSort( doctors )
print( "\nDoctors by specialty and name: " ) 
for doctor in doctors:
    print( doctor )


# add a new doctor to the list if she/he is not already in the list
doctorInfo = input( "Enter Doctor ID, name, specialty and her/his hospital: " )
info = doctorInfo.strip().split( ',' )
newDoc = Doctor( info[0].strip(), info[1].strip(), info[2].strip(), info[3].strip() )
if newDoc not in doctors:
    doctors.append( newDoc )
    print( "New doctor added" )
else:
    print( "Doctor exists" )
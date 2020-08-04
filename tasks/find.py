from csvoperations import csvReader

def findCollege(op):

    if op=='2':
        csvReader.prefDetails()
    elif op=='3':
        print("Enter Parameters")
        course = input("Course: ")
        city = input("City: ")
        csvReader.prefDetails(course, city)
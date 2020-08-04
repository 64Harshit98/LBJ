from classes import collegeModule

# function for registering college
def collegeDetails():

    print("Enter College Details")

    collegeId = input(" ID : ")

    collegeName = input(" Name: ")

    courseType = input(" Course : ")

    city = input(" City : ")

    fees = input(" Fees : ")

    pincode = input(" Pincode : ")

    collegeObj = collegeModule.College(collegeId, collegeName, courseType, city, fees, pincode)
    collegeObj.collegeRegister()
    
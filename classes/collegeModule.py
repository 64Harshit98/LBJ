from csvoperations import csvWriter

class College: 
    def __init__(self, collegeId, collegeName, courseType, city, fees, pincode):
        self.collegeId = collegeId
        self.collegeName = collegeName
        self.courseType = courseType
        self.city = city
        self.fees = fees
        self.pincode = pincode

    def collegeView(self):
        print(self.collegeName)

    # function for saving college details in csv 
    def collegeRegister(self):
        
        # adding valuesin details list
        details = []
        details.append(self.collegeId)
        details.append(self.collegeName)
        details.append(self.courseType)
        details.append(self.city)
        details.append(self.fees)
        details.append(self.pincode)

        # saving in college.csv
        csvWriter.saveDetails(details)
    
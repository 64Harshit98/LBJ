import csv

# Field Names in csv
# fields = ['ID', 'Name', 'Course', 'City', 'Fees', 'Pincode']

# function to save values in cs file
def saveDetails(details):
    # Name of CSV file
    filename = "csvoperations/colleges.csv"

    # csvfile object
    with open(filename, 'a+', newline='') as csvfile:

        # Creating a writer object
        csvwriter = csv.writer(csvfile)

        # Writing the data in csv
        csvwriter.writerow(details)

        print('College details saved!!!')
        print(details)
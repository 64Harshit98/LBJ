import csv

# Name of CSV file
filename = "csvoperations/colleges.csv"

# for deleting the college detail with given id
def deleteDetails():
    id = input("Please Enter Id of College to be deleted: ")
    # opening the document
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        temp = []
        temprow = ""
        i=0
        for row in csvreader:
            if row[0]!=id:
                temp.insert(i, row)
                i+=1
            elif row[0]==id:
                temprow = row
                i+=1
        if temprow:
            # csvfile object
            with open(filename, 'w', newline='') as csvfile:

                # Creating a writer object
                csvwriter = csv.writer(csvfile)

                # Writing the data in csv
                csvwriter.writerows(temp)
                print(temprow)
                print('College details deleted!!!')
        else:
            print("College Not Found!!!")
        
import csv

# Name of CSV file
filename = "csvoperations/colleges.csv"

# for reading data 
def readDetails():
    # opening the document
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        line = 0
        for row in csvreader:
            print(row)
            line += 1
        print(f'Processed {line} lines.')

# for reading values with given values
def prefDetails(course='Engineering', city='Mumbai'):
    # opening a document
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        record = 0
        for row in csvreader:
            if (row[2]==course and row[3]==city):
                print(row)
                record+=1
        if record<2:
            print(f'{record} Record Found!!')
        else:
            print(f'{record} Records Found!!')



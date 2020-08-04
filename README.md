# Case Study on Python

A standalone console based Python application which will manage various colleges across the state

## Run

1. Install python3 [python 3](https://www.python.org/downloads/) to run application.
2. Run college.py in terminal

```bash
python college.py
```

### Features

1. We have a class called College with the following attributes
   `(collegeId, collegeName, courseType, city, fees, pinCode)`
1. The application will be responsible for storing all data in a file by the name **colleges.csv**.
   A CSV file is nothing but a file with data separated by commas.
1. The program has below functionalities:
   - Register new College
   - Display Colleges in Mumbai having Engineering
   - Display Colleges in a *city*having _course_
   - Remove College based on _collegeId_

## Modules

Code divided into classes and functions.

1. **Classes**
   College class
1. **csvoperations**
   Operations related to CSV files
1. **tasks**
   all the tasks or feature class abstraction

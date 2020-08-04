from tasks import register, find, delete
import os

# for restarting
def restart():
    now = input("Press\tY to restart N to Exit\n")
    if now =='Y' or now =='y':
        main()
    else:
        print("See You Soon!!!")

# main function
def main():
    # To clear the console
    os.system('clear')
    print("Select Operation: \n 1.Register College\n 2.Find college with Engineering in Mumbai\n 3.Find College with Course and City\n 4.Delete College data with CollegeID\n 5.Exit⛔")
    op = input("Choose Operation: ")

    # Checking user request
    if op=='1':
        register.collegeDetails()
    elif op=='2':
        find.findCollege(op)
    elif op=='3':
        find.findCollege(op)
    elif op=='4':
        delete.deleteCollege()
    elif op=='5':
        print('Exit!!!')
    else:
        print("Choose valid Option❌")
    
    restart()

main()

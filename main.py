import subprocess as sp
import getpass
from db_connection import connect_to_db
from employee import hireAnEmployee, fireAnEmployee, promoteEmployee, employeeStatistics
from airport import addAirport, deleteAirport, airportStatistics
from airline import addAirline, deleteAirline, airlineStatistics
from airplane import addAirplane, deleteAirplane
from flight import addFlight, deleteFlight
from passenger import addPassenger, deletePassenger, addFirstClassPassenger, addBusinessClassPassenger
from operates import addOperates, deleteOperates

def dispatch(ch, cur, con):
    if ch == 1:
        hireAnEmployee(cur, con)
    elif ch == 2:
        fireAnEmployee(cur, con)
    elif ch == 3:
        promoteEmployee(cur, con)
    elif ch == 4:
        employeeStatistics(cur)
    elif ch == 5:
        addAirport(cur, con)
    elif ch == 6:
        deleteAirport(cur, con)
    elif ch == 7:
        airportStatistics(cur)
    elif ch == 8:
        addAirline(cur, con)
    elif ch == 9:
        deleteAirline(cur, con)
    elif ch == 10:
        airlineStatistics(cur)
    elif ch == 11:
        addAirplane(cur, con)
    elif ch == 12:
        deleteAirplane(cur, con)
    elif ch == 13:
        addFlight(cur, con)
    elif ch == 14:
        deleteFlight(cur, con)
    elif ch == 15:
        addPassenger(cur, con)
    elif ch == 16:
        deletePassenger(cur, con)
    elif ch == 17:
        addFirstClassPassenger(cur, con)
    elif ch == 18:
        addBusinessClassPassenger(cur, con)
    elif ch == 19:
        addOperates(cur, con)
    elif ch == 20:
        deleteOperates(cur, con)
    else:
        print("Error: Invalid Option")

if __name__ == "__main__":
    while True:
        tmp = sp.call('clear', shell=True)
        
        username = input("Username: ")
        password = getpass.getpass("Enter MySQL password: ")

        con, cur = connect_to_db(username, password)
        if con and cur:
            tmp = sp.call('clear', shell=True)
            print("Connected")
            tmp = input("Enter any key to CONTINUE>")

            while True:
                tmp = sp.call('clear', shell=True)
                print("1. Hire an Employee")
                print("2. Fire an Employee")
                print("3. Promote Employee")
                print("4. Employee Statistics")
                print("5. Add Airport")
                print("6. Delete Airport")
                print("7. Airport Statistics")
                print("8. Add Airline")
                print("9. Delete Airline")
                print("10. Airline Statistics")
                print("11. Add Airplane")
                print("12. Delete Airplane")
                print("13. Add Flight")
                print("14. Delete Flight")
                print("15. Add Passenger")
                print("16. Delete Passenger")
                print("17. Add First Class Passenger")
                print("18. Add Business Class Passenger")
                print("19. Add Operates Relationship")
                print("20. Delete Operates Relationship")
                print("21. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 21:
                    exit()
                else:
                    dispatch(ch, cur, con)
                    tmp = input("Enter any key to CONTINUE>")
        else:
            tmp = sp.call('clear', shell=True)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
            tmp = input("Enter any key to CONTINUE>")

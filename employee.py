def hireAnEmployee(cur, con):
    try:
        row = {}
        print("Enter new employee's details: ")
        row["Emp_id"] = input("Employee ID: ")
        row["F_name"] = input("First Name: ")
        row["M_name"] = input("Middle Name: ")
        row["L_name"] = input("Last Name: ")
        row["Jobtype"] = input("Job Type: ")
        row["Salary"] = float(input("Salary: "))
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        
        cur.execute("SELECT Airline_ID, Airline_name FROM Airline")
        airlines = cur.fetchall()
        print("Select Works For (Airline ID) from the following airlines:")
        for airline in airlines:
            print(f"ID: {airline['Airline_ID']}, Name: {airline['Airline_name']}")
        row["Works_For"] = input("Works For (Airline ID): ")

        cur.execute("SELECT Emp_id, F_name, L_name FROM Flight_Employee")
        employees = cur.fetchall()
        print("Select Manager ID from the following employees:")
        for emp in employees:
            print(f"ID: {emp['Emp_id']}, Name: {emp['F_name']} {emp['L_name']}")
        row["ManagerID"] = input("Manager ID: ")

        query = "INSERT INTO Flight_Employee (Emp_id, F_name, M_name, L_name, Jobtype, Salary, Bdate, Works_For, ManagerID) VALUES ('%s', '%s', '%s', '%s', '%s', %f, '%s', '%s', '%s')" % (
            row["Emp_id"], row["F_name"], row["M_name"], row["L_name"], row["Jobtype"], row["Salary"], row["Bdate"], row["Works_For"], row["ManagerID"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def fireAnEmployee(cur, con):
    try:
        emp_id = input("Enter Employee ID to fire: ")
        query = "DELETE FROM Flight_Employee WHERE Emp_id = '%s'" % emp_id
        cur.execute(query)
        con.commit()
        print("Employee fired from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

def promoteEmployee(cur, con):
    try:
        emp_id = input("Enter Employee ID to promote: ")
        new_salary = float(input("Enter new salary: "))
        query = "UPDATE Flight_Employee SET Salary = %f WHERE Emp_id = '%s'" % (new_salary, emp_id)
        cur.execute(query)
        con.commit()
        print("Employee promoted in the database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

def employeeStatistics(cur):
    try:
        query = "SELECT Jobtype, AVG(Salary) AS Average_Salary FROM Flight_Employee GROUP BY Jobtype"
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            print(f"Job Type: {row['Jobtype']}, Average Salary: {row['Average_Salary']}")

    except Exception as e:
        print("Failed to retrieve data from database")
        print(">>>>>>>>>>>>>", e)

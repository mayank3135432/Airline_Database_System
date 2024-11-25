def addPassenger(cur, con):
    try:
        row = {}
        print("Enter new passenger's details: ")
        row["PID"] = input("Passenger ID: ")
        row["BoardingFlight"] = input("Boarding Flight (Flight Code): ")

        query = "INSERT INTO Passenger (PID, BoardingFlight) VALUES ('%s', '%s')" % (
            row["PID"], row["BoardingFlight"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def deletePassenger(cur, con):
    try:
        pid = input("Enter Passenger ID to delete: ")
        query = "DELETE FROM Passenger WHERE PID = '%s'" % pid
        cur.execute(query)
        con.commit()
        print("Passenger deleted from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

def addFirstClassPassenger(cur, con):
    try:
        pid = input("Enter Passenger ID to promote to First Class: ")
        query = "INSERT INTO First_Class_Passenger (PID) VALUES ('%s')" % pid
        cur.execute(query)
        con.commit()
        print("Passenger promoted to First Class")

    except Exception as e:
        con.rollback()
        print("Failed to promote passenger to First Class")
        print(">>>>>>>>>>>>>", e)

def addBusinessClassPassenger(cur, con):
    try:
        pid = input("Enter Passenger ID to promote to Business Class: ")
        query = "INSERT INTO Business_Class_Passenger (PID) VALUES ('%s')" % pid
        cur.execute(query)
        con.commit()
        print("Passenger promoted to Business Class")

    except Exception as e:
        con.rollback()
        print("Failed to promote passenger to Business Class")
        print(">>>>>>>>>>>>>", e)

def addAirport(cur, con):
    try:
        row = {}
        print("Enter new airport's details: ")
        row["Ap_name"] = input("Airport Name: ")
        row["City"] = input("City: ")
        row["Country"] = input("Country: ")

        query = "INSERT INTO Airport (Ap_name, City, Country) VALUES ('%s', '%s', '%s')" % (
            row["Ap_name"], row["City"], row["Country"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def deleteAirport(cur, con):
    try:
        ap_name = input("Enter Airport Name to delete: ")
        query = "DELETE FROM Airport WHERE Ap_name = '%s'" % ap_name
        cur.execute(query)
        con.commit()
        print("Airport deleted from the database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

def airportStatistics(cur):
    try:
        query = "SELECT Country, COUNT(*) AS Airport_Count FROM Airport GROUP BY Country"
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            print(f"Country: {row['Country']}, Number of Airports: {row['Airport_Count']}")

    except Exception as e:
        print("Failed to retrieve data from database")
        print(">>>>>>>>>>>>>", e)

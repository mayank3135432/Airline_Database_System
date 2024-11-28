# PROJECT PHASE-4 

1. Get emplyee details:
 SELECT F_name, M_name, L_name, Phone_No FROM Flight_Employee JOIN Employee_Phone ON Flight_Employee.Emp_id = Employee_Phone.PID WHERE Works_For = (SELECT Airline_ID FROM Airline WHERE Airline_name = 'Emirates');

2. Get flight details from given source:
SELECT Flight_code, Destination, AirplaneID, Pilot, Departure FROM Flight WHERE Source = 'LAX';
Get flights from a sour

3. #flights operated by each ailines
SELECT Airline_name, COUNT(Flight_code) AS Total_Flights FROM Airline JOIN Flight_Employee ON Airline.Airline_ID = Flight_Employee.Works_For JOIN Flight ON Flight.Pilot = Flight_Employee.Emp_id GROUP BY Airline_name;

4. Get passenger details in a given flight 
SELECT F_name, M_name, L_name, Phone_No FROM Passenger LEFT JOIN Passenger_Phone ON Passenger.PID = Passenger_Phone.PID WHERE BoardingFlight = 'AA101';

5. #employees of each job type.
SELECT Airline_name, Jobtype, COUNT(*) AS Employee_Count FROM Flight_Employee JOIN Airline ON Flight_Employee.Works_For = Airline.Airline_ID GROUP BY Airline_name, Jobtype;

6. Promote an employee
UPDATE Flight_Employee SET Salary = Salary * 1.10 WHERE Jobtype = 'Pilot';

7. Change destination of flight 
UPDATE Flight SET Destination = 'LHR' WHERE Flight_code = 'DL202';

8. Update flying hours of an airplane.
UPDATE Airplane SET Flying_Hours = Flying_Hours + 500 WHERE Flying_Hours > 5000;

9. INSERT INTO Airport (Ap_name, City, Country) VALUES ('ORD', 'Chicago', 'USA'),('BOM', 'Mumbai', 'India'),('DEL', 'New Delhi', 'India');

10. INSERT INTO Flight_Employee (Emp_id, F_name, M_name, L_name, Jobtype, Salary, Bdate, Works_For, ManagerID) VALUES ('FE123', 'Michael', 'J', 'Scott', 'Pilot', 120000, '1980-01-15', 'AC1234', NULL), ('FE124', 'Dwight', 'K', 'Schrute', 'Cabin Crew', 75000, '1983-01-20', 'AC1234', 'FE123'), ('FE125', 'Jim', 'H', 'Halpert', 'Technician', 65000, '1985-02-25', 'ET5678', NULL);

INSERT INTO Airline (Airline_ID, Airline_name) VALUES ('AC1234', 'Air Canada'), ('ET5678', 'Ethiopian Airlines'), ('AI9101', 'Air India');
## Description of the queries:
1. Fetches the first name, middle name, last name, and phone number of employees working for the airline "Emirates."
2. Retrieves details (flight code, destination, airplane ID, pilot, and departure time) for flights departing from Los Angeles International Airport (LAX).
3. Counts the total number of flights operated by each airline, grouped by airline name.
4. Retrieves the names and phone numbers of passengers boarding flight "AA101".
5. Counts the number of employees in each job type (e.g., pilot, crew) for every airline, grouped by airline name and job type.
6. Increases the salary of all employees with the job type "Pilot" by 10%.
7. Updates the destination of the flight with flight code "DL202" to "London Heathrow (LHR)."
8. Adds 500 flying hours to airplanes that already have more than 5000 flying hours.
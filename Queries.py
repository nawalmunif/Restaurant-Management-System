import mysql.connector

myb = mysql.connector.connect(host="localhost", user="user", passwd="unlockit123|", database="Restaurant_Management")

mycursor = myb.cursor()

 ################queries##############################

mycursor.execute("Insert INTO Employee (FNAME, LNAME,EMAILID,ADDRESS, gender, phoneno, salary, EMPID) VALUES ('Hamza', 'Saleem', 'hamza@yahoo.com', 'Khi, Pakistan' , 'M', '0212987365', '50000', '1')")

myb.commit()
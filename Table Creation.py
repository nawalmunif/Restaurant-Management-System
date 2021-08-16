import mysql.connector

myb = mysql.connector.connect(host="localhost", user="user", passwd="unlockit123|", database="Restaurant_Management")

mycursor = myb.cursor()

#Creating table from query

#######customer table###############
mycursor.execute("CREATE TABLE Customer (Fname varchar(20) Not Null, lname varchar(20) Not Null , custid int primary key,emailid varchar(20) Not Null check(emailid like '%@%.com'),city varchar(20) default 'Ahmedabad',street varchar(20) not null,pincode integer not null ,gender varchar(1) not null check(gender = 'F' or gender = 'M' or gender = 'O'), phoneno integer not null , allergy varchar(20) default 'Null')")

#########employee table#############
mycursor.execute("CREATE TABLE Employee (FNAME varchar(20) Not Null, LNAME varchar(20) Not Null , EMPID int primary key,EMAILID varchar(20) Not Null check(emailid like '%@%.com'),ADDRESS varchar(20) not null,gender varchar(1) not null check(gender = 'F' or gender = 'M' or gender = 'O'), phoneno integer not null , salary varchar(50) not null)")

############Cuisine Table################
mycursor.execute("CREATE TABLE Cuisine (CUISINENAME varchar(20) Not Null, CUISINEID int primary key)")

############chef table####################
mycursor.execute("CREATE TABLE Chef (CHEFID int primary key, CHEFNAME varchar(20) Not Null, ADDRESS varchar(20) not null, phoneno integer not null , salary varchar(50) not null , EMPID int not null,EMAILID varchar(20) Not Null check(emailid like '%@%.com'), SPEC int not null, constraint fk_cusineChef FOREIGN KEY (SPEC) REFERENCES Cuisine(CUISINEID), constraint fk_cusineEmp FOREIGN KEY (EMPID) REFERENCES Employee(EMPID))")

#########food table##############
mycursor.execute("CREATE TABLE Food (FOODID int primary key, FOODNAME varchar(20) Not Null, PRICE varchar(20) not null, QUANTITY varchar(20) not null, CHEFID int not null, CUISINEID int not null, constraint fk_cusineFood FOREIGN KEY (CUISINEID) REFERENCES Cuisine(CUISINEID), constraint fk_chefFood FOREIGN KEY (CHEFID) REFERENCES CHEF(CHEFID))")

#########drinks table#######################
mycursor.execute("CREATE TABLE Drinks (DNAME varchar(20) Not Null, DRINKID int primary key, Price varchar(20) not null, SIZE varchar(20) not null check(SIZE IN( 'large', 'medium', 'small')) )")


############delivery tABLE###############
mycursor.execute("CREATE TABLE Delivery (DELNAME varchar(20) Not Null, DELID int primary key, DELCHARGE varchar(20) not null, DELDATE varchar(20) not null, CUSTID int not null, EMPID int not null, constraint fk_deliveryEmp FOREIGN KEY (EMPID) REFERENCES Employee(EMPID), constraint fk_deliveryCustomer FOREIGN KEY (CUSTID) REFERENCES Customer(CUSTID))") 


##############order table#####################
mycursor.execute("CREATE TABLE Orders ( DelID int not null, TOTALCOST varchar(20) not null, ORDID int primary key, FOODID int not null, DrinkID int not null, constraint fk_orderFood FOREIGN KEY (FOODID) REFERENCES FOOD(FOODID), constraint fk_orderDrink FOREIGN KEY (DrinkID) REFERENCES DRINKS(DRINKID), constraint fk_orderDev FOREIGN KEY (DelID) REFERENCES Delivery(DELID) )" )



######################## payment table #####################
mycursor.execute("CREATE TABLE Payment ( PAYMETHOD varchar(20) not null check ( PAYMETHOD IN (' credit card ', 'cash', 'debit card', 'Paytm')), CUSTID INT not null, constraint fk_PaymentCustomer FOREIGN KEY (CUSTID) REFERENCES Customer(CUSTID), ORDID int not null, constraint fk_PaymentOrder FOREIGN KEY (ORDID) REFERENCES Orders(ORDID), PID int not null)")
myb.commit()
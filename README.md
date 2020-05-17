# PythonGUI_for_Database
Connecting the database to a Graphical User Interface using python.
A simple python GUI application using tkinter and MySQL
***************README******************

1. Find the "Data.sql" along with the files.
2. Import the Turner.sql file into your system by following the steps below
	1. Open CommandPrompt or Terminal(if MAC os)
	2. Open MySQL from your terminal
	3. Create a new Database using command "create database Data" (without the quotes)
	4. Type the following command to import Data.sql dump into your system
		mysql -u root -p db_name < ~/Documents/db_name.sql
	5. Insert more values into the tables.

3. Open the main.py in Pycharm or any IDE and run it.

4. Before running main.py, make sure you have the following
	1. A user named "user1" is created in the MySQL with password as "password"(see below for the steps)
	2. A Database called Turner is there in your MySQL
	3. Open Terminal/command prompt and type the following
		pip install pymysql
		pip install tkinter

****************************************
Creating a user and granting privileges to the user in MySQL

1. open the database using "use Data;" command.
2. type the following commands
	CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password';
3. GRANT ALL PRIVILEGES ON Turner.* TO 'user1'@'localhost';
****************************************

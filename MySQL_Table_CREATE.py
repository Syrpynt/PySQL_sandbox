import mysql.connector                      # MySQL connector MODULE. This was installed via gitBASH and
                                            # approved with PYTHON's install with checkbox "PATH ALLOWED"

account = mysql.connector.connect(          # MySQL connect function used to connect to databases
    host = "localhost",
    user = "root",
    passwd = input("PASSWORD: "),           # Input user password for security reasons! Don't hardcode!
    database = input("Which database do you want to add a table to? "), # The database (db) input is also the only db that the table will be applied to!
    )

#Create "cursor" instance into the MySQL query text box for submitting commands to MySQL.
my_cursor = account.cursor()

#Create new table, DO NOT use if table name already exists! Error checking opportunity here for the future...
tblname = input("What is the new table's name: ")
column_quantity = int(input("How many columns does the table need? "))
column_qty = column_quantity + 1

# Turning the user inputs into an "Array form" for easy data recall later.
column_id = [0]
x = 0
flag = str(1)
column_id[x] = input("What is column " + flag + "'s name and data type? ")

# User inputs the column names and their datatypes, will ask as many times as they entered the "column quantity".
for x in range(2, column_qty):
        flag = str(x)
        column = input("What is column " + flag + "'s name and data type? ")
        column_id.append(column)

#Creates the table. Columns are added to the first column of the table because it makes the logic easier.
for x in range(1, column_qty):
    if x == 1:
        my_cursor.execute("CREATE TABLE " + tblname + "(" + column_id[x - 1] + ")")
    else:
        my_cursor.execute("ALTER TABLE " + tblname + " ADD " + column_id[x - 1])


# Confirmation
print('table and columns successfully created')
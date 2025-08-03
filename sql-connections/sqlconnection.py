import mysql.connector
mydvb= mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="***Your Password***",
    database= "sakila")
mycursor = mydvb.cursor() 
#mycursor.execute("SHOW TABLES") 
mycursor.execute("SELECT * FROM actor WHERE first_name LIKE 'j%'")
for table in mycursor: 
   print(table)
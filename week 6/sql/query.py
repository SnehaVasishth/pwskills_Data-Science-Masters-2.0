import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
mycursor=mydb.cursor()
##mycursor.execute("SELECT *from test3.test3_table")
mycursor.execute("SELECT c1,c2 from test3.test3_table")
for i in mycursor.fetchall():
    print(i)


mydb.close()

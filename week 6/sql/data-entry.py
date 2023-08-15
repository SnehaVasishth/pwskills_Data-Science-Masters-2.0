import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
mycursor=mydb.cursor()
mycursor.execute("insert into test3.test3_table values(21,'Sneha',100.230,100,'Vasishth')")
mycursor.execute("insert into test3.test3_table values(21,'Sneha',100.230,100,'Vasishth')")
mycursor.execute("insert into test3.test3_table values(21,'Sneha',100.230,100,'Vasishth')")
mycursor.execute("insert into test3.test3_table values(21,'Sneha',100.230,100,'Vasishth')")
mycursor.execute("insert into test3.test3_table values(21,'Sneha',100.230,100,'Vasishth')")
mycursor.execute("insert into test3.test3_table values(21,'Sneha',100.230,100,'Vasishth')")

mydb.commit()
mydb.close()
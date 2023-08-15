import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database="Student_database" 
)

mycursor = mydb.cursor()

query=""" INSERT INTO Details(NAME,ROLLNO,EMAIL)
          VALUES('Sneha Vasishth' ,35,'swqqjj@gmail.com'),
                 ('sparsh',40,'edkdw@gmail.com');
"""
mycursor.execute(query)
mydb.commit()
mycursor.close()
mydb.close()
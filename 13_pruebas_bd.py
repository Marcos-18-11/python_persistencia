import mysql.connector as con
db=con.connect(host="localhost",
               user="root",
               password="root",
               port=3306,
               database="universidad")
print("Conexión realizada!")
cursordb=db.cursor(dictionary=True)
sql_insert="insert into alumnos values(%s,%s,%s,%s,%s)"
cursordb.execute(sql_insert,("655656z","alumno6","alumno6@gamil.com","python",9))
db.commit()
cursordb.execute("select * from alumnos where nota>%s",(5,))
for row in cursordb:
    print(row)
db.close()
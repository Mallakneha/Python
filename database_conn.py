import mysql.connector
def create_connection():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mysql@123",
            database="mydata"
        )
        print("Connection Successfull")
        return connection
    except mysql.connector.Error as e:
        print("Error connection",e)
        return None
def create_table(connection):
    try:
        cursor=connection.cursor()
        cursor.execute("create table  if not exists student_infor (id int,name varchar(10), age int,course varchar(10))")
        print("Table Creation Successful")
        cursor.close()     
    except mysql.connector.Error as e:
        print('Error in Creation',e)   
def insert_data(connection):
    try:
        cursor=connection.cursor()
        cursor.execute("delete from student_infor")
        cursor.execute("""insert into student_infor (id,name,age,course)values
        (1,'Neha',21,'Python'),
        (2,'Sanvika',20,'Java'),
        (3,'Sarika',22,'Sql'),
        (4,'Keerthana',23,'Python')""")
        connection.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print("Insertion Error",e)
   
def display_data(connection):
    try:
        cursor=connection.cursor()
        cursor.execute("select * from student_infor")
        print("Display Successful")
        res=cursor.fetchall()
        for i in res:
            print(i)
    except mysql.connector.Error as e:
        print("Error in displaying",e)
def main():
    try:
        connection=create_connection()
        if connection:
            create_table(connection)
            insert_data(connection)
            display_data(connection)
    except mysql.connector.Error as e:
        print("not display",e)
    finally:
        connection.close()
if __name__=='__main__':
    main()

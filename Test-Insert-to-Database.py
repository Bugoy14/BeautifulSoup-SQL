
from bs4 import BeautifulSoup
import mysql.connector

my_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='alieya30',
    database='dbpythoncourse'
)

my_cursor = my_connection.cursor()

mysql_query = "insert into tblcourses (Course, Price) values (%s, %s)"

python_courses = [
    ('Python AI', '120')
]

try:
    my_cursor.executemany(mysql_query, python_courses)
    my_connection.commit()
    print("Data Manipulated")
except Exception as e:
    print(f"Error: {e}")
    my_connection.rollback()

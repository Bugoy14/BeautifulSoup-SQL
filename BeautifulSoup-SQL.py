from bs4 import BeautifulSoup
import mysql.connector

my_database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='alieya30',
    database='dbpythoncourse'
)

my_cursor = my_database.cursor()

all_course = []
with open("C:/Users/azarc/Downloads/home.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")

    course_cards = soup.find_all("div", class_="card")

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        all_course.append((course_name, course_price))
        print(f"{course_name} costs {course_price}")


mysql_query = "insert into tblcourses (Course, Price) values (%s, %s)"

try:
    my_cursor.executemany(mysql_query, all_course)
    my_database.commit()
    print("Data Inserted")
except Exception as e:
    print(f"Error: {e}")
    my_database.rollback()

import sqlite3
sch=sqlite3.connect('school.db')
c=sch.cursor()

c.execute("""

          CREATE TABLE IF NOT EXISTS Students(
          Id INTEGER PRIMARY KEY AUTOINCREMENT,
          Name TEXT,
          Age INTEGER,
          Grade INTEGER
          );
          """)
sch.commit()
#******************** Add Student Details ***************************
def add_stud_details():
 n =input("Enter your Name:")
 a =int(input("Enter your Age:"))
 g =input("Enter your Grade:")


 c.execute("""INSERT INTO Students(Name,Age,Grade)
             VALUES(?,?,?)
             """,(n,a,g))
 sch.commit()
#********************** view Student ***************************
def view_student():
    print("\n|---------------------------------- View All Students --------------------------|")
    c.execute("SELECT * FROM Students")

    print(f"{'Id':<20}{'Name':<15}{'Age':<15}{'Grade':<15}")
    print(
        "----------------------------------------------------------------------------------------------------------|")

    for item in c.fetchall():
        print(f"{item[0]:<20}{item[1]:<15}{item[2]:<15}{item[3]:<10}")
    sch.commit()


# #**************************** View Passing Student *************************
def view_pass_student():
    print("\n|---------------------------------- View Passig Students --------------------------|")
    c.execute("SELECT * FROM Students WHERE Grade>=70")
    print(f"{'Id':<20}{'Name':<15}{'Grade':<15}")
    print("-"*40)

    for item in c.fetchall():
        print(f"{item[0]:<20}{item[1]:<15}{item[3]:<15}")

    sch.commit()

# #****************************** Show Average Grade **************************
def avg_grade():
    print("\n|---------------------------------- Show Average Grade --------------------------|")
    c.execute("SELECT AVG(Grade) From Students")
    Average=c.fetchall()[0]
    print("Average Grade:",Average)
    sch.commit()


# #********************************* Search Student ******************************
def sear_student():

    print("\n|---------------------------------- Search Students --------------------------|")
    Name = input("Enter your Name:")
    c.execute("SELECT * FROM Students WHERE Name=?",(Name,))

    student = c.fetchone()
    if student:
        print(f"{'Id':<20}{'Name':<15}{'Age':<15}{'Grade':<15}")
        print(f"{student[0]:<20}{student[1]:<15}{student[2]:<15}{student[3]:<15}")
    else:
        print("Student not found")
    sch.commit()

# #*********************************** Delete Student ****************************
def delete_student():
    view_student()
    print("\n|------------------------------- Delete Student --------------------------|")
    id = input("Enter your Id:")
    c.execute("DELETE FROM Students WHERE Id=?",(id,))
    print("Student deleted")
    sch.commit()

# #************************* Main Program *******************************
while True:
    print("====================== STUDENT MANAGEMENT SYSTEM ==========================")
    print("1.Add student")
    print("2.View all students")
    print("3.View passing students")
    print("4.Show average grade")
    print("5.Search student")
    print("6.Delete student")
    print("7.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
      add_stud_details()
    elif choice == 2:
        view_student()
    elif choice == 3:
        view_pass_student()
    elif choice == 4:
        avg_grade()
    elif choice == 5:
        sear_student()
    elif choice == 6:
        delete_student()
    else:
        print("Exit")
        break


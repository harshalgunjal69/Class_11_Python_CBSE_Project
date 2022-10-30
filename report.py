from prettytable import PrettyTable

mytable_2 = PrettyTable()
mydict = {}

no_students = int(input("Enter the number of students' reports you wanna enter ? "))

for i in range(1, no_students + 1):
    mytable = PrettyTable()

    print('\n')
    print("Enter the details of student ", i, " : ")
    print('\n')

    name = input("Enter the name of the student : ")
    class_ = input("Enter the class/sec of the student : ")
    roll_no = input("Enter the roll no. of the student : ")

    print('\n')
    print("Now, lets get to the academic details.")
    print('\n')

    print('1. Maths')
    print('\n')
    term1_1 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
    term2_1 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
    term_1 = max(term1_1, term2_1)
    pt_1 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
    assignment_1 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
    practical_1 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
    grade_1 = input("Enter the grade to be given ( best of 2 ) : ")
    totalmarks_1 = term_1 + pt_1 + assignment_1 + practical_1
    print('\n')

    print('2. Physics')
    print('\n')
    term1_2 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
    term2_2 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
    term_2 = max(term1_2, term2_2)
    pt_2 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
    assignment_2 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
    practical_2 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
    grade_2 = input("Enter the grade to be given ( best of 2 ) : ")
    totalmarks_2 = term_2 + pt_2 + assignment_2 + practical_2
    print('\n')

    print('3. Chemistry')
    print('\n')
    term1_3 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
    term2_3 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
    term_3 = max(term1_3, term2_3)
    pt_3 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
    assignment_3 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
    practical_3 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
    grade_3 = input("Enter the grade to be given ( best of 2 ) : ")
    totalmarks_3 = term_3 + pt_3 + assignment_3 + practical_3
    print('\n')

    print('4. Computer / Bio')
    print('\n')
    term1_4 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
    term2_4 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
    term_4 = max(term1_4, term2_4)
    pt_4 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
    assignment_4 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
    practical_4 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
    grade_4 = input("Enter the grade to be given ( best of 2 ) : ")
    totalmarks_4 = term_4 + pt_4 + assignment_4 + practical_4
    print('\n')

    print('5. English')
    print('\n')
    term1_5 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
    term2_5 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
    term_5 = max(term1_5, term2_5)
    pt_5 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
    assignment_5 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
    practical_5 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
    grade_5 = input("Enter the grade to be given ( best of 2 ) : ")
    totalmarks_5 = term_5 + pt_5 + assignment_5 + practical_5
    print('\n')

    list_data = [[term1_1, term2_1, pt_1, assignment_1, practical_1, totalmarks_1, grade_1],
                 [term1_2, term2_2, pt_2, assignment_2, practical_2, totalmarks_2, grade_2],
                 [term1_3, term2_3, pt_3, assignment_3, practical_3, totalmarks_3, grade_3],
                 [term1_4, term2_4, pt_4, assignment_4, practical_4, totalmarks_4, grade_4],
                 [term1_5, term2_5, pt_5, assignment_5, practical_5, totalmarks_5, grade_5]]

    mydict[name] = list_data
    print("\n")


    def table(my_table):
        print('                                      Atomic Energy Central School No. 3                              ')
        print('                                                 REPORT CARD                                          ')
        print('\n')

        print("Name of the student : ", name)
        print("Class/Sec : ", class_)
        print("Roll no. : ", roll_no)
        print('\n')

        my_table.field_names = ["SUBJECT", "TERM 1", "TERM 2",
                               "PERIODIC TESTS", "ASSIGNMENT", "PRACTICALS",
                               "TOTAL MARKS", "GRADE(Best of 2)"
                                ]

        my_table.add_row(
            ["Maths", list_data[0][0], list_data[0][1],
             list_data[0][2], list_data[0][3], list_data[0][4],
             list_data[0][5], list_data[0][6]]
        )
        my_table.add_row(
            ["Physics", list_data[1][0], list_data[1][1],
             list_data[1][2], list_data[1][3], list_data[1][4],
             list_data[1][5], list_data[1][6]]
        )
        my_table.add_row(
            ["Chemistry", list_data[2][0], list_data[2][1],
             list_data[2][2], list_data[2][3], list_data[2][4],
             list_data[2][5], list_data[2][6]]
        )
        my_table.add_row(
            ["Computer / Bio", list_data[3][0], list_data[3][1],
             list_data[3][2], list_data[3][3], list_data[3][4],
             list_data[3][5], list_data[3][6]]
        )
        my_table.add_row(
            ["English", list_data[4][0], list_data[4][1],
             list_data[4][2], list_data[4][3], list_data[4][4],
             list_data[4][5], list_data[4][6]]
        )
        my_table.add_row(["C.G.P.A. ", " ", " ", " = ", " ", " ", (
                list_data[0][5] + list_data[1][5] + list_data[2][5] +
                list_data[3][5] + list_data[4][5]) / 5, " "]
                         )

        table_line = my_table.get_string().split('\n')
        horizontal_line = table_line[0]
        result_lines = 1
        print("\n".join(table_line[:-(result_lines + 1)]))
        print(horizontal_line)
        print("\n".join(table_line[-(result_lines + 1) :]))


    table(mytable)


print("\n")
update_name = eval(input("Enter the name of the student whose marks you wanna update( input inside '' ) : "))
list_data = mydict[update_name]

print("\nWhich subject's marks do you wanna change : ")
print("1 - Maths")
print("2 - Physics")
print("3 - Chemistry")
print("4 - Comp/Bio")
print("5 - English\n")
choice_subjects = int(input())
print("\n")

def term1() :
    if choice_exam == 2 :
        return int(term1_1)
    elif choice_exam == 1 :
        return int(term1_2)


def term2() :
    if choice_exam == 2 :
        return int(term1_2)
    elif choice_exam == 1 :
        return int(term2_2)


def term3() :
    if choice_exam == 2 :
        return int(term1_3)
    elif choice_exam == 1 :
        return int(term2_3)


def term4() :
    if choice_exam == 2 :
        return int(term1_4)
    elif choice_exam == 1 :
        return int(term2_4)


def term5() :
    if choice_exam == 2 :
        return int(term1_5)
    elif choice_exam == 1 :
        return int(term2_5)


if choice_subjects == 1 :
    print("Which marks do you wanna change : ")
    print("1 - Term 1")
    print("2 - Term 2")
    print("3 - Periodic tests")
    print("4 - Assignments")
    print("5 - Practicals\n")
    choice_exam = int(input())
    new_marks = int(input("\nEnter the new marks = "))
    list_data[choice_subjects - 1][choice_exam - 1] = new_marks
    list_data[choice_subjects - 1][5] = max(new_marks, term1()) + pt_1 + assignment_1 + practical_1

if choice_subjects == 2 :
    print("Which marks do you wanna change = ")
    print("1 - Term 1")
    print("2 - Term 2")
    print("3 - Periodic tests")
    print("4 - Assignments")
    print("5 - Practicals\n")
    choice_exam = int(input())
    new_marks = int(input("\nEnter the new marks = "))
    list_data[choice_subjects - 1][choice_exam - 1] = new_marks
    list_data[choice_subjects - 1][5] = max(new_marks, term2()) + pt_1 + assignment_1 + practical_1

if choice_subjects == 3 :
    print("Which marks do you wanna change = ")
    print("1 - Term 1")
    print("2 - Term 2")
    print("3 - Periodic tests")
    print("4 - Assignments")
    print("5 - Practicals\n")
    choice_exam = int(input())
    new_marks = int(input("\nEnter the new marks = "))
    list_data[choice_subjects - 1][choice_exam - 1] = new_marks
    list_data[choice_subjects - 1][5] = max(new_marks, term3()) + pt_1 + assignment_1 + practical_1

if choice_subjects == 4 :
    print("Which marks do you wanna change = ")
    print("1 - Term 1")
    print("2 - Term 2")
    print("3 - Periodic tests")
    print("4 - Assignments")
    print("5 - Practicals\n")
    choice_exam = int(input())
    new_marks = int(input("\nEnter the new marks = "))
    list_data[choice_subjects - 1][choice_exam - 1] = new_marks
    list_data[choice_subjects - 1][5] = max(new_marks, term4()) + pt_1 + assignment_1 + practical_1

if choice_subjects == 5 :
    print("Which marks do you wanna change = ")
    print("1 - Term 1")
    print("2 - Term 2")
    print("3 - Periodic tests")
    print("4 - Assignments")
    print("5 - Practicals\n")
    choice_exam = int(input())
    new_marks = int(input("\nEnter the new marks = "))
    list_data[choice_subjects - 1][choice_exam - 1] = new_marks
    list_data[choice_subjects - 1][5] = max(new_marks, term5()) + pt_1 + assignment_1 + practical_1

print("\nNew report card : ")
table(mytable_2)

update_name_2 = input("\nEnter the name of the student you wanna delete = ")
del mydict[update_name_2]
print("\nData of", update_name_2, "has been deleted from the database.")
















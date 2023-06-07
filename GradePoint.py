print("===========================Grade Point Calculator================================")

school_name = input("Your School Name: ")
student_name = input("Your Name: ")
level_education = input("Your Level of Education: ")
passing_year = int(input("Passing Year: "))

sub1_name = (input("Subject name: "))
sub1_number = int(input("Number: "))

sub2_name = (input("Subject name: "))
sub2_number = int(input("Number: "))

sub3_name = (input("Subject name: "))
sub3_number = int(input("Number: "))

print("=====================StudentProfile===============================")

print("Your School Name: " + school_name)
print("Your Name: " + student_name)
print("Your Level Education: " + level_education)
print("Year of Compleated: ",passing_year)
print("Course-01: " + sub1_name)
print("You got: ", sub1_number)
print("Course-02: " + sub2_name)
print("You got: ",sub2_number)
print("Course-01: " + sub3_name)
print("You got: ",sub3_number)

if sub1_number + sub2_number + sub3_number > 270:
    print("Your GPA: A")
elif sub1_number + sub2_number + sub3_number > 240:
    print("Your GPA: B")
elif sub1_number + sub2_number + sub3_number >210:
    print("Your GPA: C")
else:
    print("Sorry You are Fail")
print("Your Total Number: ", sub1_number + sub2_number + sub3_number)
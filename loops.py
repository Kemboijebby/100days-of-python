#fruits=["Apple","Mango","Orange","Pineapple"]
#for fruit in fruits:
    #print(fruit)
   # print(fruit + " ""pie")
#print(fruits)

student_heights=input("Input the student heights.\n").split()
for n in range(0,len(student_heights)):
    student_heights=int(student_heights[n])
print(student_heights)

total_heights=0
for heights in student_heights:
    total_heights+=heights
#print(f"The total sum of student heights is {total_heights}")


student_no=0
for students in student_heights:
    student_no+=1
#print(f"The number of students is {student_no}")
average=round(total_heights/student_no,2)
print(f"The average of the students heights is {average}")

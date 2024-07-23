name = "shamoon ahmed"

first, last = name.split(" ")
for i in first, last:
    print(i.capitalize(), end=" ")

print()

para = input("Enter a paragraph: ")
char = []
words = para.split(" ")
for i, ch in enumerate(words):
    char.append(ch)
    total_char = "".join(char)
print("Number of words: ", len(char))
print("Number of characters: ", len(total_char))

print()

# Student Management System:
# This project is a simple console based Student Management System.
# In this project you will be learning how to add new students,
# how to generate a 5 digit unique studentID for each student,
# how to enroll students in the given courses.
# Also, you will be implementing the following operations
# enroll, view balance, pay tuition fees, show status, etc.
# The status will show all the details of the student including
# name, id, courses enrolled and balance.
# This is one of the best projects to implement the
# Object-Oriented Programming concepts.

import random


class Student:

    fees = 7000

    def __init__(self, std_name, paid_fees):
        self.std_name = std_name
        self.paid_fees = paid_fees


    def id(self):
        unique = random.randint(10001, 10010)
        return unique

    def pay_fee(self):
        owe = self.fees - self.paid_fees
        if self.paid_fees < self.fees:
            return owe

    def enroll(self, course1="N/A", course2="N/A", course3="N/A", course4="N/A", course5="N/A"):
        self.course1 = course1
        self.course2 = course2
        self.course3 = course3
        self.course4 = course4
        self.course5 = course5

    def status(self):
        print("Student Name: ", self.std_name)
        print("ID: ", self.id())
        print("Eligibility: 5 Courses")
        print("Courses Enrolled: ", self.course1, ",", self.course2, ",", self.course3, ",", self.course4, ",", self.course5)
        print("Fees Paid: ", self.paid_fees)
        print("Balance: ", self.pay_fee())


s1 = Student("Samson", 6500)
s1.enroll("PF", "Eng")
s1.status()

print("------------------------")

s2 = Student("Sohaib", 7000)
s2.enroll("ICT", "English", "DMS")
s2.status()

print("------------------------")

s3 = Student("Bro", 5500) #making another object
s3.enroll("Eng", "PF")
s3.status()
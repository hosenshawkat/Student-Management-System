# Student-Management-System
Python has four main built-in data structures: 1. List 2. Tuple 3. Set 4. Dictionary

1. List
students = []

সব student এই list-এর মধ্যে থাকবে।

students.append(student)

নতুন student add করছি।

List = ordered + changeable + duplicate allowed


2. Tuple
basic_info = (student_id, name)

এখানে Student ID এবং Name একসাথে রাখছি।

যেমন:

("S001", "Shawkat")

Tuple সাধারণত এমন data-এর জন্য ভালো যেটা পরিবর্তন করার দরকার নেই।

Tuple = ordered + unchangeable


3. Set
courses = {"Python", "Database", "Django"}

এখানে available courses রাখছি।

আর student-এর course:

"courses": set()

তারপর:

student["courses"].add(course)

Set-এর সুবিধা হলো duplicate automatically remove হয়।

যেমন:

courses = {"Python", "Python", "Database"}

ফল:

{"Python", "Database"}


4. Dictionary

প্রতিটি student-এর information dictionary-তে:

student = {
    "basic_info": basic_info,
    "age": age,
    "courses": set()
}

Dictionary-তে key → value থাকে।

যেমন:
"age": 25

এখানে:

key   = age
value = 25

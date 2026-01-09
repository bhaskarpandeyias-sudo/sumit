import pandas as pd
import numpy as np

marks = {
"Name": [
        "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun",
        "Sai", "Krishna", "Ishaan", "Rohan", "Ananya",
        "Diya", "Priya", "Kavya", "Neha", "Pooja",
        "Sneha", "Aditi", "Isha", "Nisha", "Ritika",
        "Rahul", "Aman", "Suresh", "Ramesh", "Mahesh",
        "Kiran", "Sunil", "Vikram", "Anil", "Deepak",
        "Pankaj", "Nitin", "Sachin", "Vikas", "Ajay",
        "Manoj", "Sanjay", "Ravi", "Ashok", "Gaurav",
        "Shubham", "Prakash", "Harish", "Naresh", "Mukesh",
        "Alok", "Rajesh", "Dinesh", "Yogesh", "Saurabh"
    ],
    "Maths": [
        45, 56, 67, 78, 89, 90, 72, 65, 88, 91,
        54, 60, 73, 84, 95, 69, 77, 82, 86, 58,
        64, 71, 79, 85, 92, 48, 55, 63, 70, 76,
        81, 87, 93, 59, 66, 74, 80, 83, 94, 57,
        61, 68, 75, 78, 88, 90, 96, 52, 62, 73
    ],
    "Science": [
        50, 62, 74, 86, 91, 68, 79, 83, 95, 57,
        64, 71, 88, 92, 76, 84, 69, 77, 81, 90,
        55, 63, 70, 78, 85, 93, 60, 67, 73, 80,
        87, 94, 58,

df["sum"]=df.sum(axis=1,numeric_only= True)
df["average"]=df.mean(axis=1,numeric_only= True)
df["max"]=df.max(axis=1,numeric_only= True)
df["min"]=df.min(axis=1,numeric_only= True)
df["count"]=df.count(axis=1,numeric_only= True)

df.to_excel("marks_with_functions.xlsx",index=False)
    ]
}
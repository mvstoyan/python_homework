import csv
import os
import custom_module
from datetime import datetime

#Task 2

def read_employees():
    data = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row 
                else:
                    rows.append(row)  
        data["rows"] = rows  
        return data
    except TypeError:
            return "You can't multiply those values!"

employees=read_employees()

#Tack 3

def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except TypeError:
        return "You can't multiply those values!"
employee_id_column= column_index("employee_id")

# Task 4

def first_name(row_number):
    employee_id_column = column_index("first_name")
    try:
        return employees['rows'][row_number][employee_id_column]
    except TypeError:
        return 'You can´t use this values'
first_name(1)

# Task 5
def employee_find(emp_id):
    try:
        def employee_match(row):
            return int(row[employee_id_column]) == emp_id
        matches=list(filter(employee_match, employees["rows"]))
        return matches
    except ValueError:
        return "Value is not correct"
    
employee_find(3)

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

employee_find_2(4)

#Task 7
def sort_by_last_name():
    try:
        employee_lastName_column=column_index("last_name")
        employees["rows"].sort(key= lambda row: row[employee_lastName_column])
        return employees["rows"]
    except TypeError:
        return "The type is incorrect"
sort_by_last_name()

#Task 8

def employee_dict(row):
    try:
        keys=employees['fields'][1:]
        
        values=row[1:]
        
        employee=dict(zip(keys, values))
        return employee
    except KeyError as e:
        return e
print(employee_dict(employees['rows'][0]))

# Task 9
def all_employees_dict():
    try:
        empDict={}
        for employee in employees["rows"]:
            key=employee[0]
            value=employee_dict(employee)
            empDict[key]=value

        return empDict

    except TypeError:
        return "The type is incorrect"
print(all_employees_dict())

#Task 10
def get_this_value():
    return os.getenv("THISVALUE")
get_this_value()

#Task 11
def set_that_secret(new_secret):
    try:
        return custom_module.set_secret(new_secret)
    except Exception as e:
        return e
set_that_secret("secret")

#Task 12
minutes1={}
minutes2={}
def read_minutes():
    try:
        def reader(read_file, minutes):
            minutes={}
            rows=[]
            with open(read_file, 'r') as file:
                reader = csv.reader(file)
                for index, row in enumerate(reader):
                    if index==0:
                        minutes['fields']=row
                    else:
                        rows.append(tuple(row))
            minutes["rows"]=rows
            return minutes
        global minutes1, minutes2
        minutes1=reader('../csv/minutes1.csv', minutes1)
        minutes2=reader('../csv/minutes2.csv', minutes2)
        return minutes1, minutes2
    except TypeError:
            return "You can't use those values!"
read_minutes()

#Task 13
minutes_set=set()
def create_minutes_set():
    try:
        set1 = set(tuple(row) for row in minutes1.get("rows"))
        set2 = set(tuple(row) for row in minutes2.get("rows"))
        unionSet=set1.union(set2)
        global minutes_set
        minutes_set=unionSet
        return minutes_set
    except Exception as e:
        return e
create_minutes_set()

#Task 14
def create_minutes_list():
    try:
        return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),minutes_set))
    except Exception as e:
        return e
minutes_list=create_minutes_list()
print(minutes_list)

#Task 15
def write_sorted_list():
    try:
        global minutes_list
        sortedList=sorted(minutes_list, key=lambda x: x[1])
        newList=list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),sortedList))
        
        with open('./minutes.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            for row in newList:
                writer.writerow(row)

        return newList
    except Exception as e:
        return e
write_sorted_list()
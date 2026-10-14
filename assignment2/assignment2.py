from numpy import sort
import os
import csv
from datetime import datetime
# task 2
def read_employees():
    # decoear empty dict and list
    employees_dict = {}
    employees_list = []
    try:
        with open("../csv/employees.csv", "r") as file:
            # use csv.reader to read the file
            reader = csv.reader(file)
            # save header row
            header_fields = next(reader)
            employees_dict["fields"] = header_fields

            for row in reader:
                # append row to the list
                employees_list.append(row)
            # save row to the dict
            employees_dict["rows"] = employees_list
    except Exception as e:
        print(f"An exception occurred: {e}")
    return employees_dict

employees = read_employees()
#print(employees)

# task 3 Find the Column Index
def column_index(field):
    field_index = employees["fields"].index(field)
    return field_index

employee_id_column = column_index("employee_id")

# task 4 find First Name by Row Index
def first_name(row_index):
    #get first name idx
    idx = column_index("first_name")
    return employees["rows"][row_index][idx]

#print(first_name(2))

#====Task 5: Find the Employee: a Function in a Function====
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#print(employee_find(5))

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))   
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    # get last name index
    last_name_idx = column_index("last_name")
    #sort employees["rows"] using .sort 
    #

    employees["rows"].sort(key=lambda row: row[last_name_idx])
    return employees["rows"]

# task 8: Convert an Employee Row to a Dictionary
# ex. ['1', 'Cindy', 'Wade', '+222 656-486-3727'] -> {'first_name': 'Cindy', 'last_name': 'Wade', 'phone': '+222 656-486-3727'}
def employee_dict(row):
    # creat empty dictionary
    emp_dist = {}
    for field, value in zip(employees["fields"], row):
        if field != "employee_id":
            emp_dist[field] = value
    return emp_dist


#print(employee_dict(employees["rows"][0]))

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    all_dict = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column] # get employee id (from task 3)
        emp_data = employee_dict(row) # get employee data (from task 8)
        all_dict[emp_id] = emp_data # save employee data to the dict
    return all_dict
    
#print(all_employees_dict())

# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

#print(get_this_value())

# Task 11: Creating Your Own Module
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("codethedream")
print(custom_module.secret)


# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    # read first file
    minutes1 = {}
    with open('../csv/minutes1.csv', 'r') as file:
        reader = csv.reader(file)
        rows_list = []
        for index, row in enumerate(reader):
            if index == 0:
                minutes1["fields"] = row
            else:
                # change row to tuple！
                rows_list.append(tuple(row))
        minutes1["rows"] = rows_list

    # read second file
    minutes2 = {}
    with open('../csv/minutes2.csv', 'r') as file:
        reader = csv.reader(file)
        rows_list = []
        for index, row in enumerate(reader):
            if index == 0:
                minutes2["fields"] = row
            else:
                # change row to tuple
                rows_list.append(tuple(row))
        minutes2["rows"] = rows_list
    

    return minutes1, minutes2

# global variable and get value 
minutes1, minutes2 = read_minutes()
#print("Minutes 1:", minutes1)
#print("Minutes 2:", minutes2)
    

# Task 13: Create minutes_set

def create_minutes_set():
    # Tuples are immutable, so they can be added to a set.
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    
    # combine the two sets using union() method
    combined_set = set1.union(set2)
    
    return combined_set

minutes_set = create_minutes_set()
#print("minutes_set has", len(minutes_set), "rows")

# Task 14: Convert to datetime
def create_minutes_list():
    # convert set to list
    minutes_list = list(minutes_set)
    
    # convert string to datetime object by using map and lambda
    converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    
    return converted_list

minutes_list = create_minutes_list()
print("Minutes List (with datetime ):", minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    # Sort minutes_list in ascending order of datetime.
    minutes_list.sort(key=lambda x: x[1])
    
    # using map and lambda to convert datetime object to string format
    sorted_converted = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    
    # Write the sorted and converted data to ./minutes.csv
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # write the header row
        writer.writerow(minutes1["fields"])
        # write all the meeting records
        writer.writerows(sorted_converted)
        
    return sorted_converted


write_sorted_list()

# map(動作, 清單) = 「把這個動作，依序套用到清單裡的每一個元素上」。

# lambda 參數: 運算式 = 「寫在當下的免洗小函數，省去另外宣告 def 的麻煩」。

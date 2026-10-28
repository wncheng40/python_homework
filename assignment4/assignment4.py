'''
Task 1
'''
#1. Create a DataFrame from a dictionary:
from asyncio import taskgroups
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

#2. Add a new column: 
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)
# 3. Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)
# 4. Save the DataFrame as a CSV file:
task1_older.to_csv("employees.csv", index=False)



'''
Task 2 :Loading Data from CSV and JSON
'''
# 1. Load the employees.csv file created in Task 1 into a DataFrame
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

json_employees = pd.read_json("additional_employees.json")
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

'''
Task 3 : Basic Data Inspection
'''
# 1. Display the first three rows
print("\nDisplay the first three rows")
first_three = more_employees.head(3)
print(first_three)

# 2. Display the last two rows
print("\nDisplay the last two rows")
last_two = more_employees.tail(2)
print(last_two)

# 3. Display the shape of the DataFrame
print("\nDisplay the shape of the DataFrame")
employee_shape = more_employees.shape
print(employee_shape)

#4. Use the info() method to get a summary of the DataFrame
print("\nUse the info() method to get a summary of the DataFrame")
more_employees.info()

'''
Task 4: Data Cleaning and Preparation
'''
# 1. Load the dirty_data.csv file into a DataFrame
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)
dirty_data.info()
# copy DataFrame
clean_data = dirty_data.copy()


#2. Drop duplicate rows
print("\n----Drop duplicate rows----")
clean_data = clean_data.drop_duplicates()
print(clean_data)


#3. Convert Age column to numeric
print("\n----Convert Age column to numeric----")
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print(clean_data)


#4. Convert Salary column to numeric
print("\n----Convert Salary column to numeric----")
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
print(clean_data)


#5. Fill missing numeric values (use fillna).  
# Fill Age with the mean and Salary with the median 
print("\n----Fill missing numeric values----")
age_mean = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(age_mean)
salary_median = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(salary_median)  

print(clean_data)

#6. convert the hire date to datetime
print("\n----Convert Hire Date column to datetime----")
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], 
                                        format = 'mixed', 
                                        errors='coerce')

#7. Strip extra whitespace and standardize Name and Department as uppercase
print("\n----Strip extra whitespace and standardize Name and Department as uppercase----")
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print(clean_data)



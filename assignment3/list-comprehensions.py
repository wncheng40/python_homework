import csv

# 1. read csv
file_path = "../csv/employees.csv"
rows = []

with open(file_path, mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)

'''
2. Using a list comprehension, create a list of the employee names,
 first_name + space + last_name. The list comprehension should iterate 
 through the items in the list read from the csv file. Print the 
resulting list. Skip the item created for the heading of the csv file.
'''
# for row in rows[1:]: will skip the first row (heading)
full_names = [f"{row[1]} {row[2]}" for row in rows[1:]]

# Print the resulting list
print("--- all employee names ---")
print(full_names)

'''
3. Using a list comprehension, create another list from the previous 
list of names. This list should include only those names that contain 
the letter "e". Print this list.
'''
names_with_e = [name for name in full_names if "e" in name.lower()]
print("\nNames containing 'e' generated. Total:", len(names_with_e))
print(names_with_e)

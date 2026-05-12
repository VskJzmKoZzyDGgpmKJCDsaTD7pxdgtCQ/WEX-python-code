with open('names.txt', 'r') as file:
    names_string = file.read()

def convert_to_list(text):
    return [name.strip() for name in text.split(',') if name.strip()]

name_List = convert_to_list(names_string)
count = len(name_List)

num = int(input("Enter how many students you want per group: "))

print(f"You will have {count//num} groups of {num} and {count%num} students remaining. \n")

groups = count // num

import random

for i in range(groups):
    print(f"Group {i+1}:\n")
    for j in range(num):
        control_variable = random.choice(name_List)
        print(" ", control_variable)
        name_List.remove(control_variable)
    print("\n\n")

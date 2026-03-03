# Employee Details
empDetails={
    "emp1":{"experience": 7, "salary": 700000},
    "emp2":{"experience": 12, "salary": 2400000},
    "emp3":{"experience": 1, "salary": 300000},
    "emp4":{"experience": 0.6, "salary": 150000},
}

print("Current Employee Salaries: \n", empDetails) # This will print Current salary details of employees

print("\nAfter Bonus: \n")


for emp_id in empDetails:
    employees = empDetails[emp_id]

    # Calculate bonus based on experience
    if employees["experience"] >= 10:
        bonus = employees["salary"] * 0.20
    elif employees["experience"] >= 5:
        bonus = employees["salary"] * 0.10
    else:
        bonus = employees["salary"] * 0.05

    # Store bonus and updated salary
    employees["bonus"] = bonus
    employees["total_salary"] = employees["salary"] + bonus

    # print each employee details
    print(emp_id, ":", employees)

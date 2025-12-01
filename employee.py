def employee_info(name, emp_id, department, salary):
    result = (
        f"Employee_Name:{name}\n"
        f"Employee_ID:{emp_id}\n"
        f"Department:{department}\n"
        f"Salary:{salary}"
    )
    return result
if __name__ == "__main__":
    name="Alice\n"
    emp_id="E1001\n"
    department="IT\n"
    salary=55000
    print(employee_info(name,emp_id,department,salary))
    

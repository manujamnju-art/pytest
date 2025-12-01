from employee import employee_info
def test_employee_info():
   expected_output =(
      "Employee_Name:Alice\n"
      "Employee_ID:E1001\n"
      "Department:IT\n"
      "Salary:50000"
    )
   assert employee_info("Alice","E1001","IT",50000) == expected_output

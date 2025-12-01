from employee import employee_info
def test_employee_info():
   expected_output =(
      "Employee_Name:Alice\n"
      "Employee_ID:E123\n"
      "Department:IT\n"
      "Salary:50000"
    )
   assert employee_info("Alice","E1001","IT",55000) == expected_output

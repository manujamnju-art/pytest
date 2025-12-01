from employe import employe_info

def test_employe_info():
   
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E123\n"
        "Department: IT\n"
        "Salary: 50000"
    )

    
    assert employe_info("Alice", "E1001", "IT", 55000) == expected_output
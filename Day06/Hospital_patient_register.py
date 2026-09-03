import re

class Patient:
    _patient_counter=0
    

    @staticmethod
    def validate_dob_format(dob_str):
        pattern=r"^\d{4}-\d{2}-\d{2}$"
        
        if not re.match(pattern , dob_str):
            return False
        else:
            return True

    
    def __init__(self , name , dob ):
        
        if not Patient.validate_dob_format(dob):
            raise ValueError(f"Invalid date of birth format:{dob}. Expected YYYY-MM-DD.")
        
        Patient._patient_counter += 1
        
        self.patient_id=f"PAT-- {1000 + Patient._patient_counter}"
        
        
        self.name=name
        self.dob=dob
        
        
    def get_total_patients():
        return Patient._patient_counter
    
# 1. Valid Registration
p1 = Patient("Arham Khan", "1999-05-15")
print(p1.patient_id)  # Output: PAT-1001

# 2. Invalid DOB registration (throws ValueError)
try:
    p2 = Patient("Lisa", "12/08/1998")
except ValueError as e:
    print(e)  # Output: Invalid date of birth format: '12/08/1998'. Expected YYYY-MM-DD.

print(Patient.get_total_patients())  # Output: 1
#decryption.py
# Name: Brianna Jarrell, Leonie Troeger, Thomas Gilligan
# email: jarrelbc@mail.uc.edu, troegele@mail.uc.edu, gilligtp@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4-23-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:
# Citations:
# Anything else that's relevant:

import json 

class DecryptLocation:
    file_path = "..\\utilitiesPackage/EncryptedGroupHints Spring 2024 Section 002.json"
    with open(file_path, 'r') as file:
        location_data = json.load(file)
    name = location_data["Tricia McMillian"]
    
    print(name)
           

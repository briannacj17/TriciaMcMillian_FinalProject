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
from utilitiesPackage.EncryptedGroupHints_Spring_2024_Section_002 import *
from utiltilesPackage.UCEnglish import *

import json 

class DecryptLocation:
    def decrypt(self):
        with open("utiltiesPackage/EncryptedGroupHints_Spring_2024_Section_002.json", "r", encoding="utf-8") as file:
            location_data = json.load(file)

        # Search for the line containing "Tricia McMillian"
        for line in location_data:
            if "Tricia McMillian" in line:
                # Split the line by tab to extract the fields
                fields = line.strip().split("\t")
                # Extract the location
                location = fields[66]
                # Return the location
                return f"The location of Tricia McMillian is {location}."

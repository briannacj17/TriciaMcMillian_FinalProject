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

# Need to finish edititng to decrypt for Tricia McMillian 
class decrypt_location(EncryptedGroupHints_Spring_2024_Section_002.json, UCEnglish.txt):
    # Load encrypted data from JSON file
    with open(eEncryptedGroupHints_Spring_2024_Section_002.json, 'r') as f:
        encrypted_data = json.load(f)
    
    # Load English text file
    with open(UCEnglish.txt, 'r', encoding='utf-8') as f:
        english_text = f.readlines()
    
    # Decrypt location
    decrypted_location = "Tricia McMillian"
    for index in encrypted_data:
        line_number = int(index)
        decrypted_location += english_text[line_number - 1].strip() + " "

    return decrypted_location.strip()
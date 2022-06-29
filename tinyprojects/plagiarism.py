from difflib import SequenceMatcher

def plagiarism_checker(f1, f2):
    with open(f1, errors='ignore') as file1, open(f2, errors='ignore') as file2:
        f1_data = file1.read()
        f2_data = file2.read()
        res = SequenceMatcher(None, f1_data, f2_data).ratio()
        print(f"These files are {res*100} % similar")
        
f1= input("path for file1: ")
f2= input("path for file2: ")


plagiarism_checker(f1, f2)
import string

for letter in string.ascii_uppercase: 
    filename = f"letters/{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")  

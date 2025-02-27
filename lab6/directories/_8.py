import os
def delete_file(filepath):
    if not os.path.exists(filepath):
        print(f"File '{filepath}' does not exist.")
        return 
    
    if not os.access(filepath, os.R_OK or os.W_OK):
        print('no access')
        return
    
    os.remove(filepath)
    print(f"'{filepath}' has been deleted.")

file = "test.txt"
delete_file(file)

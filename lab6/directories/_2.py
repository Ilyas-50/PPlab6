import os

p = r"C:\Windows"
print(os.path.exists(p))
if os.access(p, os.R_OK):
    print("readable")
if os.access(p, os.W_OK):
    print("writable")
if os.access(p, os.X_OK):
    print("executable")

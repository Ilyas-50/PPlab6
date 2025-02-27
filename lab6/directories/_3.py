import os
path = r"C:\Users\user\Desktop\sem-1 (Operations on sets).pdf"

if os.path.exists(path):
    print("exist")
    print(os.path.dirname(path))
    print(os.path.basename(path))
else:
    print("does not exist")

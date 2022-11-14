import os

print(f"The files and folders in {os.getcwd()} are:")
items = os.listdir('.')
for item in items:
    prefix = "(d) " if os.path.isdir(item) else "(f) "
    print(f"{prefix}\t{item}")

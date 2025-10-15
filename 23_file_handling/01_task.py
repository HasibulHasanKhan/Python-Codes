import os

# Get the folder where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "hasib.txt")


if os.path.exists(file_path):
    print(f"The location '{file_path}' exists.")
else:
    print("That location doesn't exist.")

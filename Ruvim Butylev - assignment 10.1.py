import os
directory = input("Which directory would you like to save your file in? ")
os.path.isdir(directory)
name = input("What is your name? ")
address = input("What is your address? ")
phone_number = input("What is your phone number? ")
print("File Contents:")
with open(file, 'w') as file_object:
  file_object.write(name)
  file_object.write(" , ")
  file_object.write(address)
  file_object.write(" , ")
  file_object.write(phone_number)
with open(file, 'r') as file_object:
  data = file_object.read()
  print(data)
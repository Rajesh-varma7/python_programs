import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*_-+="

letters_count = int(input("How many letters you want in password"))
num_count = int(input("How many numbers you want in password"))
sym_count = int(input("How many symbols you want in password"))

password = ''

for i in range(1,letter_count+1):
  password += random.choice(letters)
for i in range(1,num_count+1):
  password += random.choice(numbers)
for i in range(1,sym_count+1):
  password += random.choice(symbols)

print(f"Your Password is {password}")

password_list = list(password)
random.shuffle(password_list)

advanced_password = ""
for ap in password_list:
  advanced_password += ap

print(f"Your Advanced Password is: {advanced_password}")

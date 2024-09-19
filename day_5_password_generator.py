import string
import random

lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to password generator!\n')
nr_passwords = int(input('Total password length!\n'))
nr_symbols = int(input('Total count of symbols in password!\n'))
nr_numbers = int(input('Total count of numbers in password!\n'))
nr_uppers = int(input('Total count of upper case letters in passwords!\n'))

password_list = []

for nr_number in range(nr_numbers):
    password_list.append(random.choice(numbers))
for nr_number in range(nr_symbols):
    password_list.append(random.choice(symbols))
for nr_upper in range(nr_uppers):
    password_list.append(random.choice(upper_letters))
for nr_lower in range(nr_passwords - nr_symbols - nr_numbers - nr_uppers):
    password_list.append(random.choice(lower_letters))

random.shuffle(password_list)
generated_password = ''.join(password_list)
print(f"Suggested password: {generated_password}")

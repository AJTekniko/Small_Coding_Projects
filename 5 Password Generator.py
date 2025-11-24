import string
import random

letters = []
for i in string.ascii_letters:
    letters.append(i)

symbols = []
for i in string.punctuation:
    symbols.append(i)

nums = []
for i in string.digits:
    nums.append(i)


print("""Welcome to the Password Generator!""")
num_letters = int(input("""How many letters would you like in
your password?"""))

num_symbols = int(input("How many symbols?"))

num_numbers = int(input("How many numbers?"))

password_list = []

for i in range(0, num_letters):
    password_list += random.choice(letters)

for i in range(0, num_symbols):
    password_list += random.choice(symbols)

for i in range(0, num_numbers):
    password_list += random.choice(nums)

random.shuffle(password_list)

password = ""
for i in password_list:
    password += i

print(f"""Your password:
{password}""")

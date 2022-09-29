import string
import random

password = string.ascii_lowercase + string.ascii_uppercase
count = 0
random_password = []

#generating the password

while count < 12:
    letter_to_add = random.choice(password)
    random_password.append(letter_to_add)
    count = count + 1

#converting list into string
final_password = ''.join(random_password)
print(final_password)
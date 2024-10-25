import random

elemets = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pass_lenght = int(input('Введите длину пароля'))

password = ''

for i in range(pass_lenght):
    password += random.choice(elemets)


    print(password)
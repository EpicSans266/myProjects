from random import choice

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pw_len = input()
password = ''

for i in range(pw_len):
  password += choice(symbol)

print('Ваш пароль:', password)

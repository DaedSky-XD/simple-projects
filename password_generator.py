import random

pswd_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
symbols = list(r"!@#$%^&*_'?.,<>:;")

include = input("[+] Do you want to include symbols in you passwd: (y/n): ").lower()
if include == "y":
    pswd_letters.extend(symbols)

pswd_len = int(input("how long password do you want: "))

for i in range(pswd_len):
    a = random.choice(pswd_letters)
    print(a, end="")
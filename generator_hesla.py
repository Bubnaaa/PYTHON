import random 

heslo: list[str] = []
velkepismeno1 = chr(random.randint(65, 90 ))
velkepismeno2 = chr(random.randint(65, 90 ))
malepismeno1 = chr(random.randint(97, 122 ))
malepismeno2 = chr(random.randint(97, 122 ))
malepismeno3 = chr(random.randint(97, 122 ))
malepismeno4 = chr(random.randint(97, 122 ))
nahodnyznak1 = chr(random.randint(43, 53 ))
nahodnyznak2 = chr(random.randint(43, 53 ))
cislo1 = random.randint(1, 9)
cislo2 = random.randint(1, 9)
cislo3 = random.randint(1, 9)


heslo = [velkepismeno1, velkepismeno2, malepismeno1, malepismeno2, malepismeno3, malepismeno4, nahodnyznak1, nahodnyznak2, cislo1, cislo2, cislo3]

random.shuffle(heslo)

for x in heslo:
    print(x, end =" ")
print()

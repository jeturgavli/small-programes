import random

piko = 'abcdefghijklmnopqrstuvwxyz0123456789'
land = list(piko)

password = str(input("password"))
lodo = ""
while(lodo != password):
    lodo = random.choices(land,k=len(password))
    print(lodo)
    lodo="".join(lodo)
print("/n loda taaro password aa che : " + lodo)
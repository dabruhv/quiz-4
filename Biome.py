# quiz-4
import random

i = 3
counter = 1



print("question 1)")
while i <= 21:
    print(i)
    i+=3

print("question 2)")

print("How many snurfle u want")

snurf = int(input())

while counter <= snurf:
    print("SUSUSUSUSUS")
    counter+=1
    
print("question 3)")

def gen(biome):
    if biome == 'd':
        desert = random.randrange(1,100)
        if desert <= 50:
            print("skeleton sus")
        elif desert > 50 and desert <=70:
            print("husk sus")
        elif desert > 70 and desert <=100:
            print("spider sus")
    if biome == 'f':
        field = random.randrange(1,100)
        if field <= 30:
            print("nothing sus")
        elif field > 30 and field <=60:
            print("zombie sus")
        elif field > 60 and field <=90:
            print("skeleton sus")
        elif field > 90:
            print("witch sus")
print("deserttttttttttttttttttttttttttttttttttttttttttttttttttttt")
for j in range(20):
    gen('d')

print("fielddddddddddddddddddddddddddddddddddddddddddddddddddd")
for j in range(20):
    gen('f')

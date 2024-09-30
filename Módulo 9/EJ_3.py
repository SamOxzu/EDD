ej1 = set()
ej2 = set()
ej3 = set()
ej4 = set()
ej5 = set()

for i in range (5):
    winners = int(input())
    for _ in range(winners):
        winner = input()
        if i == 0:
            ej1.add(winner)
        elif i == 1:
            ej2.add(winner)
        elif i == 2:
            ej3.add(winner)
        elif i == 3:
            ej4.add(winner)
        elif i == 4:
            ej5.add(winner)

abs_winners = ej1.intersection(ej2).intersection(ej3).intersection(ej4).intersection(ej5)
if abs_winners:
    print(1000000//len(abs_winners))
else:
    print("Nadie gana")
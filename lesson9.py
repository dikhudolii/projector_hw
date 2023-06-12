# -1 cat without hat; 1 - with hat

rounds = 100
number_of_cats = 100

cats = [-1 for _ in range(number_of_cats)]


for round in range(1, 1 + rounds):
    for cat in range(0, number_of_cats, round):
        cats[cat] *= -1


for cat in range(len(cats)):
    print(f'Cat number {cat} have a cap: {cats[cat] == 1}')


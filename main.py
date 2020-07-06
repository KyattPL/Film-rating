import matplotlib.pyplot as plt

data = []
names = {'1': 0, '1.5': 0, '2': 0, '2.5': 0, '3': 0, '3.5': 0, '4': 0, '4.5': 0, '5': 0,
         '5.5': 0, '6': 0, '6.5': 0, '7': 0, '7.5': 0, '8': 0, '8.5': 0, '9': 0, '9.5': 0, '10': 0}

with open("rating.txt", encoding="utf8") as file:
    data = file.read().splitlines()

tuples = []

for line in data:
    tuples.append(line.split('-'))

rating = []

for lis in tuples:
    print(lis[0] + ", rating: " + lis[1], end='')
    names[lis[1].split('/')[0].strip()] += 1
    if len(lis) > 2:
        print(", comment: " + lis[2])
        continue
    print()

fig, ax = plt.subplots()
ax.plot(list(names.keys()), list(names.values()))

ax.set(xlabel="Ocena (1-10)", ylabel="Liczba filmów", title="Wykaz filmów")
ax.grid()

fig.savefig("test.png")
plt.show()

import matplotlib.pyplot as plt

films = []
ratings = {'1': 0, '1.5': 0, '2': 0, '2.5': 0, '3': 0, '3.5': 0, '4': 0, '4.5': 0, '5': 0,
           '5.5': 0, '6': 0, '6.5': 0, '7': 0, '7.5': 0, '8': 0, '8.5': 0, '9': 0, '9.5': 0, '10': 0}


def print_graph():

    for k in ratings.keys():
        ratings[k] = 0

    for film in films:
        ratings[film[2].split('/')[0].strip()] += 1

    fig, ax = plt.subplots()
    ax.plot(list(ratings.keys()), list(ratings.values()))

    ax.set(xlabel="Rating (1-10)", ylabel="Number of films",
           title="Distribution of films by rating")
    ax.grid()

    fig.savefig("test.png")
    plt.show()


def read_data():
    with open("rating.txt", "r", encoding="utf8") as file:
        data = file.read().splitlines()

    for line in data:
        films.append(line.split('-'))


def print_films():
    for film in films:
        print(film[0] + ", year:" + film[1] + ", rating:" + film[2], end='')
        if len(film) > 3:
            print(", comment: " + film[3])
            continue
        print()


def search(input, flag):
    index = 0
    if flag == 2:
        index = 1
    elif flag == 3:
        index = 2
    for film in films:
        if film[index].strip().lower() == input.strip().lower() and index != 0:
            print(film[0] + ", year:" + film[1] +
                  ", rating:" + film[2], end='')
            if len(film) > 3:
                print(", comment: " + film[3])
                continue
            print()
        elif film[index].strip().lower().startswith(input.strip().lower()):
            print(film[0] + ", year:" + film[1] +
                  ", rating:" + film[2], end='')
            if len(film) > 3:
                print(", comment: " + film[3])
                continue
            print()


def add_film():
    name = input("Name of the film: ")
    year = input("Year of production: ")
    rating = input("Rating (out of 10): ")
    comment = input("Comment (optional): ").strip()
    rating = rating.replace(",", ".")
    rating += "/10"
    line = name + " - " + year + " - " + rating
    if len(comment) >= 1:
        line += " - " + comment
    films.append(line.split("-"))
    with open("rating.txt", "a", encoding="utf8") as file:
        file.write("\n" + line)


def remove_film(name):
    choices = []
    for (index, film) in enumerate(films):
        if film[0].strip().lower().startswith(name):
            choices.append(index)
            print(str(index + 1) + ". ", end='')
            print(film[0] + ", year:" + film[1] +
                  ", rating:" + film[2], end='')
            if len(film) > 3:
                print(", comment: " + film[3])
                continue
            print()
    deleted = input("What film would you like to delete?: ")
    deleted = int(deleted.strip()) - 1
    if deleted in choices:
        films.pop(deleted)
        with open("rating.txt", "r+", encoding="utf8") as file:
            d = file.readlines()
            file.seek(0)
            for i in d:
                if deleted != 0:
                    file.write(i)
                deleted -= 1
            file.truncate()
    last_line = ""
    with open("rating.txt", "r", encoding="utf8") as file:
        for line in file:
            if line:
                last_line = line
    if last_line.endswith("\n"):
        with open("rating.txt", "rb+") as file:
            file.seek(0, 2)
            size = file.tell()
            file.truncate(size - 2)


if __name__ == "__main__":
    read_data()
    while True:
        print("1. Print all the films")
        print("2. Show graph of ratings")
        print("3. Search by name")
        print("4. Search by year")
        print("5. Search by rating")
        print("6. Add a new film")
        print("7. Delete the film")
        print("9. Exit")
        choice = int(input("").strip())
        if choice == 1:
            print_films()
        elif choice == 2:
            print_graph()
        elif choice == 3:
            temp = input("Name of the film: ")
            search(temp, 1)
        elif choice == 4:
            temp = input("Year of production: ")
            search(temp, 2)
        elif choice == 5:
            temp = input("Rating (out of 10): ")
            temp = temp.replace(",", ".")
            temp += "/10"
            search(temp, 3)
        elif choice == 6:
            add_film()
        elif choice == 7:
            name = input("Name of the film to remove: ").strip().lower()
            remove_film(name)
        elif choice == 9:
            break

import json

def persons_file(N):
    persons = []
    ID_counter = 0

    for i in range(N):
        name = input("Enter name: ")
        while True:
            try:
                age = int(input("Enter age: "))
                break
            except ValueError or TypeError:
                print("Please insert only integers")

        ID_counter =+ 1
        persons.append({"ID":ID_counter,"Name":name, "Age":age})
    print(persons)

    with open("persons.json", "w+") as file:
        json.dump(persons, file, indent=4)


persons_file(int(input("Enter the number of persons: ")))

# Fast i Källaren - Textbaserat äventyrsspel
import random

class Room:
    def __init__(self, description, items):
        self.description = description
        self.items = items

    def search(self):
        if self.items:
            item = self.items.pop()
            print(f"Du hittar {item}!")
            return item
        else:
            print("Du hittar inget av värde.")
            return None

def show_main_menu():
    print("\nHuvudmeny")
    print("1. Starta spelet")
    print("2. Välj svårighetsgrad")
    print("3. Avsluta spelet")

def show_difficulty_menu():
    print("\nVälj svårighetsgrad")
    print("1. Lätt")
    print("2. Medel")
    print("3. Svår")

def main():
    while True:
        show_main_menu()
        choice = input("Ange ditt val (1-3): ")

        if choice == "1":
            start_game()
        elif choice == "2":
            show_difficulty_menu()
            difficulty_choice = input("Ange svårighetsgrad (1-3): ")
            set_difficulty(difficulty_choice)
        elif choice == "3":
            print("Spelet avslutas.")
            break
        else:
            print("Ogiltigt val. Försök igen.")

def set_difficulty(choice):
    if choice == "1":
        print("Svårighetsgrad satt till Lätt.")
    elif choice == "2":
        print("Svårighetsgrad satt till Medel.")
    elif choice == "3":
        print("Svårighetsgrad satt till Svår.")
    else:
        print("Ogiltigt val. Svårighetsgrad satt till Medel som standard.")

def start_game():
    rooms = [
        Room("\nDu vaknar upp i ett mörkt och kallt rum. Du är fast bunden i kedja till en stång.", ["en nyckel"]),
        Room("\nDu är i ett fuktigt rum med steniga väggar.", ["en ficklampa"]),
        Room("\nDu befinner dig i ett rum fyllt med gamla möbler.", ["en kniv"]),
        Room("\nDu är i ett rum med en låst dörr.", [])
    ]

    current_room = 0
    inventory = []

    while True:
        print(rooms[current_room].description)
        print("Vad vill du göra?")
        print("1. Letar i rummet")
        print("2. Använd föremålet för att försöka fly")
        print("3. Smyg dig ut försiktigt")
        print("4. Ge upp")

        choice = input("Ange ditt val (1-4): ")

        if choice == "1":
            item = rooms[current_room].search()
            if item:
                inventory.append(item)
        elif choice == "2":
            if "en nyckel" in inventory and current_room == 3:
                print("Du använder nyckeln för att låsa upp dörren och fly!")
                break
            else:
                print("Du har inget användbart föremål för att fly.")
        elif choice == "3":
            if current_room < len(rooms) - 1:
                current_room += 1
                print("Du smyger dig till nästa rum.")
            else:
                print("Det finns inga fler rum att smyga till.")
        elif choice == "4":
            print("Du ger upp och förblir fast i källaren.")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()
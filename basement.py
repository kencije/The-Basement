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
    print("3. Läs Instruktioner")
    print("4. Avsluta spelet")

def show_difficulty_menu():
    print("\nVälj svårighetsgrad")
    print("1. Lätt")
    print("2. Medel")
    print("3. Svår")

def read_readme():
    try:
        with open("readme.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print("\nInnehåll i readme.txt:\n")
            print(content)
    except FileNotFoundError:
        print("Filen readme.txt hittades inte.")

def main():
    difficulty = "Medel"

    while True:
        show_main_menu()
        choice = input("Ange ditt val (1-4): ")

        if choice == "1":
            start_game(difficulty)
        elif choice == "2":
            show_difficulty_menu()
            difficulty_choice = input("Ange svårighetsgrad (1-3): ")
            difficulty = set_difficulty(difficulty_choice)
        elif choice == "3":
            read_readme()
        elif choice == "4":
            print("Spelet avslutas.")
            break
        else:
            print("Ogiltigt val. Försök igen.")

def set_difficulty(choice):
    if choice == "1":
        print("Svårighetsgrad satt till Lätt.")
        return "Lätt"
    elif choice == "2":
        print("Svårighetsgrad satt till Medel.")
        return "Medel"
    elif choice == "3":
        print("Svårighetsgrad satt till Svår.")
        return "Svår"
    else:
        print("Ogiltigt val. Svårighetsgrad satt till Medel som standard.")
        return "Medel"

def start_game(difficulty):
    rooms = [
        Room("\nDu vaknar upp i ett mörkt och kallt rum. Du är fast bunden i kedja till en stång.", ["en nyckel"]),
        Room("\nDu är i ett fuktigt rum med steniga väggar.", ["en ficklampa"]),
        Room("\nDu befinner dig i ett rum fyllt med gamla möbler.", ["en kniv"]),
        Room("\nDu är i ett rum med en låst dörr.", []),
        Room("\nDu är i ett rum med gamla böcker och papper.", ["en karta"]),
        Room("\nDu är i ett rum med trasiga möbler och skräp.", ["en skruvmejsel"])
    ]

    current_room = 0
    inventory = []
    key_room = random.randint(0, len(rooms) - 1)
    debuff = False

    while True:
        print(rooms[current_room].description)
        print("\nVad vill du göra?")
        print("1. Letar i rummet")
        print("2. Använd föremålet för att försöka fly")
        print("3. Smyg dig ut försiktigt")
        print("4. Visa inventariet")
        print("5. Ge upp")

        choice = input("Ange ditt val (1-5): ")

        if choice == "1":
            item = rooms[current_room].search()
            if item:
                inventory.append(item)
        elif choice == "2":
            if "en nyckel" in inventory and current_room == key_room:
                print("Du använder nyckeln för att låsa upp dörren och fly!")
                break
            elif "en kniv" in inventory:
                print("Du använder kniven för att försvara dig!")
                combat(inventory, debuff)
            else:
                print("Du har inget användbart föremål för att fly.")
        elif choice == "3":
            if "en ficklampa" in inventory:
                print("Ficklampan gör det lättare att se, men du kan bli upptäckt lättare.")
                if random.random() < 0.5:
                    print("Du blev upptäckt!")
                    combat(inventory, debuff)
                else:
                    print("Du smyger dig till nästa rum.")
                    if current_room < len(rooms) - 1:
                        current_room += 1
                    else:
                        print("Det finns inga fler rum att smyga till.")
            else:
                print("Du smyger dig till nästa rum.")
                if current_room < len(rooms) - 1:
                    current_room += 1
                else:
                    print("Det finns inga fler rum att smyga till.")
        elif choice == "4":
            print("Ditt inventarie innehåller:")
            for item in inventory:
                print(f"- {item}")
        elif choice == "5":
            print("Du ger upp och förblir fast i källaren.")
            break
        else:
            print("Ogiltigt val. Försök igen.")

        if random.random() < 0.1:
            print("Du snubblar och gör ett ljud!")
            if random.random() < 0.5:
                print("Kidnapparen hörde dig!")
                combat(inventory, debuff)
            else:
                print("Du lyckades återhämta dig utan att bli upptäckt.")
            debuff = True

def combat(inventory, debuff):
    print("Du är i strid!")
    while True:
        print("\nVad vill du göra?")
        print("1. Attackera")
        print("2. Försvara")
        print("3. Försök att fly")

        choice = input("Ange ditt val (1-3): ")

        if choice == "1":
            if "en kniv" in inventory:
                print("Du attackerar med kniven!")
                if random.random() < 0.7:
                    print("Du vann striden!")
                    break
                else:
                    print("Du misslyckades med att attackera!")
            else:
                print("Du har inget vapen att attackera med!")
        elif choice == "2":
            print("Du försvarar dig!")
            if random.random() < 0.5:
                print("Du lyckades försvara dig!")
            else:
                print("Du misslyckades med att försvara dig!")
        elif choice == "3":
            print("Du försöker fly!")
            if random.random() < 0.5:
                print("Du lyckades fly!")
                break
            else:
                print("Du snubblade och föll!")
                debuff = True
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()
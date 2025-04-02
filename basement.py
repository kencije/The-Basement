import random

# Klass för att representera ett rum
class Room:
    def __init__(self, description, items):
        self.description = description
        self.items = items

    # Metod för att söka i rummet efter föremål
    def search(self):
        if self.items:
            item = self.items.pop()
            print(f"Du hittar {item}!")
            return item
        else:
            print("Du hittar inget av värde.")
            return None

# Funktion för att visa huvudmenyn
def show_main_menu():
    print("\nHuvudmeny")
    print("1. Starta spelet")
    print("2. Välj svårighetsgrad")
    print("3. Läs Instruktioner")
    print("4. Avsluta spelet")

# Funktion för att visa menyn för att välja svårighetsgrad
def show_difficulty_menu():
    print("\nVälj svårighetsgrad")
    print("1. Lätt")
    print("2. Medel")
    print("3. Svår")

# Funktion för att läsa innehållet i readme.txt
def read_readme():
    try:
        with open("readme.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print("\nInnehåll i readme.txt:\n")
            print(content)
    except FileNotFoundError:
        print("Filen readme.txt hittades inte.")

# Huvudfunktion för spelet
def main():
    difficulty = "Medel"  # Standard svårighetsgrad

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

# Funktion för att sätta svårighetsgraden
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

# Funktion för att starta spelet
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
    key_room = random.randint(0, len(rooms) - 1)  # Slumpmässigt rum för att använda nyckeln
    player_hp = 100
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
                player_hp = combat(inventory, player_hp, debuff)
            else:
                print("Du har inget användbart föremål för att fly.")
        elif choice == "3":
            if "en ficklampa" in inventory:
                print("Ficklampan gör det lättare att se, men du kan bli upptäckt lättare.")
                if random.random() < 0.5:  # 50% chans att bli upptäckt
                    print("Du blev upptäckt!")
                    player_hp = combat(inventory, player_hp, debuff)
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

        # Slumpmässig chans att snubbla och larma kidnapparen
        if random.random() < 0.1:  # 10% chans att snubbla
            print("Du snubblar och gör ett ljud!")
            if random.random() < 0.5:  # 50% chans att larma kidnapparen
                print("Kidnapparen hörde dig!")
                player_hp = combat(inventory, player_hp, debuff)
            else:
                print("Du lyckades återhämta dig utan att bli upptäckt.")
            debuff = True  # Tillämpa debuff

# Funktion för stridssystemet
def combat(inventory, player_hp, debuff):
    kidnapper_hp = 100
    while player_hp > 0 and kidnapper_hp > 0:
        print("\nDu är i strid!")
        print(f"Din HP: {player_hp}")
        print(f"Kidnapparens HP: {kidnapper_hp}")
        print("\nVad vill du göra?")
        print("1. Blockera")
        print("2. Boxa")
        print("3. Sparka")
        print("4. Skallning")
        print("5. Försök att fly")

        choice = input("Ange ditt val (1-5): ")

        if choice == "1":
            print("Du försöker blockera!")
            if random.random() < 0.6:  # 60% chans att lyckas blockera
                print("Du lyckades blockera attacken!")
            else:
                print("Du misslyckades med att blockera!")
                player_hp -= 10
        elif choice == "2":
            print("Du försöker boxa!")
            if random.random() < 0.5:  # 50% chans att lyckas boxa
                print("Du träffade!")
                kidnapper_hp -= 10
            else:
                print("Du missade!")
        elif choice == "3":
            print("Du försöker sparka!")
            if random.random() < 0.4:  # 40% chans att lyckas sparka
                print("Du träffade med en spark!")
                kidnapper_hp -= 20
            else:
                print("Du missade!")
        elif choice == "4":
            print("Du försöker skallning!")
            if random.random() < 0.1:  # 10% chans att lyckas med skallning
                print("Du träffade med en skallning!")
                kidnapper_hp -= 50
                if random.random() < 0.5:  # 50% chans att slå ut kidnapparen
                    print("Kidnapparen blev medvetslös!")
                    break
            else:
                print("Du missade!")
        elif choice == "5":
            print("Du försöker fly!")
            if random.random() < 0.5:  # 50% chans att lyckas fly
                print("Du lyckades fly!")
                break
            else:
                print("Du snubblade och föll!")
                player_hp -= 10
                debuff = True  # Tillämpa debuff
        else:
            print("Ogiltigt val. Försök igen.")

        # Kidnapparen attackerar om inte utslagen
        if kidnapper_hp > 0:
            print("Kidnapparen attackerar!")
            if random.random() < 0.5:  # 50% chans att träffa
                print("Kidnapparen träffade dig!")
                player_hp -= 10
            else:
                print("Kidnapparen missade!")

    if player_hp <= 0:
        print("Du förlorade striden och blev fångad igen.")
    elif kidnapper_hp <= 0:
        print("Du besegrade kidnapparen!")

    return player_hp

if __name__ == "__main__":
    main()
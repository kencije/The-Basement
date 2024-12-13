# Fast i Källaren - Textbaserat äventyrsspel
import random

def main():
    print("Du vaknar upp i ett mörkt och kallt rum")
    print("Du är fast bunden i kedja till en stång")
    print()

    while True:
        print("Vad vill du göra?")
        print("1. Letar i rummet")
        print("2. Använd föremålet för att försöka fly")
        print("3. Smyg dig ut försiktigt")
        print("4. Ge upp")

        choice = input("Ange ditt val (1-4): ")

        if choice == "1":
            print("Letar i rummet...")
            print("Lyckas hitta ett föremål som kan användas för att fly!")
        elif choice == "2":
            print("Använder föremålet för att försöka fly...")
            print("Fortsätter leta...")
        elif choice == "3":
            print("Smyger dig ut försiktigt...")
            print("Smyger dig ut")
            print("Spring ut direkt")
            print("Hör ljud")
            print("Hittar föremål för att fly")
            print("Känsla av panik")
            print("Hon kan komma tillbaka när som helst")
            print("Du är ute, men hör hennes röst i fjärran")
            print("Vad ska du göra nu...?")
            break
        elif choice == "4":
            print("Du ger upp och förblir fast i källaren.")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()
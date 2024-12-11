import random

print("Du vaknar upp i en okänd mörk plats...")
input("...")

print("Du är yr och vet inte vart du är...")
input("...")

print("Du ser en dörr som är låst. Vad vill du göra?")
choice = input("(1. Försök bryta kedjan, 2. Leta i rummet): ")

if choice == "1":
    print("Du försöker bryta kedjan, men den är för stark. Du lyckas inte.")
    print("Vad gör du nu?")
    choice2 = input("(1. Leta i rummet, 2. Smyg dig ut försiktigt): ")

if choice2 == "1":
        print("Du letar i rummet och hittar ett föremål som kan hjälpa dig att fly.")
        print("Du använder föremålet för att försöka fly.")
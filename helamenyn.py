# Function to show menu
def show_menu():
    print()
    print("=============================")
    print()
    print("1. Starta övervakning")
    print("2. Lista aktiv övervakning")
    print("3. Skapa larm")
    print("4. Visa larm")
    print("5. Starta övervakningsläge")
    print("6. Stäng programmet")
    print()
    print()

def start_monitor():
    print(f"A string is a datatype that is used to store text. Example of a string is 'Hello World'")

def show_active_monitor():
    print(f"En int(integer) är en datatyp som används för att lagra heltal. Exempel på en integer är: 42")

def create_alarm():
    print(f"En bool(boolean) är en datatyp som används för att lagra sant eller falskt. Värdena är således antingen True eller False")

def show_alarm():
    print(f"En float är en datatyp som används för att lagra decimaltal. Exempel på en float är: 3.14")

def start_monitor_mode():
    print(f"En complex är en datatyp som används för att lagra komplexa tal. Exempel på en complex är: 1 + 5j")

def close():
    print("Programmet avslutas.")
    exit()

# A loop to show the start/main menu
def main_menu():
    while True:
        show_menu()
        userChoice = input("Välj ett alternativ i menyn: ")
        if userChoice == "1":
            start_monitor()
            print()
            input("Tryck på valfri tangent för att gå tillbaka till menyn.")
            print()

        elif userChoice == "2":
            show_active_monitor()
            print()
            input("Tryck på valfri tangent för att gå tillbaka till huvudmenyn.")
            print()

        elif userChoice == "3":
            create_alarm()
            print()
            input("Tryck på valfri tangent för att gå tillbaka till huvudmenyn.")
            print()

        elif userChoice == "4":
            show_alarm()
            print()
            input("Tryck på valfri tangent för att gå tillbaka till huvudmenyn.")
            print()
        
        elif userChoice == "5":
            start_monitor_mode()
            print()
            input("Tryck på valfri tangent för att gå tillbaka till huvudmenyn.")
            print()

        elif userChoice == "6":
            close()
        
        else:
            print("Felaktig inmatning. Försök igen")
            print()
            print()

# Launch program
print("==== VÄLKOMMEN TILL PROGRAMMET ====")
print("Välj vad du vill göra genom att mata in rätt nummer i menyn.")
print()
main_menu()
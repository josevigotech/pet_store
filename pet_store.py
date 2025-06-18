
from datetime import datetime

print("**********************************")
print("****     WELCOME TO THE      *****")
print("****      PET STORE!        *****")
print("**********************************")

inventory = {
    "dog": 10,
    "cat": 8,
    "bird": 25,
    "iguana": 2
}

total_animals = 0
for val in inventory.values():
    total_animals += val

print("Enter your first name: ")
first_name = input()
print("Enter your last name: ")
last_name = input()

full_name = first_name + " " + last_name

print("Thank you for visiting us,", full_name)

purchases = []

def show_menu():
    print("")
    print("=================================================")
    print("Choose an option:")
    print("1: See how many animals are in the store")
    print("2: Buy an animal")
    print("3: Show purchases")
    print("4: Exit the program")

def show_inventory():
     print("**** INVENTORY ****")
     for key, value in inventory.items():
         print(f"     {key}: {value}")
     print("We have a total of", total_animals, "animals in our inventory.")

def buy_animal():
     cart = []

     while True:
        print("Which animal would you like to buy? You can choose only 1 of each species.")
        print("Type F to finish your list, or V to view your cart.")
        animal = input()
        if animal == "F": break

        if animal == "V":
            print(f"Your shopping cart contains: {cart}")
            continue

        if animal not in inventory:
            print(f"Sorry, we do not have the animal {animal}.")
        elif inventory[animal] == 0:
            print(f"Sorry, {animal} is out of stock.")
        elif animal not in cart:
            cart.append(animal)
        else:
            print("That animal is already in your cart.")

     print("Your shopping cart contains:")
     for animal in cart: 
         print("   ", animal)
         inventory[animal] -= 1

     date = datetime.now()
     purchases.append((full_name, cart, date))

def show_purchases():
    print("")
    print("***** PURCHASE HISTORY *****")
    for purchase in purchases:
        print(f"{purchase[0]} bought {purchase[1]} on {purchase[2]}")

while True:
    show_menu()
    choice = int(input())

    if choice == 1:
        show_inventory()
    elif choice == 2:
        buy_animal()
    elif choice == 3:
        show_purchases()
    elif choice == 4:
        print("Exiting the program.")
        break

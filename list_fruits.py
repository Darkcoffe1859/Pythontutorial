import csv
import os

# File to store fruits
FILENAME = "fruits.csv"

# Fruit class
class Fruit:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Fruit: {self.name}")

# List to store fruits
fruits = []

# Load fruits from CSV file
def load_fruits():
    if os.path.exists(FILENAME):
        with open(FILENAME, newline='', mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # skip empty rows
                    fruit = Fruit(row[0])
                    fruits.append(fruit)

# Save fruits to CSV file
def save_fruits():
    with open(FILENAME, newline='', mode="w") as file:
        writer = csv.writer(file)
        for fruit in fruits:
            writer.writerow([fruit.name])

# Add a new fruit
def add_fruits():
    print("\nAdd New Fruit")
    name = input("Enter name of fruit: ")
    fruit = Fruit(name)
    fruits.append(fruit)
    save_fruits()
    print("Fruit added successfully!")

# View all fruits
def view_fruits():
    if not fruits:
        print("No fruits to show.")
    else:
        print("\nFruits List:")
        for i, fruit in enumerate(fruits, 1):
            print(f"{i}. ", end="")
            fruit.display()

# Search for a fruit
def search_fruit():
    name_to_find = input("Enter fruit to search: ")
    found = False
    for fruit in fruits:
        if fruit.name.lower() == name_to_find.lower():
            fruit.display()
            found = True
            break
    if not found:
        print("Fruit not found.")

# Delete a fruit
def delete_fruit():
    name_to_delete = input("Enter fruit name to delete: ")
    for fruit in fruits:
        if fruit.name.lower() == name_to_delete.lower():
            fruits.remove(fruit)
            save_fruits()
            print(f"{fruit.name} deleted.")
            return
    print("Fruit not found.")

# Update a fruit
def update_fruit():
    name_to_update = input("Enter fruit name to update: ")
    for fruit in fruits:
        if fruit.name.lower() == name_to_update.lower():
            new_name = input("Enter new name: ")
            fruit.name = new_name
            save_fruits()
            print("Fruit updated.")
            return
    print("Fruit not found.")

# Load fruits when program starts
load_fruits()

# Main menu loop
while True:
    print("\n=== Fruit Tracker ===")
    print("1. Add Fruit")
    print("2. View Fruits")
    print("3. Search Fruit")
    print("4. Delete Fruit")
    print("5. Update Fruit")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_fruits()
    elif choice == "2":
        view_fruits()
    elif choice == "3":
        search_fruit()
    elif choice == "4":
        delete_fruit()
    elif choice == "5":
        update_fruit()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

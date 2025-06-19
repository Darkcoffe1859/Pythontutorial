import json

FILENAME = "restaurants.json"
restaurants = []

# Function to load existing data from file
def load_data():
    global restaurants
    try:
        with open(FILENAME, "r") as file:
            restaurants = json.load(file)
    except FileNotFoundError:
        restaurants = []
    except json.JSONDecodeError:
        restaurants = []

# Function to save current data to file
def save_data():
    with open(FILENAME, "w") as file:
        json.dump(restaurants, file, indent=4)

# Function to add a restaurant
def add_restaurant():
    name = input("Enter the name of the restaurant: ")
    location = input("Enter the location: ")
    food_type = input("Enter type of food (e.g., Chinese, Nigerian, Italian): ")

    try:
        rating = int(input("Enter your rating (1 to 5): "))
        if rating < 1 or rating > 5:
            print("❌ Rating must be between 1 and 5.")
            return
    except ValueError:
        print("❌ Please enter a valid number for rating.")
        return

    restaurant = {
        "name": name,
        "location": location,
        "food_type": food_type,
        "rating": rating
    }

    restaurants.append(restaurant)
    save_data()
    print("✅ Restaurant added successfully!")

# Function to view all restaurants
def view_restaurants():
    if not restaurants:
        print("📭 No restaurants added yet.")
    else:
        print("\n📋 Your Restaurant Collection:")
        for i, restaurant in enumerate(restaurants, 1):
            print(f"{i}. {restaurant['name']} - {restaurant['food_type']} food in {restaurant['location']} (Rating: {restaurant['rating']}/5)")

# Function to search restaurants by name
def search_restaurant():
    keyword = input("Enter the name to search for: ").lower()
    found = False
    for restaurant in restaurants:
        if keyword in restaurant['name'].lower():
            print(f"✅ Found: {restaurant['name']} in {restaurant['location']} - {restaurant['food_type']} (Rating: {restaurant['rating']}/5)")
            found = True
    if not found:
        print("❌ No matching restaurant found.")

# Main program
def main():
    load_data()
    while True:
        print("\n🍽️ Restaurant Tracker")
        print("1. Add Restaurant")
        print("2. View Restaurants")
        print("3. Search Restaurant")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            add_restaurant()
        elif choice == "2":
            view_restaurants()
        elif choice == "3":
            search_restaurant()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1, 2, 3 or 4.")

# Run the program
if __name__ == "__main__":
    main()

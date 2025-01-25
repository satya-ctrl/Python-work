import os
import json

DATA_DIR = "data"

def create_data_dir():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

def save_data(filename, data):
    with open(os.path.join(DATA_DIR, filename), "w") as file:
        json.dump(data, file)

def load_data(filename, default=[]):
    data_file = os.path.join(DATA_DIR, filename)
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    else:
        return default

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("Dietitian Record Management System")
    print("1. Add Client")
    print("2. Update Client")
    print("3. View Client")
    print("4. Add Diet for Client")
    print("5. View Diet for Client")
    print("6. Exit")

def add_client():
    client_data = load_data("clients.json")
    name = input("Enter client name: ")
    age = input("Enter client age: ")
    contact = input("Enter client contact details: ")
    weight = input("Enter client weight: ")
    height = input("Enter client height: ")

    client_data.append({
        "name": name,
        "age": age,
        "contact": contact,
        "weight": weight,
        "height": height
    })

    save_data("clients.json", client_data)
    print("Client added successfully!")

def update_client():
    client_data = load_data("clients.json")
    name = input("Enter client name to update: ")
    for client in client_data:
        if client["name"] == name:
            client["name"] = input("Enter new name (leave empty to keep the same): ") or client["name"]
            client["age"] = input("Enter new age (leave empty to keep the same): ") or client["age"]
            client["contact"] = input("Enter new contact details (leave empty to keep the same): ") or client["contact"]
            client["weight"] = input("Enter new weight (leave empty to keep the same): ") or client["weight"]
            client["height"] = input("Enter new height (leave empty to keep the same): ") or client["height"]
            save_data("clients.json", client_data)
            print("Client information updated successfully.")
            return
    print("Client not found.")

def view_client():
    client_data = load_data("clients.json")
    name = input("Enter client name to view: ")
    for client in client_data:
        if client["name"] == name:
            print("Client Information:")
            print(f"Name: {client['name']}")
            print(f"Age: {client['age']}")
            print(f"Contact: {client['contact']}")
            print(f"Weight: {client['weight']}")
            print(f"Height: {client['height']}")
            return
    print("Client not found.")

def add_diet_for_client():
    client_data = load_data("clients.json")
    name = input("Enter client name to add diet for: ")
    
    for client in client_data:
        if client["name"] == name:
            diet = input("Enter diet information for the client: ")
            # Add the diet information to the client's data structure
            client["diet"] = diet
            save_data("clients.json", client_data)
            print("Diet information added successfully.")
            return
    print("Client not found.")

def view_diet_for_client():
    client_data = load_data("clients.json")
    name = input("Enter client name to view diet for: ")
    
    for client in client_data:
        if client["name"] == name:
            if "diet" in client:
                print("Diet Information:")
                print(f"Name: {client['name']}")
                print(f"Diet: {client['diet']}")
            else:
                print("No diet information found for this client.")
            return
    print("Client not found.")

if __name__ == "__main__":
    create_data_dir()
    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_client()
        elif choice == "2":
            update_client()
        elif choice == "3":
            view_client()
        elif choice == "4":
            add_diet_for_client()
        elif choice == "5":
            view_diet_for_client()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        input("Press Enter to continue...")

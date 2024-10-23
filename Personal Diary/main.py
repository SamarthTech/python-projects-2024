import datetime
import os

# Function to write a new diary entry
def write_entry():
    entry = input("Enter your diary entry: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append the new entry with timestamp to the diary file
    with open("diary.txt", "a") as file:
        file.write(f"{timestamp}: {entry}\n")
    print("Diary entry saved!")

# Function to read all diary entries
def read_entries():
    if os.path.exists("diary.txt"):
        print("\n--- Your Diary Entries ---")
        with open("diary.txt", "r") as file:
            for line in file:
                print(line.strip())
        print("--------------------------")
    else:
        print("No diary entries found!")

# Function to delete all diary entries
def delete_entries():
    if os.path.exists("diary.txt"):
        os.remove("diary.txt")
        print("All diary entries deleted!")
    else:
        print("No diary entries to delete!")

# Menu to choose actions
def menu():
    while True:
        print("\n--- Personal Diary ---")
        print("1. Write a new entry")
        print("2. Read all entries")
        print("3. Delete all entries")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            delete_entries()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the diary application
menu()

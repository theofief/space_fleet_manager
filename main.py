import json, random, atexit
from fleet import Fleet
from spaceship import Spaceship
from crew import Crew
from Operator import Operator
from mentalist import Mentalist
from member import Member

global game_settings, fleet_manager
game_settings = {}

def initialize_json_file():
    """Initialize the JSON file if it doesn't exist."""
    default_data = {
        "settings": {
            "auto_save_on_exit": True,
            "auto_load": True
        },
        "fleet_name": "",
        "spaceships": []
    }
    try:
        with open("fleet.json", "x") as f:
            json.dump(default_data, f, indent=4)
    except FileExistsError:
        return

def get_settings():
    global game_settings
    try:
        with open("fleet.json", "r") as f:
            fleet_data = json.load(f)
            for setting in fleet_data["settings"]:
                game_settings[setting] = fleet_data["settings"][setting]
    except FileNotFoundError:
        print("No settings file found. Using default settings.")
        
def reset_data():
    global game_settings
    game_settings = {
        "auto_save_on_exit": True,
        "auto_load": True
    }
    with open("fleet.json", "w") as f:
        json.dump({
            "settings": game_settings,
            "fleet_name": "",
            "spaceships": []
        }, f, indent=4)
    print("Datas has been deleted, please restart the game.\n")

def random_event(fleet_manager):
    if not fleet_manager._spaceships:
        return
    num1 = random.randint(1, 7)
    num2 = random.randint(1, 7)

    if num1 == num2:
        spaceship = random.choice(fleet_manager._spaceships)

        current_condition = spaceship._condition
        available_condition = ["damaged", "destroyed", "operational"]
        
        if current_condition == "damaged":
            new_condition = "destroyed"
        elif current_condition == "operational":
            new_condition = "damaged"
        else:
            return
        spaceship._condition = new_condition
        print(f"Event: The spaceship '{spaceship._name}' is now {new_condition}.")

def load_data(fleet_manager):
    try:
        with open("fleet.json", "r") as f:
            fleet_data = json.load(f)
            fleet_manager._name = fleet_data["fleet_name"]

            for spaceship_data in fleet_data["spaceships"]:
                fleet_manager.append_spaceship_api(spaceship_data)

                for member_data in spaceship_data["crew"]:
                    spaceship = fleet_manager.get_spaceship_by_name(spaceship_data["name"])
                    spaceship._crew.add_member_api(member_data)

            print("\nData loaded successfully.")
    except FileNotFoundError:
        print("No fleet data found. Starting with an empty fleet.")

def save_data(fleet_manager):
    global game_settings
    try:
        fleet_data = {
            "settings": [],
            "fleet_name": fleet_manager._name,
            "spaceships": []
        }
        for spaceship in fleet_manager._spaceships:
            spaceship_data = {
                "name": spaceship._name,
                "type": spaceship._type,
                "condition": spaceship._condition,
                "crew": []
            }
            for member in spaceship._crew.crew_list:
                if member.role == "mentalist":
                    member_data = {
                        "first_name": member.first_name,
                        "last_name": member.last_name,
                        "gender": member.gender,
                        "age": member.age,
                        "role": member.role,
                        "mana": member.mana
                    }
                else:
                    member_data = {
                        "first_name": member.first_name,
                        "last_name": member.last_name,
                        "gender": member.gender,
                        "age": member.age,
                        "role": member.role,
                        "experience": member.experience
                    }
                spaceship_data["crew"].append(member_data)
            
            fleet_data["spaceships"].append(spaceship_data)
        settings_data = {}
        for data in game_settings:
            settings_data[data] = game_settings[data]

        fleet_data["settings"] = settings_data
        
        with open("fleet.json", "w") as f:
            json.dump(fleet_data, f, indent=4)
        print("\nData saved successfully.\n")
        return
    except Exception as e:
        print("An error occurred while saving the data:")
        print(e)
        
def cleanup():
    global game_settings
    if game_settings["auto_save_on_exit"]:
        save_data(fleet_manager)

def manage_member_menu(member):
    while True:
        if member.role == "mentalist":
            print(
                f"\nManaging member: {member.first_name} {member.last_name} {member.age} years old, {member.role}\n"
                " [1 - ls] Introduce himself\n [2] Act\n [3] Recharge mana\n[0 - back] Back to main menu\n"
            )
            user_choice = input("Enter your choice: ").strip()

            if user_choice == "1" or user_choice == "ls":
                member.introduce_yourself()
            elif user_choice == "2":
                member.act()
            elif user_choice == "3":
                member.recharge_mana()
            elif user_choice == "0" or user_choice == "backt" or user_choice == "":
                break
            else:
                print("Please choose a valid option (0-3).")
        if len(member.role) >= 1:
            print(
                f"\nManaging member: {member.first_name} {member.last_name} {member.age} years old, {member.role}\n"
                " [1 - ls] Introduce himself\n [2] Act\n [3] Gain experience\n [4] Change role\n [5] Change experience\n[0 - back] Back to main menu\n"
            )
            user_choice = input("Enter your choice: ").strip()

            if user_choice == "1" or user_choice == "ls":
                member.introduce_yourself()
            elif user_choice == "2":
                member.act()
            elif user_choice == "3":
                member.gain_experience()
            elif user_choice == "4":
                print("Types of operator:\n [1] Pilot\n [2] Technician\n [3] Scientist\n [4] Engineer\n [5] Doctor\n [6] Security\n [7] Cook")
                operator_role = input("Enter the role of the crew member: ").strip().lower()
                if operator_role == "1":
                    role = "pilot"
                elif operator_role == "2":
                    role = "technician"
                elif operator_role == "3":
                    role = "scientist"
                elif operator_role == "4":
                    role = "engineer"
                elif operator_role == "5":
                    role = "doctor"
                elif operator_role == "6":
                    role = "security"
                elif operator_role == "7":
                    role = "cook"
                else:
                    print("Invalid option, please try again")
                Operator.role = role
            elif user_choice == "5":
                experience = input("Enter the experience of the crew member (default 0): ")
                try:
                    experience = int(experience)
                except ValueError:
                    experience = 0
                    print("Invalid, experience set to default (0)")
                Operator.experience = experience
            elif user_choice == "0" or user_choice == "back" or user_choice == "":
                break
            else:
                print("Please choose a valid option (0-3).")

def navigate_members(spaceship):
    if not spaceship._crew.crew_list:
        print("No members in the crew yet.")
        return

    while True:
        print("\nAvailable members:")
        for idx, member in enumerate(spaceship._crew.crew_list, 1):
            if member.role == "mentalist":
                print(f" [{idx}] {member.first_name} ({member.last_name}, {member.gender}, {member.age}, {member.role}, {member.mana})")
            else:
                print(f" [{idx}] {member.first_name} ({member.last_name}, {member.gender}, {member.age}, {member.role}, {member.experience})")
        print("[0] Back to main menu")

        choice = input("Choose a member to manage (or 0 to return): ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            elif 1 <= choice <= len(spaceship._crew.crew_list):
                manage_member_menu(spaceship._crew.crew_list[choice - 1])
            else:
                print("Invalid choice.")
        else:
            print("Invalid input. Please enter a number.")

def manage_spaceship_menu(spaceship):
    while True:
        print(
            f"\nManaging spaceship: {spaceship._name}\n"
            " [1 - ls] Display crew\n [2] Add crew member\n [3] Remove crew member\n [4] Change condition\n [5] Display name\n [6] Check preparation\n [7] Manage members\n[0 - back] Back to main menu\n"
        )
        user_choice = input("Enter your choice: ").strip()

        if user_choice == "1" or user_choice == "ls":
            spaceship._crew.display_crew()
        elif user_choice == "2":
            spaceship._crew.add_member()
        elif user_choice == "3":
            spaceship._crew.remove_crew_member()
        elif user_choice == "4":
            print("Condition\n[1] Damaged\n[2] Operational\n[3] Destroyed\n")
            new_condition = input("Enter new condition: ").strip().lower()
            if new_condition == "1":
                new_condition = "damaged"
            elif new_condition == "2":
                new_condition = "operational"
            elif new_condition == "3":
                new_condition = "destroyed"
            else:
                print("Invalid condition.")
                break
            spaceship._condition == (new_condition)
            print(f"Condition updated to {new_condition}.")
        elif user_choice == "5":
            print(f"Spaceship name: {spaceship._name}")
        elif user_choice == "6":
            spaceship.check_preparation()
        elif user_choice == "7":
            navigate_members(spaceship)
        elif user_choice == "0" or user_choice == "back" or user_choice == "":
            return
        else:
            print("Please choose a valid option (0-7).")

def navigate_spaceships():
    if not fleet_manager._spaceships:
        print("No spaceships in the fleet yet.")
        return

    while True:
        print("\nAvailable spaceships:")
        for idx, ship in enumerate(fleet_manager._spaceships, 1):
            print(f" [{idx}] {ship._name} ({ship._type}, {ship._condition})")
        print("[0] Back to main menu")

        choice = input("Choose a spaceship to manage (or 0 to return): ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            elif 1 <= choice <= len(fleet_manager._spaceships):
                manage_spaceship_menu(fleet_manager._spaceships[choice - 1])
            else:
                print("Invalid choice.")
        else:
            print("Invalid input. Please enter a number.")

def settings_menu():
    global game_settings

    while True:
        print("\n====Settings====\n Actual settings:")
        print(f"Auto save on exit: {game_settings["auto_save_on_exit"]}")
        print(f"Auto load: {game_settings["auto_load"]}")
        if game_settings['auto_save_on_exit']:
            print(" [1] Disable auto save on exit ❌")
        else:
            print(" [1] Enable auto save on exit ✅")
        
        if game_settings['auto_load']:
            print(" [2] Disable auto loading ❌")
        else:
            print(" [2] Enable auto loading ✅")
        print(" [3 - reset] Reset game")
        print("[0] Back to main menu")

        user_choice = input("Enter your choice: ").strip()

        if user_choice == "1":
            if game_settings['auto_save_on_exit']:
                game_settings['auto_save_on_exit'] = False
                print("\nAuto save on exit now disabled ❌")
            else:
                game_settings['auto_save_on_exit'] = True
                print("\nAuto save on exit now enable ✅")
        elif user_choice == "2":
            if game_settings['auto_load']:
                game_settings['auto_load'] = False
                print("\nAuto load now disabled ❌")
            else:
                game_settings['auto_load'] = True
                print("\nAuto load now enabled ✅")
        elif user_choice == "3" or user_choice == "reset":
            if input("\n\nAre you sure ? (y/n): ").strip().lower() == "y":
                 reset_data()
                 return "reset"
            else:
                print("Operation canceled")
        elif user_choice == "0" or user_choice == "back" or user_choice == "":
            break
        else:
            print("Please choose a valid option (0-3).")

def main_menu():
    global game_settings
    while True:
        print(
            "\n Main Menu:\n [1] Add a spaceship to the fleet\n [2 - ls] Show all spaceships in the fleet\n [3] Display fleet statistics\n [4] Display name\n [5] Rename the fleet\n [6] Manage spaceships\n[7 - settings] Settings 🛠️\n[8 - save] Save your fleet 💾\n[0 - exit] Exit ❌\n"
        )
        r_event = random.randint(1, 10)
        if r_event // 2 == 0:
            random_event(fleet_manager)
        
        user_choice = input("Enter your choice: ").strip()

        if user_choice == "1":
            fleet_manager.append_spaceship(Spaceship)
        elif user_choice == "2" or user_choice == "ls":
            fleet_manager.display_fleet()
        elif user_choice == "3":
            fleet_manager.fleet_statistics()
        elif user_choice == "4":
            print(f"Fleet named: {fleet_manager._name}")
        elif user_choice == "5":
            input_name = input("Enter the new name of the fleet: ").strip()
            fleet_manager._name = input_name
        elif user_choice == "6":
            navigate_spaceships()
        elif user_choice == "7" or user_choice == "settings":
            if settings_menu() == "reset":
                break
        elif user_choice == "8" or user_choice == "save":
            save_data(fleet_manager)
        elif user_choice == "0" or user_choice == "exit" or user_choice == "":
            if game_settings["auto_save_on_exit"]:
                save_data(fleet_manager)
            print(f"Goodbye from fleet '{fleet_manager._name}'!\n")
            break
        else:
            print("Please choose a valid option (0-7).")
            
def start_menu():
    global fleet_manager
    print("\n====================================\n")
    print("🚀 Welcome to the Spaceship Fleet Manager! 🚀")
    print("\n====================================\n")
    fleet_name = input("Enter the name of your fleet: ").strip()
    fleet_manager = Fleet(fleet_name)


if __name__ == "__main__":
    atexit.register(cleanup)
    initialize_json_file()
    get_settings()
    
    print("\nSettings informations:")
    if game_settings['auto_load'] == True:
        print("Auto load is enabled")
    else:
        print("Auto load is disabled")
    
    if game_settings['auto_save_on_exit'] == True:
        print("Auto save on exit is enabled")
    else:
        print("Auto save on exit is disabled")
    
    if game_settings['auto_load'] == True:
        try:
            with open("fleet.json", "r") as f:
                fleet_data = json.load(f)
                if fleet_data["fleet_name"] == "":
                    start_menu()
                else:
                    fleet_manager = Fleet(fleet_data["fleet_name"])
                    load_data(fleet_manager)
        except FileNotFoundError:
            print("Fleet data file not found. Starting with an empty fleet.")
            start_menu()
    else:
        print("Auto load is disabled, then:")
        if input("\n\nLoad last save ? (y/n): ").strip().lower() == "y":
            fleet_manager = Fleet("")
            load_data(fleet_manager)
        else:
            start_menu()
    
    main_menu()
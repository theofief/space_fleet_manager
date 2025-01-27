from spaceship import Spaceship

class Fleet:
    def __init__(self, name):
        self.__name = name
        self.__spaceships = []

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _spaceships(self):
        return self.__spaceships

    @_spaceships.setter
    def _spaceships(self, value):
        self.__spaceships = value

    def set_spaceships(self, value):
        self.__spaceships = value

    def append_spaceship(self, spaceship):
        if len(self.__spaceships) < 15:
            name = input("Enter name: ")
            if not name or name in [spaceship._name for spaceship in self._spaceships]:
                print("Already used or empty")
                return

            print("Ship type\n[1] Transporter\n[2] Fighter\n[3] Merchandiser\n")
            ship_type = input("Enter ship type: ")
            if ship_type == "1":
                ship_type = "transporter"
            elif ship_type == "2":
                ship_type = "fighter"
            elif ship_type == "3":
                ship_type = "merchandiser"
            else:
                print("Invalid choice")
                return

            print("Condition\n[1] Damaged\n[2] Operational\n[3] Destroyed\n")
            condition = input("Enter condition: ")
            if condition == "1":
                condition = "damaged"
            elif condition == "2":
                condition = "operational"
            elif condition == "3":
                condition = "destroyed"
            else:
                print("Invalid condition, defaulting to 'destroyed'.")
                condition = "destroyed"

            new_spaceship = Spaceship(name, ship_type, condition)
            self.__spaceships.append(new_spaceship)

            print(f"{name} has been successfully added to the fleet as a {ship_type} in {condition} condition.")
        else:
            print("The fleet is full. Cannot add any more spaceships.")

    def append_spaceship_api(self, spaceship_data):
        """Ajoute un vaisseau en utilisant des données issues de l'API ou d'un fichier JSON"""
        if len(self.__spaceships) < 15:
            name = spaceship_data.get("name", "").strip()

            if not name or any(s._name == name for s in self._spaceships):
                print("Name already used or is empty.")
                return

            ship_type = spaceship_data.get("type", "").strip()
            ship_types = {
                "transporter": "transporter",
                "fighter": "fighter",
                "merchandiser": "merchandiser"
            }

            if ship_type not in ship_types:
                print("Invalid ship type.")
                return

            condition = spaceship_data.get("condition", "").strip()
            conditions = {
                "damaged": "damaged",
                "operational": "operational",
                "destroyed": "destroyed"
            }

            if condition not in conditions:
                print("Invalid condition, defaulting to 'destroyed'.")
                condition = "destroyed"

            new_spaceship = Spaceship(name, ship_type, condition)

            self.__spaceships.append(new_spaceship)
        else:
            print("The fleet is full. Cannot add any more spaceships.")

    def get_spaceship_by_name(self, name):
        """Retourne un vaisseau par son nom."""
        for spaceship in self.__spaceships:
            if spaceship._name == name:
                return spaceship
        print(f"Spaceship with name {name} not found.")
        return None

    def display_fleet(self):
        if not self.__spaceships:
            print("No spaceships in the fleet.\n")
        else:
            print(f"Spaceships in fleet '{self.__name}':\n")
            for idx, spaceship in enumerate(self.__spaceships, start=1):
                print(f"[{idx}] Name: {spaceship._name}, Type: {spaceship._type}, Condition: {spaceship._condition}")
            print("\n")

    def fleet_statistics(self):
        if not self.__spaceships:
            print("No spaceships in the fleet to display statistics.\n")
            return

        total_members = 0
        roles = {}
        total_experience = 0

        for spaceship in self.__spaceships:
            total_members += len(spaceship._crew._crew_list)
            for member in spaceship._crew._crew_list:
                roles[member._role] = roles.get(member._role, 0) + 1
                if member._role == "operator":
                    total_experience += member._experience

        if total_members > 0:
            median_level = total_experience / total_members
        else:
            median_level = 0

        print(f"Fleet statistics:")
        print(f"Total members: {total_members}")
        print(f"Median experience level: {median_level:.2f}")
        print("Roles distribution:")
        for role, count in roles.items():
            print(f"  {role}: {count} members")

        print(f"Fleet '{self.__name}' Statistics:\n")
        print(f"Total crew members: {total_members}")
        print(f"Roles distribution: {roles}")
        print(f"Median experience level: {median_level:.2f}")

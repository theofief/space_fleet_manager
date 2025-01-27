from member import Member
from Operator import Operator
from mentalist import Mentalist

class Crew:
    """Manage your own crew"""

    def __init__(self):
        self.__crew_list = []
        self.__roles = ["pilot", "technician", "scientist", "engineer", "doctor", "security", "cook"]

    @property
    def crew_list(self):
        return self.__crew_list

    @crew_list.setter
    def crew_list(self, value):
        self.__crew_list = value

    def verify_crew(self):
        """Vérifie si l'équipe est prête"""
        job_counts = {role: 0 for role in ["pilot", "technician"]}
        for member in self.__crew_list:
            job_counts[member.role] = job_counts.get(member.role, 0) + 1

        if job_counts["pilot"] < 1 or job_counts["technician"] < 1:
            print("At least one pilot and one technician are required.")
            return False
        return True

    def verify_last_name(self, last_name):
        """Vérifie la validité et l'unicité du nom de famille"""
        if not last_name:
            print("Last name is required.")
            return False
        if any(member.last_name == last_name for member in self.__crew_list):
            print("Last name already exists.")
            return False
        if not (3 <= len(last_name) <= 15):
            print("Last name must be between 3 and 15 characters.")
            return False
        return True

    def verify_age(self, age):
        """Vérifie si l'âge est valide"""
        try:
            age = int(age)
        except ValueError:
            print("Invalid age")
            return False
        if not (18 <= age <= 65):
            print("Age must be between 18 and 65.")
            return False
        return True

    def add_member(self):
        """Ajoute un nouveau membre d'équipage"""
        first_name = input("Enter the first name of the crew member: ").strip()
        last_name = input("Enter the last name of the crew member: ").strip()
        gender = input("Enter the gender of the crew member: ").strip().lower()
        age = input("Enter the age of the crew member: ")
        if not self.verify_age(age):
            return
        print(
            f"\nChoose a role:\n"
            " [1] Operator\n [2] Mentalist\n"
        )
        input_role = input("Enter the role of the crew member: ").strip().lower()
        if input_role == "1":
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
                print("Invalid role")
                return
            experience = input("Enter the experience of the crew member (default 0): ")
            try:
                experience = int(experience)
            except ValueError:
                experience = 0
                print("Invalid, experience set to default (0)")
            new_member = Operator(first_name, last_name, gender, age, role, experience)
        elif input_role == "2":
            role = "mentalist"
            experience = int(input("Enter the experience of the crew member (default 0): "))
            if len(experience) == 0:
                experience = 0
            new_member = Mentalist(first_name, last_name, gender, age, role, experience)
        else:
            print("Invalid role")
            return
        if not self.verify_last_name(last_name):
            return
        if not self.verify_age(age):
            return
        self.__crew_list.append(new_member)
        print(f"Added new member: {first_name} {last_name} ({role})")

    def add_member_api(self, member_data):
        """Ajoute un membre d'équipage à partir d'un objet 'member_data'"""
        if member_data["role"] == "mentalist":
            new_member = Mentalist(
                member_data["first_name"],
                member_data["last_name"],
                member_data["gender"],
                member_data["age"],
                member_data["role"],
                member_data["mana"]
            )
            self.__crew_list.append(new_member)
        else:
            new_member = Operator(
                member_data["first_name"],
                member_data["last_name"],
                member_data["gender"],
                member_data["age"],
                member_data["role"],
                member_data["experience"]
            )
            self.__crew_list.append(new_member)

    def display_crew(self):
        """Affiche les membres de l'équipage"""
        if not self.__crew_list:
            print("The crew is currently empty.")
            return

        print("Current crew members:")
        for member in self.__crew_list:
            if member.role == "mentalist":
                print(
                    f"{member.first_name} {member.last_name} - {member.role} "
                    f"({member.age} years old, {member.mana} mana)"
                )
            else:
                print(
                    f"{member.first_name} {member.last_name} - {member.role} "
                    f"({member.age} years old, {member.experience} XP)"
                )

    def remove_crew_member(self):
        """Supprime un membre d'équipage"""
        last_name = input("Enter the last name of the crew member to remove: ").strip()
        for member in self.__crew_list:
            if member.last_name == last_name:
                self.__crew_list.remove(member)
                print(f"Removed crew member: {member.first_name} {member.last_name}")
                return
        print("Crew member not found.")

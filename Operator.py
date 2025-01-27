import random
from member import Member

class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = experience

        self.tasks = [
            "piloting the spacecraft",
            "maintaining the spacecraft's systems",
            "repairing mechanical components",
            "performing medical check-ups",
            "conducting scientific experiments",
            "managing communications with mission control",
            "overseeing navigation and flight paths",
            "monitoring life support systems",
            "ensuring safety protocols are followed",
            "providing technical support for crew members",
            "managing cargo and supplies",
            "assisting with spacewalks",
            "maintaining and updating crew records",
            "planning and executing mission strategies",
            "preparing meals and managing food supplies",
            "training new crew members",
            "performing emergency procedures",
            "analyzing data collected during the mission",
            "designing and implementing mission hardware",
            "performing routine health check-ups for the crew",
        ]

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        self.__experience = value

    def act(self):
        task = random.choice(self.tasks)
        print(f"{self.role} {self.first_name} {self.last_name} is {task}")

    def gain_experience(self):
        self.experience += 1
        print(f"{self.role} {self.first_name} {self.last_name} gained 1 year of experience")

import random
from member import Member

class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age, role, mana=100):
        super().__init__(first_name, last_name, gender, age)

        self.__role = role
        self.__mana = mana

        self.tasks = [
            "casting elemental spells (fire, water, earth, air)",
            "healing injured allies",
            "summoning creatures for assistance",
            "protecting allies with defensive magic",
            "enchanting weapons and items",
            "teleporting to distant locations",
            "controlling weather conditions",
            "manipulating time for short periods",
            "detecting magical auras and hidden objects",
            "creating illusions to deceive enemies",
            "creating magical barriers to block attacks",
            "performing divination to foresee future events",
            "crafting magical potions and elixirs",
            "studying ancient magical texts",
            "teaching and training apprentices in magic",
            "performing ritual magic for specific purposes",
            "transmuting objects into other materials",
            "banishing dark forces and evil spirits",
            "channeling energy from mystical sources",
            "controlling minds or influencing emotions",
            "summoning familiars for guidance and aid",
        ]
        
    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, value):
        self.__mana = value

    def act(self):
        if self.__mana >= 20:
            task = random.choice(self.tasks)
            self.__mana -= 20
            print(f"{self.__role} {self.first_name} {self.last_name} is {task}. Mana remaining: {self.__mana}")
        else:
            print(f"{self.first_name} {self.last_name} is out of mana and needs to recharge.")

    def recharge_mana(self):
        if self.__mana < 50:
            self.__mana += 50
            print(f"{self.first_name} {self.last_name} recharged 50 mana. Current mana: {self.__mana}")
        else:
            self.__mana = 100
            print(f"{self.first_name} {self.last_name} recharged to full mana.")

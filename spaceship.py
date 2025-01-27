from crew import *

class Spaceship:
    def __init__(self, name, ship_type, condition):
        self.__name = name
        self.__type = ship_type
        self.__crew = Crew()
        self.__condition = condition

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _type(self):
        return self.__type

    @_type.setter
    def _type(self, value):
        self.__type = value

    @property
    def _crew(self):
        return self.__crew

    @_crew.setter
    def _crew(self, value):
        self.__crew = value

    @property
    def _condition(self):
        return self.__condition

    @_condition.setter
    def _condition(self, value):
        self.__condition = value

    def append_member(self, member, first_name, last_name, gender, age):
        if len(self.__crew.crew_list) < 10:
            self.__crew.add_member()
        else:
            print("The crew is full")

    def check_preparation(self):
        for member in self.__crew.crew_list:
            if member.role == "mentalist" and member.mana < 50:
                print("The crew is not ready")
                return
        if not self.__crew.verify_crew():
            print("The crew is not ready")
            return
        print("The crew is ready")
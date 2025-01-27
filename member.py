class Member:
    def __init__(self, first_name, last_name, gender, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def introduce_yourself(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}. I am {self.age} years old.")

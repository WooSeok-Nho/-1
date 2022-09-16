class Profile():
    def __init__(self):
        self.name = "Nho"
        self.gender = "man"
        self.birthday = "0223"
        self.age = "27"
        self.phone = "76874569"
        self.email = "nhowooseok@gmail.com"

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.name = gender

    def set_birthday(self, birthday):
        self.name = birthday

    def set_age(self, age):
        self.name = age

    def set_phone(self, phone):
        self.name = phone

    def set_email(self, email):
        self.name = email

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_birthday(self):
        return self.birthday

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email


profile1 = Profile()
print(profile1.get_name())
print(profile1.get_gender())
print(profile1.get_birthday())
print(profile1.get_age())
print(profile1.get_phone())
print(profile1.get_email())


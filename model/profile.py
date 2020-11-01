class Profile:
    def __init__(self, mobile=None, password=None, email="", name="Александр", surname="Строков", secondname="Сергеевич"):
        self.mobile = mobile
        self.password = password
        self.email = email
        self.name = name
        self.surname = surname
        self.secondname = secondname
        self.surnameNS = self.surname + ' ' + self.name[0] + ' ' + self.secondname[0]

    def __repr__(self): #Как будет выглядеть объект при выводе на консоль
        return  "%s:%s" % (self.mobile, self.password)

    def __eq__(self, other): #Как будут сравниваться объекты
        return self.mobile == other.modile and self.password == other.password
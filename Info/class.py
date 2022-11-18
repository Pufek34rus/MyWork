class House():
    """описание дома"""

    def __init__(self, street, number, material):
        # __init__Обязательный метод для инициализации. Блягодаря ему,
        #  все объекты ссылающиеся на этот класс, будут использовать
        # все свойства этого класса.

        """Свойство дома"""

        # Свойство класса. Применяет номер улицы указанный пользователем.
        self.street = street
        self.number = number
        self.material = material
        # Свойство не указанно в методе, значит его нельзя изменять
        # и оно будет по умолчанию для всех объектов класса.
        self.age = 2017

        # Метод при обращении к которму выведет сообщение
        # на основе данных в головном методе init
    def build(self):
        """строительство"""
        print("Дом на улице " + self.street +
              " под номером " + str(self.number) + " материал " +
              self.material + " = построен.")
        # Метод при обращении к которму сложит число указанное
        # для его значения "years" с значением в свойстве по умолчанию
        """Возраст дома"""
    def age_of_house(self, years):
        self.age += years


# Создали объект класса и присвоили ему значения
House1 = House("Розы-Люксембург", 1, "кирпич")
House2 = House("64 Армии", 24, 'кирпич')

print("~~~~~~~Часть 1~~~~~~~")
# Обращение к свойствам объекта
print(House1.street)
print(House2.number)
print("~~~~~~~Часть 2~~~~~~~")
# Обращение к заранее созданному методу
House1.build()
print("~~~~~~~Часть 3~~~~~~~")
# Вызов свойства по умолчанию
print(House1.age)
# использование метода "Возраст дома"
House1.age_of_house(5)
print(House1.age)
print("~~~~~~~Часть 4~~~~~~~")
# Дочерний класс от class.House


class ProspectHouse(House):
    """Дома на проспекте"""
    def __init__(self, Prospect, number, material):
        # функция super() позваляет связать аттрибуты с родительским классом
        super().__init__(self, number, material)
        self.Prospect = Prospect
prHouse = ProspectHouse("Ленина", 7, "Панели")
print(prHouse.Prospect + str(prHouse.number))

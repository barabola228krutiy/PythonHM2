class Danya:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        course = age - 16 if age >= 17 else None
        return f"{course} курс" if course and 1 <= course <= 6 else None

    def get_name_list(self):
        return [self.name, self.surname]


# Дочірній клас
class Student(Danya):
    def __init__(self, name=None, surname=None, birth_year=None,
                 university=None, major=None, gpa=None):
        super().__init__(name, surname, birth_year)
        self.university = university
        self.major = major
        self.__gpa = gpa  # Приватний атрибут

    def get_full_profile(self):
        return {
            "ПІБ": f"{self.name} {self.surname}",
            "ВНЗ": self.university,
            "Спеціальність": self.major,
            "Курс": self.calculate_course(),
            "GPA": self.__gpa
        }

    def _is_eligible_for_scholarship(self):  # Protected метод
        """Метод перевіряє, чи студент має право на стипендію"""
        return self.__gpa is not None and self.__gpa >= 4.5


# Приклад використання
student = Student("Даниїл", "Вознюк", 2007, "КПІ", "Інформатика", 4.8)
print(student.get_full_profile())  # Профіль студента
print(student._is_eligible_for_scholarship())  # True (має право на стипендію)

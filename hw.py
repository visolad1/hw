class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def print_inf(self):
        return f'''
        Имя - {self.name}
        Пол - {self.sex}
        Возраст - {self.age}
        '''


class Book:
    def __init__(self, title, author, language, genre):
        self.title = title
        self.author = author
        self.language = language
        self.genre = genre

    def print_inf(self):
        return f'''
        Название - {self.title}
        Автор - {self.author}
        Язык - {self.language}
        Жанр - {self.genre}
        '''


class Laptop:
    def __init__(self, brand, series, screen, cpu, color):
        self.brand = brand
        self.series = series
        self.screen = screen
        self.cpu = cpu
        self.color = color

    def print_inf(self):
        return f'''
        Brand - {self.brand}
        Series - {self.series}
        Screen - {self.screen}
        CPU - {self.cpu}
        Color - {self.color}
        '''


class Sneakers:
    def __init__(self, brand, sex, material, color):
        self.brand = brand
        self.sex = sex
        self.material = material
        self.color = color

    def print_inf(self):
        return f'''
        Brand - {self.brand}
        Sex - {self.sex}
        Material - {self.material}
        Color - {self.color}
        '''


class Text:
    def __init__(self, text):
        self.text = text

    def flip_text(self):
        self.text = self.text[::-1] 
        return self.text


class Num:
    def __init__(self, num):
        self.num = num
    
    def fibonacci(self):
        l = '1 1'
        f1, f2 = 1, 1
        n = int(self.num)
 
        for i in range(2, n):
            f1, f2 = f2, f1 + f2
            l = l + ' ' + str(f2)
        
        return l
    
    def primes(self):
        n = int(self.num)
        l = []
        k = 0
        for i in range(2, n+1):
            for j in range(2, i):
                if i % j == 0:
                    k = k + 1
            if k == 0:
                l.append(i)
            else:
                k = 0
        return l


class Person:
    def __init__(self, name, surname, sex, age):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age

    def print_inf(self):
        return f'''
        Имя - {self.name}
        Фамилия - {self.surname}
        Пол - {self.sex}
        Возраст - {self.age}
        '''


class Phone:
    def __init__(self, brand, os_version, screen_type, color):
        self.brand = brand
        self.os_version = os_version
        self.screen_type = screen_type
        self.color = color

    def print_inf(self):
        return f'''
        Бренд - {self.brand}
        Версия ОС - {self.os_version}
        Тип экрана - {self.screen_type}
        Цвет - {self.color}
        '''


class User:
    def __init__(self, name, surname, username, password):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password

    def login(self):
        return f'''
        Name - {self.name}
        Surname - {self.surname}
        Username - {self.username}
        Password - {self.password}
        '''


class Movie:
    def __init__(self, name, director, writers, stars):
        self.name = name
        self.director = director
        self.writers = writers
        self.stars = stars

    def print_inf(self):
        return f'''
        Name - {self.name}
        Director - {self.director}
        Writers - {self.writers}
        Stars - {self.stars}
        '''
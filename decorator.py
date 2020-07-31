"""
Created on Wed Jul 31 22:17:11 2020
@author: industrius
@institution: SkillFactory
"""

print("\nФункция-декоратор с параметром количества запусков и выводом среднего усредненного времени выполнения испытываемой функции.")

# Функция-декоратор
def time_this_func(num=10): #прием параметров декоратора - количество запусков
    """
    функция - секундомер 
    Принимает функцию и количество тестовых запусков.
    Показывает среднее время на один запуск тестируемой функции 
    и время на запуск указанное количество раз.
    """
    def decorator(fn): #функция декоратор, принимающая испытываемую/исполняемую функцию
        import time
        def wrapper(): #функция оборачивающая испытываемую/исполняемую функцию
            avg_time = 0
            for _ in range(num):
                start = time.time()
                fn()  #испытываемая функция
                end = time.time()
                avg_time += (end - start)
            print("Среднее время выполнения: %.6f" % (avg_time / num))
            print("Общее время на %.0f запусков: %.6f\n" % (num ,avg_time))
        return wrapper #функция декоратор возвращает оборачивающую функцию
    return decorator #внешняя функция возвращает декоратор

@time_this_func(15) # функция декоратор, количество запусков 15
def fibo():
    """
    Тестируемая функция
    """
    digit = 0
    digit_current = 1
    digit_prew = 0
    while digit < 6000000000000:
        digit = digit_prew + digit_current
        digit_prew = digit_current
        digit_current = digit

# Вызов декорируемой функции
fibo()



# Декоратор в качестве объекта класса-секундомера
class timeThis:
    """
    Класс - секундомер 
    Принимает функцию и количество тестовых запусков.
    Показывает среднее время на один запуск тестируемой функции 
    и время на запуск указанное количество раз.
    """
    num = 10 # количество запусков тестируемой функции
    def __init__(self, func):
        self.func = func # тестируемая функция

    def __call__(self):
        import time
        avg_time = 0
        for _ in range(self.num):
            start = time.time()
            self.func() # запуск функции
            finish = time.time()
            avg_time += finish - start
        print("Среднее время выполнения функции: %.6f" % (avg_time / self.num))
        print("Общее время на %.0f запусков: %.6f\n" % (self.num, avg_time))
    
    def __enter__(self): # методы, необходимые для работы с контекстным менеджером
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback): # методы, необходимые для работы с контекстным менеджером
        pass


print("\nЗадание с одной звездочкой: написать декоратор в качестве объекта класса-секундомера.")

@timeThis
def fibo2():
    """
    Тестируемая функция
    """
    digit = 0
    digit_current = 1
    digit_prew = 0
    while digit < 6000000000000000:
        digit = digit_prew + digit_current
        digit_prew = digit_current
        digit_current = digit

# задаем количество запусков тестируемой функции
timeThis.num = 5
# запускаем тестируемой функции с классом-декоратором
fibo2()


print("\nЗадание с двумя звездочками: написать декоратор в качестве объекта класса-секундомера, который можно использовать как контекстный менеджер.")

def fibo3():
    """
    Тестируемая функция
    """
    digit = 0
    digit_current = 1
    digit_prew = 0
    while digit < 6000000000000000:
        digit = digit_prew + digit_current
        digit_prew = digit_current
        digit_current = digit

# Вызов класса, как контекстного менеджера с указанием тестируемой функции 
# Передаем в класс тестируемую функцию
with timeThis(fibo3) as timer:
    # задаем количество запусков тестируемой функции
    timeThis.num = 25
    # вызываем класс-декоратор для подсчета времени выполения тестируемой функции
    timer()
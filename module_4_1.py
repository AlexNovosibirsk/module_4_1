"""
Задача "А как делить?":
"""

import fake_math as fm  # установить псевдоним
from fake_math import *  # импортировать всё из fake_math в глобальное пространство данного модуля
from fake_math import divide as fake_divide
from true_math import divide as true_divide

print(dir(fm)) # посмотрим список атрибутов модуля fake_math подключенного как fm
fm.divide(1, 4)  # вызвали из fake_math
divide(1, 4)  # вызвали из fake_math напрямую (from fake_math import *)

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
"""
23.0
Ошибка
7.0
inf
"""


print(fm.__name__) # псевдоним принадлежит модулю fake_math
print(__name__) # этот модуль __main__



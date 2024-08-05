"""
Задача "А как делить?":
"""

import fake_math as fm  # установить псевдоним
from fake_math import *  # импортировать всё из fake_math
from fake_math import divide as fake_divide
from true_math import divide as true_divide

#print(dir(fm))
fm.divide(1, 4)  # вызвали из fake_math
divide(1, 4)  # вызвали из fake_math напрямую

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


#print(fm.__name__) # fake_math
#print(__name__) # __main__



import pytest
from functions import fibonachi, bubble_sort, calculator

def test_fibonachi():
    assert fibonachi(0) == [0]  #проверка для 0 чисел
    assert fibonachi(1) == [0, 1]   #проверка для 1 числа
    assert fibonachi(4) == [0, 1, 1, 2] #проверка для 4 чисел

def test_bubble_sort():
    assert bubble_sort([]) == []    #проверка для пустого списка
    assert bubble_sort([4, 2, 3, 1]) == [1, 2, 3, 4]    #проверка для обычного списка
    assert bubble_sort([3, -2, 0, 1]) == [-2, 0, 1, 3]  #проверка сортировки списка с отрицательными числами

def test_calculator():
    assert calculator(2, 3, "+") == 5   #проверка суммы
    assert calculator(3, 2, "-") == 1   #проверка разности
    assert calculator(2, 3, "*") == 6   #проверка умножения
    assert calculator(4, 2, "/") == 2   #проверка деления
    with pytest.raises(ZeroDivisionError):
        calculator(3, 0, "/")   #проверка деления на ноль


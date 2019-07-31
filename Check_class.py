# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=W0105
"""
Декоратор для проверки типов входящих переменных
"""


def Check_class(iters=0, Reg=0):
    """
    from Check_class import Check_class
    @Check_class({}) 
    Reg - Отображать имена входящие в декоратор
    """
    def actual_decorator(func):
        def decorator_function(*Items, **Dicts):
            if Reg:
                """
                Информация Reg = 1
                """
                for x in range(len(list(func.__name__))+7): #pylint: disable=W0612
                    print('_', end='')

                print(f'\nFunc - {func.__name__}')
                print(f'Variables - {Dicts}')
                a = [type(x) for x in Dicts.values()]
                print('Class - {}'.format(a))

                for x in range(len(str(a))+8):
                    print('_', end='')
                print('\n', end='')

            if not iters:
                return func(*Items, **Dicts)

            if not Dicts:
                return func(*Items, **Dicts)

            for name_variable in Dicts:
                if name_variable in iters:
                    if not isinstance(Dicts[name_variable], iters[name_variable]):
                        raise Exception(False, {'Error Type': (
                            name_variable, Dicts[name_variable], iters[name_variable])})

            return func(*Items, **Dicts)

        return decorator_function
    return actual_decorator


"""
# print(iters) # Значения переданные в Декоратор !
# print(func) # Основная функций после декоратора
# print(Items) # Значения переданные в Функцию ! => tuple
# print(Dicts) # Значения переданные в Функцию ! => dict
# print(*Dicts) # Значения переданные в Функцию ! => dict

Декоратор для проверки типов входящих переменных

- Состояния покоя : ничего не делает
@Check_class({}) 


- Работа : указать словарем неограниченное количество элементов 
и правильных для них классов

{'название переменной в вызываемой функции' : правильный класс}

@Check_class({'arr_str':int})

def Fanc(arr_str, int_s):
    return "ВЫПОЛЕННО"

print(Fanc(arr_str='123',int_s='s1'))

# (False, {'Error Type': ('arr_str', '123', <class 'int'>)})


Проверяет:
- Тип переменной с заданной в декораторе 
- Имя пременной преданное в декаратор на налиеие этого имяни в 
функции 

"""

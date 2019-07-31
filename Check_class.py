# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=W0105
"""
Декоратор для проверки типов входящих переменных
"""
import time


def Check_class(Reg=0):
    """
    from Check_class import Check_class
    @Check_class(1) 
    def Entrance_VK(logins:str, passwords:str)-> True:
        pass
    Entrance_VK(123,'12312')
    """
    def actual_decorator(func):
        def decorator_function(*Items, **Dicts):
            # 0.008 Длительность
            
            if Reg:
                print('___________________________________')
                print(f'Func_Name: {func.__name__}')
                if Dicts:
                    print('**Kargs: {}'.format([[x, type(x)]
                                                for x in Dicts.values()]))
                if Items:
                    print('*Arg: {}'.format([[x, type(x)] for x in Items]))

            value_function = func.__annotations__
            if value_function.get('return'):  # отчистка от ->
                value_function.pop('return')

            # Комбенированная проврека

            if Items:
                # Если значения переданы без присваивания
                # fanc(login,password_VK)
                test_Gen_Items = [x for x in zip(
                    value_function.keys(), Items, value_function.values())]
                for x in test_Gen_Items:
                    if not isinstance(x[1], x[2]):
                        raise Exception(f'\n\n*Args-| {x[0]} != {x[2]}\n')

            if Dicts:
                # Если присваиваться значение
                # fanc(passwords=password_VK)
                test_Gen_Dicts = [list(x)+[value_function.get(x[0])]
                                  for x in zip(Dicts.keys(), Dicts.values())]
                for x in test_Gen_Dicts:
                    if not isinstance(x[1], x[2]):
                        raise Exception(f'\n\n**Kargs-| {x[0]} != {x[2]}\n')

            if Reg:
                start = time.time()
                func_Time = func(*Items, **Dicts)
                print('Time: {} секунд.'.format(time.time()-start))
                print('-----------------------------------')
                return func_Time
            return func(*Items, **Dicts)
        return decorator_function
    return actual_decorator


"""

# print(iters) # Значения переданные в Декоратор !
# print(func) # Основная функций после декоратора
# print(Items) # Значения переданные в Функцию ! => tuple
# print(Dicts) # Значения переданные в Функцию ! => dict
# print(*Dicts) # Значения переданные в Функцию ! => dict

    #     print(dir(func))
    #     print(func.__annotations__)# описание def Audio_VK(vk_sessions:vk_api.vk_api.VkApi):
    #     #print(func.__name__)# имя функции
    #     #print(func.__kwdefaults__)# все стандартные значения  функции
    #     #print(func.__globals__)#  Словарь, определяющий глобальное пространство имен
    #     #print(dir(func.__eq__))#?
    #     #print(func.__doc__)# Строка документирования
    #     #print(func.__dict__)# Словарь, содержащий атрибуты функции
    #     #print(dir(func.__delattr__))# ?
    #     #print(func.__defaults__) # Кортеж с аргументами по умолчанию
    #     #print(dir(func.__code__))# не надо
    #     #print(func.__class__)# прсто класс
    #     #print(dir(func.__call__)) # ?

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

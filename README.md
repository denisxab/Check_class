# Check_class
Проверка Класса
```python

from Check_class import Check_class


@Check_class({'arr_str':int})

def Fanc(arr_str, int_s):
    return "ВЫПОЛЕННО"

print(Fanc(arr_str='123',int_s='s1'))

# (False, {'Error Type': ('arr_str', '123', <class 'int'>)})


```

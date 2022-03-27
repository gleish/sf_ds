from decimal import Decimal
 
number = Decimal("4.123456789")

print()

# В этих строках - округление decimal до указанной разрядности

n1 = number.quantize(Decimal("1.00"))
n2 = number.quantize(Decimal("1.0"))
n3 = number.quantize(Decimal("1"))

print('n1 = ', n1, 'type = ', type(n1))
print('n2 = ', n2, ' type = ', type(n2))
print('n3 = ', n3, '  type = ', type(n3))

print()

# Разрешено складывать decimal с int числами, а с float - нельзя, будет ошибка
n1 = n1 + 10
n2 = n2 + 10
n3 = n3 + 10

print('n1 = ', n1, 'type = ', type(n1))
print('n2 = ', n2, ' type = ', type(n2))
print('n3 = ', n3, '  type = ', type(n3))

print()

# Преобразование decimal в int
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

print('n1 = ', n1, 'type = ', type(n1))
print('n2 = ', n2, ' type = ', type(n2))
print('n3 = ', n3, '  type = ', type(n3))

print()



'''
Изменение типа с float на int приводит к округлению не по математическим правилам!
9.353535 превращается в 9
99.85 превращается в 99
    
'''

x = 4.0000095 + 5.353535
y = int(x)
print('x, type = ', x, type(x), 'y, type = ', y, type(y))

print()


def number_types(number: float, digits_num: int=2) -> int:  

    print(number)
    print(type(number))
    print()
    number = int(number)
    print(number)
    print(type(number))
    print()
    number = float(number)
    print(number)
    print(type(number))
    print()
    number = str(number)
    print(number)
    print(type(number))
    print()
    number = float(number)
    print(number)
    print(type(number))
    print()
    number = int(number)
    print(number)
    print(type(number))
    print()
    number = float(number)
    print(number)
    print(type(number))
    print()
    
    return number

print(number_types(99.85490009995))

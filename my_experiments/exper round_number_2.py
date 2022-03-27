number = 2.35353453
digits = 3

number = str(number)
rounded = ''
length = len(number)
dot_i = length

print('length ', length)

if length < new_length:
    number = number + (new_length - length + 1) * '0'

print('number with 000', number)
print('length of number', len(number))

string = []

for i in range (0, length):
    if number[i] == '.' or number[i] == ',':
        dot_i = i
    if i < dot_i + digits + 1:
        string.append(number[i])

print('dot_i ', dot_i)
print('string ', string)       

rounded_length = dot_i + digits
new_length = dot_i + digits + 1

print('rounded_length ', rounded_length)
print('new_length ', new_length)

if int(number[new_length]) > 4:
    number[new_length - 1] = str(int(number[new_length - 1]) + 1)
    print(int(number[new_length - 1]))
    print(int(number[new_length - 1]) + 1)

string.append(number[new_length - 1])
        

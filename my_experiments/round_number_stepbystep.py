def round_number(number, digits):
   
    string = str(number)
    length = len(string)
    dot_i = 1000

    for i in range(0, length):
        print('1: ', number, ' i =', i, ' length =', length, ' string =', string)

        if string[i] == '.' or string[i] == ',': 
            dot_i = i
            print('2: ', number, ' Dot_i =', i, ' length =', length, ' string =', string)

            if length < dot_i + 1 + digits + 1: 
                string += '0' * (dot_i + 1 + digits + 1 - length)
                length = dot_i + 1 + digits
                print('3: ', number, ' i =', i, ' length =', length, ' string =', string)

            if digits == 0: 

                if int(string[i + 1]) > 4:
                    if string[i - 1] != '9': 
                        string = string[: (i - 2)] + str(int(string[i - 1]) + 1)
                    if string[i - 1] == '9': 
                        string = str(string[: (i + 1)])
                        string = round_9(string) 
                    print('4: ', number, ' i =', i, ' length =', length, ' string =', string)
                    break
                else:                 
                    print('5: ', number, ' i =', i, ' length =', length, ' string =', string)
                    break

        if digits > 0 and i > dot_i:
            print('6: ', number, ' i =', i, ' length =', length, ' string =', string)

            if i == length - 1:

                if int(string[i + 1]) > 4:
                    if string[i] != '9': 
                        string = string.replace(string[i - 1], str(int(string[i - 1]) + 1)) # проверить на точность!
                        string = str(string[: (i + 1)])
                        string = round_9(string)                   
                    print('7: ', number, ' i =', i, ' length =', length, ' string =', string)
                    break

                # СДЕЛАТЬ!
                else:
                    if string[i] != '9': 
                        string = string.replace(string[i - 1], str(int(string[i - 1]) + 1)) # проверить на точность!
                        string = str(string[: (i + 1)])
                        string = round_9(string)                   
                    print('7: ', number, ' i =', i, ' length =', length, ' string =', string)
                    break
                    
                    
                    
                    
                    print('8: ', number, ' i =', i, ' length =', length, ' string =', string)
                    break

        print('9: ', number, ' i =', i, ' length =', length, ' string =', string)
        
    return string


def round_9(num_str: str):
    
    length = len(num_str)
    reversed_str = num_str[::-1]

    #print()
    #print(reversed_str)
    #print(num_str)
    #print()
    
    for i in range(0, length):
            
        jump_over = 0
        if i == length - 1 and reversed_str[i] == '9':
            reversed_str += '0'
        if reversed_str[i + 1] == '.' or reversed_str[i + 1] == ',': 
            jump_over = 2
        if reversed_str[i] == '.' or reversed_str[i] == ',': 
            jump_over = 1
       
        #print('before: ', reversed_str, 'i: ', i, 'jump_over: ', jump_over)
        
        if jump_over == 1:
            continue
        
        if reversed_str[i] == '9' and jump_over == 0:
            
            if reversed_str[i + 1] != '9': 
                reversed_str_1 = reversed_str[:i]
                reversed_str_2 = reversed_str[i:]
                reversed_str_2 = reversed_str_2.replace(reversed_str_2[1], str(int(reversed_str_2[1]) + 1), 1)
                reversed_str_2 = reversed_str_2.replace(reversed_str_2[0], '0', 1)
                reversed_str = reversed_str_1 + reversed_str_2
                #print('after: ', reversed_str, 'i: ', i, 'jump_over: ', jump_over)
                break
            if reversed_str[i + 1] == '9': 
                reversed_str = reversed_str.replace(reversed_str[i], '0', 1)
       
        if reversed_str[i] == '9' and jump_over == 2:
            if reversed_str[i + 1 + 1] != '9': 
                reversed_str = reversed_str.replace(reversed_str[i + 1 + 1], str(int(reversed_str[i + 1 + 1]) + 1), 1)
                reversed_str = reversed_str.replace(reversed_str[i], '0', 1)
                break
            if reversed_str[i + 1 + 1] == '9': 
                reversed_str = reversed_str.replace(reversed_str[i], '0', 1)
        
    num_str = reversed_str[::-1]
    #print()
    #print(reversed_str)
    #print(num_str)
    #print()
            
    return num_str
        


print(round_number(99.45, 0))


print(round_9('99.95'))
        
                
                 
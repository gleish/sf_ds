def round_9(num_str: str):
    
    length = len(num_str)
    reversed_str = num_str[::-1]

    print()
    print(reversed_str)
    print(num_str)
    print()
    
    for i in range(0, length):
            
        jump_over = 0
        if i == length - 1 and reversed_str[i] == '9':
            reversed_str += '0'
        if reversed_str[i + 1] == '.' or reversed_str[i + 1] == ',': 
            jump_over = 2
        if reversed_str[i] == '.' or reversed_str[i] == ',': 
            jump_over = 1
       
        print('before: ', reversed_str, 'i: ', i, 'jump_over: ', jump_over)
        
        if jump_over == 1:
            continue
        
        if reversed_str[i] == '9' and jump_over == 0:
            
            if reversed_str[i + 1] != '9': 
                reversed_str_1 = reversed_str[:i]
                reversed_str_2 = reversed_str[i:]
                reversed_str_2 = reversed_str_2.replace(reversed_str_2[1], str(int(reversed_str_2[1]) + 1), 1)
                reversed_str_2 = reversed_str_2.replace(reversed_str_2[0], '0', 1)
                reversed_str = reversed_str_1 + reversed_str_2
                print('after: ', reversed_str, 'i: ', i, 'jump_over: ', jump_over)
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
    print()
    print(reversed_str)
    print(num_str)
            
    return num_str

print(round_9('12.546'))

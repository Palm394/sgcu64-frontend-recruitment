temp = {
    '0' : (' __ ','|  |','|__|'),
    '1' : ('    ','   |','   |'),
    '2' : (' __ ',' __|','|__ '),
    '3' : (' __ ',' __|',' __|'),    
    '4' : ('    ','|__|','   |'),
    '5' : (' __ ','|__ ',' __|'),
    '6' : (' __ ','|__ ','|__|'),
    '7' : (' __ ','   |','   |'),
    '8' : (' __ ','|__|','|__|'),
    '9' : (' __ ','|__|',' __|'),
    'space' : ' ',
    'dot' : (' ','·','·')
}

data = input('input: ').split(':')

def is_valid_format() :
    if 59 >= int(data[1]) >= 0 and 59 >= int(data[2]) >= 0 :
        return True
    return False

def add_num_by_pos(group,digit):
    return temp[data[group][digit]][line_number]

if is_valid_format() :
    for line_number in range(3):
        line = ''
        for group in range(3):
            for digit in range(2):
                line += add_num_by_pos(group,digit) + temp['space']
            if group != 2 :
                line += temp['dot'][line_number]
        print(line)
else:
    print('                              ')
    print('         ·           ·')
    print('__   __  ·  __   __  ·  __  __')

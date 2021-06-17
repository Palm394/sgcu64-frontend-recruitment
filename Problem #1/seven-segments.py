temp = {
    '0' : (' __ ','|  |','|__|'),
    '1' : ('    ','   |','   |'),
    '2' : (' __ ',' __|','|__ '),
    '3' : ('__ ','__|','__|'),    
    '4' : ('    ','|__|','   |'),
    '5' : (' __ ','|__ ',' __|'),
    '6' : (' __ ','|__ ','|__|'),
    '7' : ('__ ','  |','  |'),
    '8' : (' __ ','|__|','|__|'),
    '9' : (' __ ','|__|',' __|'),
    'space' : ' ',
    'colon' : (' ','·','·')
}

data = input('input: ').split(':')

if 59 >= int(data[1]) >= 0 and 59 >= int(data[2]) >= 0 :
    for line_number in range(3):
        line = ''
        for unit in range(3):
            for digit in range(2):
                line += temp[data[unit][digit]][line_number] + temp['space']
            if unit != 2 :line += temp['colon'][line_number]
        print(line)

else:
    print('error')

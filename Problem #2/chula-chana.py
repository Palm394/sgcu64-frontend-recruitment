mock_data = [
  ['Mahamakut Building',20,[]],
  ['Sara Phra Kaew',9,[]],
  ['CU Sport Complex',35,[]],
  ['Sanum Juub',44,[]],
  ['Samyan Mitr Town',112,[]],
]

while True :
  print(('''
  Welcome to Chula Chana!!!
  Available commands:
    1. Check in user
    2. Check out user
    3. Print people count
  ''').strip())

  action = int(input('Please input any number: '))
  print('-----------------------------------------------------------------')

  if action == 1 :
    print('Check in')
    phone_number = input('Enter phone number: ')

    for order in range(len(mock_data)):
      print(str(order + 1) + '. ' + mock_data[order][0])

    select_place = int(input('Please input any number: ')) - 1
    mock_data[select_place][1] += 1
    mock_data[select_place][2].append(phone_number)
    print('Checking in',phone_number,'into',mock_data[select_place][0]) 
    print('-----------------------------------------------------------------')

  elif action == 2 :
    print(2)
  elif action == 3 :
    print(3)

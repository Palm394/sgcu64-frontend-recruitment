mock_data = [
  ['Mahamakut Building',20,[]],
  ['Sara Phra Kaew',9,[]],
  ['CU Sport Complex',35,[]],
  ['Sanum Juub',44,[]],
  ['Samyan Mitr Town',112,[]],
]

def where_user_check_in(phone,req):
  for place in range(len(mock_data)):
    if phone in mock_data[place][2]:
      if place == req :
        print('Oh you already check in.')
        return
      else :
        print('Oh you move from',mock_data[place][0],'to',mock_data[req][0])

        mock_data[req][1] += 1
        mock_data[req][2].append(phone)

        mock_data[place][1] -= 1
        mock_data[place][2].remove(phone)
        return
  mock_data[req][1] += 1
  mock_data[req][2].append(phone)

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

    user_place = int(input('Please input any number: ')) - 1

    where_user_check_in(phone = phone_number,req = user_place)

    print('Checking in',phone_number,'into',mock_data[user_place][0]) 
    print('-----------------------------------------------------------------\n')

  elif action == 2 :
    print(2)
  elif action == 3 :
    print('Current Population')
    for order in range(len(mock_data)):
      print('      ' + str(order + 1) + '.',mock_data[order][0] + ':',mock_data[order][1])


# Assumption: จำนวนเริ่มต้นในแต่ละสถานที่ != 0 ให้ถือว่าลงทะเบียนด้วยวิธีอื่นๆ
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

        # add to new position
        mock_data[req][1] += 1
        mock_data[req][2].append(phone)

        # remove from old position
        mock_data[place][1] -= 1
        mock_data[place][2].remove(phone)
        return
  # case : ไม่เจอผู้ใช้ในฐานข้อมูลใดเลย (new user)
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
      print('      '+str(order + 1) + '. ' + mock_data[order][0])

    try :
      user_place = int(input('Please input number: ')) - 1
      where_user_check_in(phone = phone_number,req = user_place)
      print('Checking in',phone_number,'into',mock_data[user_place][0]) 
    except :
      print('Your input is invalid. Try again!')
      
  elif action == 2 :
    print('Check out')
    phone_number = input('Enter phone number: ')

    # find user in database and delete him,if didn't found don't do anything
    for place in mock_data:
      if phone_number in place[2]:
        place[1] -= 1
        place[2].remove(phone_number)

  elif action == 3 :
    print('Current Population')
    for order in range(len(mock_data)):
      print('      ' + str(order + 1) + '.',mock_data[order][0] + ':',mock_data[order][1])

  print('-----------------------------------------------------------------\n')

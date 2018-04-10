favorite_number={
    'Xiaoming':['1','2','3'],
    'Xiaoliu':['1','5','3'],
    'Xiaoli':['1','6','3'],
    'Xiaowang':['1','7','3']
    }

for name,numbers in favorite_number.items():
    print(name.title()+"'s favorite numbers are:")
    for number in numbers:
        print(number)

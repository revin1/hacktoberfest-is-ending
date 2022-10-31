def check_value():
    dict={'name': 'John', 'expertise': 'Math'}
    name = input('Enter a value: ')
    print(name in dict.values())
    
check_value()

try:
    with open('example_text.txt', 'r') as file:
        contents = file.read()
        print(contents)
except:
    print('Ошибка открытия файла')    
    
    
